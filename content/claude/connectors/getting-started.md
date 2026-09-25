> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started with connectors

> Connect Claude to an app or service from the Connectors directory, turn the connector on in a conversation, and manage or disconnect it later.

A connector links Claude to an outside app or service, such as your calendar, your documents, or your issue tracker, so Claude can find information there and take actions for you.

This page is for anyone who wants to add a connector to their own Claude account, in claude.ai or the Claude desktop app. You connect one from Anthropic's directory, use it in a conversation, and learn where to turn it off or disconnect it afterward.

If you already know which connector you want, open [**Customize > Connectors**](https://claude.ai/customize/connectors) and follow [Add a connector from the directory](#add-a-connector-from-the-directory).

<Note>
  * If the service you want isn't in the directory and you have its server URL, see [Add a connector that isn't in the directory](/docs/connectors/custom/add-unlisted#add-a-connector-by-url)
  * If you're building a connector, see [Build an MCP server for Claude](/docs/connectors/building/index)
  * If you're a Team or Enterprise Owner deciding which connectors your organization offers, see [Browse the directory](/docs/connectors/directory#browse-the-directory) to add them from organization settings and handle member requests
</Note>

## Before you begin

To add a connector you need:

* A Claude account, signed in at claude.ai or in the Claude desktop app
* An account with the service you're connecting. That service is run by its provider, which may require its own account or paid plan

On Team and Enterprise plans, an Owner adds a connector for the organization, and members then connect with their own account.

## Add a connector from the directory

The Connectors directory lists the connectors that Anthropic and other providers offer. You reach it from **Customize**, the page in claude.ai and the desktop app that holds your connectors, skills, and plugins.

<Steps>
  <Step title="Open the Connectors page">
    Go to [**Customize > Connectors**](https://claude.ai/customize/connectors). In the desktop app, select **Customize** in the sidebar, then **Connectors**.
  </Step>

  <Step title="Find the connector">
    Select **Discover** to browse the directory. Enter a service name in **Search connectors**, or look through the categories, then select a connector to open its page.

    Each listing carries a Verified or Community label. [Connector verification](/docs/connectors/verification) explains what each one means.
  </Step>

  <Step title="Start the connection">
    Select **Connect to Claude**. Some connectors first ask for details such as a server URL or the region your account is hosted in. Enter them and continue.

    On a Team or Enterprise plan, what you see depends on whether the connector has been added for your organization:

    * If it hasn't, you see **Request** or a note to ask an organization Owner instead of a connect button. [Request a connector on a Team plan](/docs/connectors/directory#request-a-connector-on-a-team-plan) covers what happens next
    * If you're an Owner, the button reads **Connect for your team** and adds the connector for everyone in your organization. You then connect your own account with **Connect to Claude**. To try the connector without adding it for everyone, select the arrow next to **Connect for your team**, then **Connect just for me**
  </Step>

  <Step title="Sign in to the service">
    Claude takes you to the service's sign-in page:

    * On claude.ai, the page opens in the same browser tab
    * In the desktop app, the page opens in your browser

    Sign in, review the access Claude asks for, and approve it.

    A connector that doesn't use sign-in connects as soon as you select the button, with no page to visit.
  </Step>

  <Step title="Confirm the connection">
    When sign-in finishes and you're back on the **Connectors** page, the connector is listed under **Your connectors** with the status **Connected**.
  </Step>
</Steps>

## Use the connector in a conversation

A connected connector is available in your conversations on the web, desktop, and mobile. You choose in each conversation whether Claude can use it.

<Steps>
  <Step title="Make sure the connector is on">
    In a new or existing chat, select **+** in the message box and select **Connectors**. The connector you connected is in the list with a toggle next to it. The toggle controls whether Claude can use the connector in this conversation. If it's off, turn it on.
  </Step>

  <Step title="Ask for something the service holds">
    Send a message that needs the service, such as "What's on my calendar tomorrow afternoon?" for a calendar connector or "Summarize the open issues assigned to me" for an issue tracker.
  </Step>

  <Step title="Approve the tool call">
    Claude can ask for your approval before it uses one of the connector's tools. Select **Allow once** to continue, or **Always allow** to skip the prompt for that tool from now on. You can change this later under the connector's [tool permissions](#manage-or-disconnect-a-connector).
  </Step>
</Steps>

To stop Claude from using a connector in a conversation, turn its toggle off in the same **+** menu. The connector stays connected: Claude is still signed in to the service on your account, and you can turn the toggle back on in any conversation. To sign Claude out of the service entirely, [disconnect the connector](#manage-or-disconnect-a-connector).

## Manage or disconnect a connector

Everything about a connector you've added is on its own page. Go to [**Customize > Connectors**](https://claude.ai/customize/connectors) and select the connector under **Your connectors**. From that page you can:

* **Set tool permissions**: under **Tool permissions**, choose **Always allow**, **Needs approval**, or **Blocked** for each group of tools or for a single tool
* **Disconnect**: select **Disconnect** to sign Claude out of the service. The connector stays in your list and shows **Connect**, so you can sign in again later
* **Remove**: open the three-dot menu and select **Remove** to take the connector off your account. On Team and Enterprise plans, an Owner removes a connector for the organization from **Organization settings > Connectors**

If Claude loses access to the service later, the connector's row shows **Reconnect**. Select it and sign in again.

## Where connectors work

Connectors work across the Claude apps. Each app supports these kinds:

* **claude.ai on the web**: remote connectors, including MCP Apps that display interactive content in the conversation
* **Claude desktop app**: remote connectors, plus local connectors installed as desktop extensions
* **Claude mobile app**: remote connectors
* **Claude Code**: the connectors you add in claude.ai are available in Claude Code, in the terminal and in cloud sessions, when you sign in with your Claude account. See [Use MCP servers from claude.ai](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claude-ai)
* **Cowork**: connectors and plugins

Most connectors are remote services that you sign in to, as the steps on this page describe. A local connector is a desktop extension, packaged as an MCP Bundle (MCPB), that runs on your computer in the Claude desktop app. To add one, see [Install a local connector in the desktop app](/docs/connectors/custom/add-unlisted#install-a-local-connector-in-the-desktop-app).

## Next steps

* [Connectors directory](/docs/connectors/directory): how the directory is organized and how requests work on a Team plan
* [Add a connector that isn't in the directory](/docs/connectors/custom/add-unlisted): connect Claude to any remote MCP server by its URL, or install a desktop extension
* [Install and use plugins](/docs/plugins/overview#bundled-connectors): add a plugin that bundles connectors with the skills that use them
* [Connectors, skills, and plugins](/docs/extend/overview): decide which of the three fits what you want Claude to do
