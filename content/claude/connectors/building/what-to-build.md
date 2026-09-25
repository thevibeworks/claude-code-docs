> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Decide what to include in your plugin

> Decide which pieces your Claude plugin needs: an MCP connector backed by a server you host, skills, commands, agents, or UI, and how they're listed together.

When you build for people who use Claude, you build a plugin. A plugin can package any combination of these pieces:

* An MCP connector that gives Claude access to your product
* Skills that teach Claude your workflows
* Commands and agents
* Interactive UI on the connector

A plugin with only a connector or only skills is complete.

This page is for developers deciding which of those pieces their plugin needs. Once you've decided, [Plugin structure and testing](/docs/plugins/build), [Build an MCP server for Claude](/docs/connectors/building/index), and [Publish to the directory](/docs/directory/publish) cover the work.

<Note>
  * If you're choosing what to add to your own Claude rather than what to build, see [Connectors, skills, and plugins](/docs/extend/overview), which compares the three from the user's side
  * If you're building for your own organization and not listing publicly, the same decisions apply, and you distribute the result as a [custom connector](/docs/connectors/custom/add-unlisted#add-a-connector-by-url) and an [organization plugin](/docs/plugins/admin) instead of through the directory
</Note>

## Reach your product with an MCP connector

Include an MCP connector when Claude needs to read from or act in your product or data. The connector points at a remote MCP server that you build and host, with [OAuth sign-in](/docs/connectors/building/authentication) if your tools act on the user's own account. [Build an MCP server for Claude](/docs/connectors/building/index) covers the server, and [Build your first MCP server for Claude](/docs/connectors/building/quickstart) is the place to start if you haven't written one.

Once the server is live, people can use your product in chat on web, desktop, and mobile, in Cowork, and in Claude Code. Tools you add to the server later reach every plugin that references it without a new plugin release.

A plugin can reference remote and local MCP servers, and more than one of each. A remote server reaches users on every surface. A local one runs in Claude Code and in a Cowork session that runs on the user's computer in the desktop app, not in chat, so most plugins reference remote servers.

If you already have a public API or CLI that Claude can use directly, the plugin can leave the connector out: its skills teach Claude to use that API or CLI instead.

## Teach Claude your workflows with skills

Include skills when you want Claude to use your product the way it's meant to be used, instead of however each user happens to prompt. A connector on its own leaves Claude to work out your workflow from tool names. The skills are where you put the sequence of steps, the defaults, and what good output looks like.

A connector with a few well-named tools that Claude can use without guidance may not need skills. You can't submit a skill to the directory on its own, so a plugin is also how skills reach the directory.

## Add commands, agents, and UI

Commands, agents, and UI are optional pieces, and each fits a particular need:

* **Commands**: named actions people run themselves, such as `/your-plugin:weekly-report`, for tasks they start deliberately rather than describe
* **Agents**: specialists Claude can delegate part of a task to. Cowork and Claude Code run them; chat doesn't, as [Plugin feature support across platforms](/docs/plugins/platform-support) lists
* **An MCP App**: interactive UI that your connector shows in the conversation, such as a form or a chart. [Add interactive UI with MCP Apps](/docs/connectors/building/mcp-apps/getting-started) covers building one

## Package and list the plugin

Most plugins for a product include both an MCP connector and skills: the connector so Claude can reach the product, and the skills so Claude uses it the way you intend. Everything in the plugin is packaged together, so one listing gives people all of it.

When you list the plugin, submit the server too: the plugin as a plugin bundle and the server as an MCP connector. Submitting the server as a connector gives your organization the connector's listing and its dashboard, and lets you pair the two listings. [Submit your plugin, and your MCP server as a connector](/docs/directory/publish#submit-your-plugin-and-your-mcp-server-as-a-connector) explains the pairing.

The diagram shows what the server and the plugin each give people. The server gives them your connector. The plugin adds your skills and points to that same server.

<img className="block dark:hidden" src="https://mintcdn.com/claude-ai/-njlLvrWxFCRdJVz/images/extend/what-you-ship.svg?fit=max&auto=format&n=-njlLvrWxFCRdJVz&q=85&s=532adf863a7d27314b67c68b561ee94d" alt="Diagram in two columns. Left, what you ship: 1, a remote MCP server you host, with your tools; 2, a plugin holding a connector entry with your server's URL and skills that teach Claude how to use your product. Right, what people get: your connector, so Claude can reach your product, and your skills, so Claude uses it the way you intend, in Chat, Cowork, and Claude Code. Three straight arrows: from the server across to your connector, labeled people connect to it; from the plugin's connector entry up to the server, labeled points to the same server; and from the plugin's skills across to your skills, labeled people add the plugin." width="1000" height="440" data-path="images/extend/what-you-ship.svg" />

<img className="hidden dark:block" src="https://mintcdn.com/claude-ai/-njlLvrWxFCRdJVz/images/extend/what-you-ship-dark.svg?fit=max&auto=format&n=-njlLvrWxFCRdJVz&q=85&s=c68dde016b86337ca85dfa19c538d95e" alt="Diagram in two columns. Left, what you ship: 1, a remote MCP server you host, with your tools; 2, a plugin holding a connector entry with your server's URL and skills that teach Claude how to use your product. Right, what people get: your connector, so Claude can reach your product, and your skills, so Claude uses it the way you intend, in Chat, Cowork, and Claude Code. Three straight arrows: from the server across to your connector, labeled people connect to it; from the plugin's connector entry up to the server, labeled points to the same server; and from the plugin's skills across to your skills, labeled people add the plugin." width="1000" height="440" data-path="images/extend/what-you-ship-dark.svg" />

In a plugin, you reference a remote MCP server by URL. If a user has both your directory connector and your plugin installed, Claude sees one set of tools, because the plugin and the connector point at the same server.

If your plugin references an MCP URL that isn't in the directory, the user first adds it as a custom connector from the plugin's **Connectors** tab, and it then has the **Custom** label. On Team and Enterprise plans, an Owner adds the connector for the organization, and members then connect with their own account.

## Next steps

* [Plugin structure and testing](/docs/plugins/build): write the folder that packages your connector, skills, and the rest, and installs on every surface
* [Build an MCP server for Claude](/docs/connectors/building/index): implement the server and its authentication, and test it against Claude
* [Publish to the directory](/docs/directory/publish): submit the plugin, and its MCP server as a connector, from the [developer portal](https://claude.ai/directory/manage). Anyone on a paid Claude plan can submit, and on Team and Enterprise an Owner submits
