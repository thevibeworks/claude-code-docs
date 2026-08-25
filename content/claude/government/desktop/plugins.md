> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plugins in Claude Desktop

> Find, install, create, and remove plugins in Claude Desktop for Claude for Government, and understand what plugins add in this deployment.

> **Who this is for:** Anyone who uses Claude Desktop in Claude for Government and wants to find, install, or create plugins.

A plugin is a package that adds capabilities to Claude in a single step, such as skills, slash commands, sub-agents, and hooks. Plugins work in Cowork and in Code. See the [Plugins overview](/docs/plugins/overview) for more on what a plugin can contain.

## Where plugins come from

In Claude for Government, plugins reach you in four ways:

* Your administrators add plugins for your organization, and some of them install automatically.
* You upload a plugin file you have.
* You ask Claude to create a plugin with you.
* You add a plugin marketplace and install plugins from it.

Claude for Government does not include a public plugin marketplace; your administrators add your organization's plugins. You can also add a plugin marketplace of your own from **Browse plugins**. Your deployment's network controls determine whether a marketplace can be downloaded.

## Find and install plugins

Open **Customize** in the sidebar, then **Plugins**. The organization plugins you have installed are listed under **Organization plugins**. To find the rest, select **Browse plugins** and open the **Organization** tab, which lists every plugin your administrators have made available to you.

A plugin your administrators set to install automatically is already installed. A plugin they offer for you to choose stays available on the **Organization** tab until you install it.

To install a plugin from a file, select **Add plugin**, then **Upload plugin**, and choose the plugin's `.zip` file. Claude Desktop shows a notice reminding you to install only plugins you trust, since uploaded plugins are not controlled by Anthropic. To have Claude build one, select **Add plugin**, then **Create with Claude**, and describe the plugin you want. Claude builds it for you, and you install the result.

## Manage installed plugins

Open an installed plugin to see the skills, slash commands, sub-agents, and hooks it provides, and turn individual components on or off. To remove a plugin, open it and click **Uninstall**. Most plugins you uninstall stay removed for you, including ones your administrators set to install automatically. A plugin your organization requires cannot be removed, and Claude Desktop tells you it is required by your organization if you try.

A plugin you upload or create is added only on the device you are using.

## What plugins add in Claude for Government

A plugin adds its skills, slash commands, sub-agents, and hooks, and its hooks run on your machine at defined points during a session. The connectors you can use are the ones your administrators provide, which appear under **Customize**, then **Connectors**. Connectors declared by a plugin you add yourself are not added to Claude Desktop's connectors, and a local [MCP server](/docs/connectors/overview) declared by a plugin never runs.
