> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Supersede older widget instances

> Keep only the newest copy of an MCP App widget active when Claude calls its tool more than once in a conversation, using a server key and BroadcastChannel.

Each time Claude calls a tool that renders an MCP App, Claude mounts a separate iframe in the conversation. No host API unmounts earlier instances when a newer one appears, so by default several live copies of the same widget stay in the conversation. Each copy independently pushes [model-context updates](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#updatemodelcontext), the data a widget feeds into Claude's context for the next turn, and [messages](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#sendmessage) to Claude.

This page is for MCP App developers whose widget represents a single piece of state, such as a shopping cart or a dashboard, where only the most recent instance should remain interactive. It shows how to use [`BroadcastChannel`](https://developer.mozilla.org/docs/Web/API/BroadcastChannel) so earlier instances disable themselves: [mint an election key on the server](#mint-the-election-key-on-the-server), [run the election in the widget](#run-the-election-in-the-widget), then [handle the production edge cases](#handle-production-edge-cases).

The snippets assume you have registered a UI resource and tool and created an `App` instance from `@modelcontextprotocol/ext-apps`. If you haven't, start with the [SDK Quickstart](https://modelcontextprotocol.github.io/ext-apps/api/documents/Quickstart.html).

## Understand how supersession works

Claude serves all widget iframes from a single connector from the same sandbox origin on `*.claudemcpcontent.com`, and the iframe sandbox includes [`allow-same-origin`](https://developer.mozilla.org/docs/Web/HTML/Element/iframe#sandbox). A `BroadcastChannel` opened in one instance therefore reaches every other instance from the same connector in the current conversation. A fixed `ui.domain` widens that scope, as [Channel scope and `ui.domain`](#channel-scope-and-ui-domain) explains.

The supersession pattern uses that shared `BroadcastChannel` to elect the newest instance:

1. **The server stamps each tool result with an election key**: it returns a `{createdAt, seq}` pair in [`structuredContent`](https://modelcontextprotocol.io/specification/latest/server/tools#structured-content), the typed JSON payload slot of an MCP tool result. `createdAt` is server wall-clock time and `seq` is a monotonic counter. Tool results are stored in the conversation transcript, so every device and every remount of the widget sees the same key.
2. **Each widget announces its key on a shared channel**: shortly after `connect()` resolves, the host delivers the tool result that mounted this widget, including its `structuredContent`, through the SDK's [`toolresult` event](https://modelcontextprotocol.github.io/ext-apps/api/types/app.AppEventMap.html). The widget reads its key from that event, opens a `BroadcastChannel`, and broadcasts the key.
3. **Any widget that sees a younger sibling marks itself superseded**: it greys out its UI, disables its buttons, and short-circuits all calls that mutate model context or inject messages.

## Mint the election key on the server

Use [`registerAppTool`](https://modelcontextprotocol.github.io/ext-apps/api/functions/server-helpers.registerAppTool.html) to register the tool, and return the key in `structuredContent` alongside your normal tool output. A per-process counter works for a demo. A production server should derive the key from something durable, such as a database row ID or a version number on the underlying record. This example registers a `show_cart` tool that returns the key with the cart contents:

```ts theme={null}
import { registerAppTool } from "@modelcontextprotocol/ext-apps/server";
import { z } from "zod";

let callSeq = 0;

registerAppTool(
  server,
  "show_cart",
  {
    title: "Show cart",
    description: "Render the user's shopping cart as an interactive widget.",
    inputSchema: { items: z.array(z.string()).optional() },
    _meta: { ui: { resourceUri: "ui://cart-demo/cart.html" } },
  },
  async ({ items }) => {
    const list = items ?? [];
    const seq = ++callSeq;
    const createdAt = Date.now();
    return {
      content: [{ type: "text", text: `Cart rendered with ${list.length} item(s).` }],
      // The election key travels with the tool result in the transcript,
      // so rehydrated widgets on any device recover the same ordering.
      structuredContent: { items: list, seq, createdAt },
    };
  },
);
```

### Understand why the key comes from the server

Client mount time doesn't reflect tool-call order. When a user reopens a stored conversation, Claude lazy-mounts widget cells as they scroll into view, so an older widget can mount after a newer one and would rank as newest in an election based on client timestamps. The server-minted key is written into the transcript at tool-call time and is identical everywhere.

## Run the election in the widget

The snippets in this section form a single module. Paste them in order into your widget entry file.

### Read the key from the `toolresult` event

Connect and read the values you need from the host: your instance ID from [`hostContext.toolInfo`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiHostContext.html#toolinfo), and the server-minted key from the `toolresult` event. The event's `structuredContent` is typed `Record<string, unknown>`, so cast it to the shape your server returns:

```ts theme={null}
import { App } from "@modelcontextprotocol/ext-apps";

type CartResult = { items?: string[]; createdAt?: number; seq?: number };

const app = new App({ name: "cart-demo", version: "1.0.0" });

let superseded = false;
let keyFinalized = false;
let orderKey: number | undefined;
let seq: number | undefined;
let items: string[] = [];

app.addEventListener("toolresult", (params) => {
  const sc = params.structuredContent as CartResult | undefined;
  if (sc?.items) items = sc.items;
  if (sc && Number.isFinite(sc.createdAt)) {
    orderKey = sc.createdAt;
    seq = Number.isFinite(sc.seq) ? sc.seq : undefined;
    keyFinalized = true;
    announce(); // defined in "Broadcast and compare on a shared channel" below
  }
});

await app.connect();
const hostContext = app.getHostContext();
const instanceId = hostContext?.toolInfo?.id ?? crypto.randomUUID();
```

### Broadcast and compare on a shared channel

Broadcast the key and compare against every sibling you hear from. The comparison is `createdAt`, tie-broken by `seq`, then by instance ID for determinism. Ignore inbound messages until your own key is finalized so you never reply with an undefined key:

```ts theme={null}
const channel = new BroadcastChannel("my-app-cart-supersede");
const peers = new Map<string, { orderKey: number; seq?: number; instanceId: string }>();

function isYounger(other: { orderKey: number; seq?: number; instanceId: string }) {
  // keyFinalized guards every call site, so orderKey is set by the time this runs.
  if (other.orderKey !== orderKey) return other.orderKey > orderKey!;
  if (other.seq != null && seq != null && other.seq !== seq) return other.seq > seq;
  return String(other.instanceId) > String(instanceId);
}

function recompute() {
  superseded = [...peers.values()].some(isYounger);
  render(); // defined in "Reflect the state in the UI" below
}

channel.onmessage = (ev) => {
  const msg = ev.data;
  if (!msg || msg.instanceId === instanceId) return;
  if (!keyFinalized) return;
  if (msg.type === "hello") {
    channel.postMessage({ type: "born", instanceId, orderKey, seq });
  }
  peers.set(msg.instanceId, msg);
  recompute();
};

function announce() {
  channel.postMessage({ type: "hello", instanceId, orderKey, seq });
  channel.postMessage({ type: "born", instanceId, orderKey, seq });
}
```

### Gate host-mutating calls on `!superseded`

The election only matters if superseded instances actually stop talking to Claude. Guard every call to [`updateModelContext`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#updatemodelcontext) or [`sendMessage`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#sendmessage):

```ts theme={null}
// addButton, card, badge: elements in your widget's DOM.
// pickRandomItem: your own helper that returns a string.

function updateModelContext() {
  if (superseded) return;
  app.updateModelContext({
    content: [{ type: "text", text: `Cart has ${items.length} item(s): ${items.join(", ")}.` }],
  });
}

addButton.onclick = () => {
  if (superseded) return;
  items.push(pickRandomItem());
  render();
  updateModelContext();
};
```

### Reflect the state in the UI

In your render function, disable buttons and show a banner that points the user to the newest instance:

```ts theme={null}
function render() {
  card.classList.toggle("superseded", superseded);
  badge.textContent = superseded ? "Superseded" : "Live";
  addButton.disabled = superseded;
}
```

## Handle production edge cases

The election in [Run the election in the widget](#run-the-election-in-the-widget) covers the common case. A production widget also accounts for channel scope under a fixed `ui.domain`, a server key that arrives late, caching the key across remounts, and the requests a custom `postMessage` bridge would drop.

### Channel scope and `ui.domain`

`BroadcastChannel` is same-origin only, and whether you set [`_meta.ui.domain`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiResourceMeta.html#domain) on your resource decides how far that origin extends:

* **Without `ui.domain`, the default**: Claude derives the iframe origin from the conversation and connector, so the broadcast is scoped to a single conversation
* **With a fixed `ui.domain`**: the origin is shared across every conversation and tab for your connector, so a fixed channel name would let a widget in one conversation supersede a widget in another

Neither `hostContext` nor the tool-call arguments include a Claude-provided conversation ID. If you need both a fixed domain and per-conversation elections, generate your own scope key on the server, such as a UUID minted once per client connection, and return it in `structuredContent` for the widget to append to the channel name.

### Fall back if the server key is delayed

The widget's `toolresult` listener in [Run the election in the widget](#run-the-election-in-the-widget) waits for the event before announcing. If you want the widget to participate in the election even when that event is slow to arrive, replace that listener with one that resolves a promise, and race the promise against a short timeout after `connect()`:

```ts theme={null}
let resolveServerKey!: (k: { orderKey: number; seq?: number }) => void;
const serverKeyReady = new Promise<{ orderKey: number; seq?: number }>(
  (r) => (resolveServerKey = r),
);

// Replaces the toolresult listener from the first widget snippet.
app.addEventListener("toolresult", (params) => {
  const sc = params.structuredContent as CartResult | undefined;
  if (sc?.items) items = sc.items;
  if (sc && Number.isFinite(sc.createdAt)) {
    resolveServerKey({ orderKey: sc.createdAt!, seq: sc.seq });
  }
});

// Place after the announce() definition in the broadcast snippet,
// so channel is initialized before announce() runs.
const serverKey = await Promise.race([
  serverKeyReady,
  new Promise<null>((r) => setTimeout(() => r(null), 1000)),
]);
orderKey = serverKey?.orderKey ?? Date.now();
seq = serverKey?.seq;
keyFinalized = true;
announce();
```

If the server key arrives after the timeout, adopt it, recompute `superseded` against the peers you have already heard from, and re-announce so siblings update their view of you. The recomputed result may flip the instance back to live.

### Don't compare server and client timestamps

If you implemented the delayed-key fallback and fall back to a client-side `Date.now()` while waiting for the server key, tag the key with its source and refuse to compare a client value against a server value. A server `createdAt` from a tool call made hours ago is always smaller than a fresh client timestamp, which would wrongly mark whichever instance happened to fall back as live. Include `keySource` in the broadcast payload, in both `announce()` and the `born` reply, and in the `peers` Map value type so siblings can read it:

```ts theme={null}
type KeySource = "server" | "client";
let keySource: KeySource = "client";

function isYounger(other: { orderKey: number; seq?: number; instanceId: string; keySource: KeySource }) {
  if ((other.keySource === "server") !== (keySource === "server")) return false;
  // keyFinalized guards every call site, so orderKey is set by the time this runs.
  if (other.orderKey !== orderKey) return other.orderKey > orderKey!;
  if (other.seq != null && seq != null && other.seq !== seq) return other.seq > seq;
  return String(other.instanceId) > String(instanceId);
}
```

### Cache the key across remounts

On claude.ai on the web, [`hostContext.toolInfo.id`](https://modelcontextprotocol.github.io/ext-apps/api/interfaces/app.McpUiHostContext.html#toolinfo) is the stable tool-use ID, so you can persist the resolved server key to `localStorage` keyed by that ID and reuse it on the next mount without waiting for the `toolresult` event again.

Treat the `localStorage` cache as an optimization rather than a correctness guarantee. On Claude iOS, `toolInfo.id` is `undefined` when a stored conversation is rehydrated, so there is no stable per-instance cache key. Detect that case and skip the cache; the server key from the `toolresult` event is the only ordering source that works on every platform.

### If you bypass the SDK `App` class

The snippets on this page use the SDK's [`App`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html) class, which handles the full host request surface and is recommended for production. A minimal `postMessage` bridge you write yourself silently drops requests the host sends to the widget, such as `ping`, a liveness check, and [`ui/resource-teardown`](https://apps.extensions.modelcontextprotocol.io/api/interfaces/app.McpUiResourceTeardownRequest.html), the host's request that the widget clean up before unmount. claude.ai on the web doesn't send either to widgets, and Claude iOS sends `ui/resource-teardown` only when the user navigates away from the conversation, so a bridge that ignores them loses nothing on those hosts.

## Next steps

* [Set `ui.domain` for Claude](/docs/connectors/building/mcp-apps/getting-started#set-ui-domain-for-claude): how to compute `_meta.ui.domain` for Claude
* [Troubleshoot MCP Apps](/docs/connectors/building/mcp-apps/troubleshooting): developer tools and fixes when a widget doesn't render
* [SDK API reference](https://modelcontextprotocol.github.io/ext-apps/api/index.html): `registerAppTool`, `App`, and `McpUiResourceMeta`
