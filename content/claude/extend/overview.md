> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Connectors, skills, and plugins

> Choose how to customize Claude: MCP connectors give it access to your tools, skills teach it how you do a task, and plugins package both as one install.

You can customize Claude with [MCP connectors](/docs/connectors/getting-started.md), [skills](/docs/skills/overview.md), and [plugins](/docs/plugins/overview.md). MCP connectors give Claude access to a tool or data source, and skills teach it how to do a task the way you or your team does it. Plugins package skills, MCP connectors, commands, and agents into one unit that you can install once and share with others.

You add all three from the [**Customize**](https://claude.ai/customize) page in claude.ai or the Claude desktop app. [Plugin feature support across platforms](/docs/plugins/platform-support.md) lists which parts of a plugin work in chat, Cowork, and Claude Code.

> [!NOTE]
>
> If you want to make a connector or plugin for other people to install, see [Build for Claude](/docs/build/overview.md). Anyone on a paid Claude plan can submit one to Anthropic's directory for review without applying to a partner program first; on Team and Enterprise, an Owner submits it.

## Choose plugins, connectors, or skills

Each card below leads to the setup page for one of the three. The last card is for Owners who manage plugins for a Team or Enterprise organization.

> **[Plugins](/docs/plugins/overview.md)**
>
> Add a set of connectors, skills, and commands with one install, such as everything for one tool, or your team's standard setup.

> **[MCP connectors](/docs/connectors/getting-started.md)**
>
> Give Claude access to a tool or data source, such as your files, calendar, issue tracker, or an internal API.

> **[Skills](/docs/skills/how-to.md)**
>
> Have Claude do a task a particular way, such as your release-note format, your contract checklist, or your weekly report.

> **[Plugins for your organization](/docs/plugins/admin.md)**
>
> If you're an Owner on a Team or Enterprise plan, choose which plugins members can add, install some for everyone, and add your organization's own.

## Compare connectors, skills, and plugins

* **[MCP connectors](/docs/connectors/getting-started.md)** connect Claude to an external service, such as your files, calendar, issue tracker, or an internal API, so Claude can read from it and act in it. Each one is a connection to an MCP server, which the service runs so Claude can reach it. In Claude's settings, connectors appear under **Connectors**
* **[Skills](/docs/skills/overview.md)** are written instructions, optionally with scripts and reference files, that Claude loads when the task you give it calls for them. Use a skill when you want Claude to follow your process for a task
* **[Plugins](/docs/plugins/overview.md)** are installable packages. One plugin can hold skills, MCP connectors, commands you run by name, and agents Claude delegates parts of a task to. You can add a skill or a connector on its own. Use a plugin when you want several of them installed and shared as one unit

When a plugin exists for a product you use, it bundles that product's connector with the skills that use it. After you add the plugin, you sign in to its connector from the plugin's page.

The diagram shows where each of the three acts when you send one request.

![Diagram read left to right. You ask in chat, Cowork, or Claude Code, and the request goes to Claude. A skill, written instructions with your steps, format, or checklist, feeds into Claude, which reads it when your request needs it. Claude calls a connector, a connection to the service's MCP server, which reads and acts in a service you use: your tools and data, such as files, calendar, chat, an issue tracker, internal APIs, and more. A dashed wrapper labeled plugin, optional, encloses the skill and the connector, captioned one package for both.](https://mintcdn.com/claude-ai/-njlLvrWxFCRdJVz/images/extend/how-connectors-skills-plugins-fit.svg?fit=max\&auto=format\&n=-njlLvrWxFCRdJVz\&q=85\&s=372738e15abde6a69704ebf43b5472f0)

## Where your connectors, skills, and plugins are available

Connectors, skills, and plugins you add in claude.ai or the desktop app are saved to your account, so you have them in chat on the web, desktop, and mobile wherever you sign in. Claude Code picks them up when you sign in there with the same account. A plugin on your account also loads in your Cowork tasks. Things you add from the Claude Code command line stay on that machine.

In chat, you can use a plugin's skills, commands, and connectors. Cowork and Claude Code also run its agents. [Plugin feature support across platforms](/docs/plugins/platform-support.md) lists each component by app.

## Next steps

* [Add your first connector](/docs/connectors/getting-started.md): connect one from the directory and use it in a conversation
* [Skills overview](/docs/skills/overview.md): turn on a skill Anthropic provides or add one of your own
* [Plugins](/docs/plugins/overview.md): find a plugin and add it to your account
* [Plugin feature support across platforms](/docs/plugins/platform-support.md): check whether a plugin's parts work where you use Claude
* [Build for Claude](/docs/build/overview.md): build a plugin or MCP server for other people and list it in Anthropic's directory
