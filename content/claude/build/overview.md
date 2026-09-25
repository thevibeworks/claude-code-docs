> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Build for Claude

> Build a plugin people use inside Claude: an MCP connector to your product, skills for your workflows, optional MCP Apps UI, and a listing in the directory.

To bring your product or workflow into Claude, you build a [plugin](/docs/plugins/build): a package people add once and then use on claude.ai, in the desktop and mobile apps, in Cowork, and in Claude Code. A plugin packages whatever your integration needs, in any combination, and a plugin with only one of these pieces is complete:

* **[An MCP connector](/docs/connectors/building/index)**: include one when Claude needs to reach your product or data. It points at an MCP server that you build and host
* **[Skills](/docs/skills/how-to)**: include them to teach Claude your workflows, such as the sequence of steps, the defaults, and what good output looks like
* **[An MCP App](/docs/connectors/building/mcp-apps/getting-started)**: include one when you want the connector to show interactive UI in the conversation
* **Commands and agents**: include named actions, or specialists Claude can delegate to, which [Plugin structure and testing](/docs/plugins/build) covers

When the plugin is ready, you can [submit it](/docs/directory/publish) to Anthropic's directory at [claude.ai/directory](https://claude.ai/directory), the catalog inside Claude where people find and add plugins and connectors, so that anyone on a paid plan can add it. Anthropic checks each submission before it's listed, and there's no partner program to apply to first.

## Choose a starting page

<CardGroup cols={2}>
  <Card title="Build a plugin" icon="box" href="/docs/plugins/build" arrow>
    Lay out the plugin folder and manifest, write the skills, reference your MCP server, and test the plugin in Claude.
  </Card>

  <Card title="Write skills" icon="book-open" href="/docs/skills/how-to" arrow>
    Teach Claude your workflows: the SKILL.md frontmatter, the instructions, reference files, and scripts.
  </Card>

  <Card title="Build an MCP server" icon="server" href="/docs/connectors/building/index" arrow>
    Give the plugin access to your product or data: implement the server, set up authentication for Claude's clients, and test it.
  </Card>

  <Card title="Add interactive UI" icon="window" href="/docs/connectors/building/mcp-apps/getting-started" arrow>
    Have your MCP server show interactive components in the conversation with MCP Apps. Optional.
  </Card>
</CardGroup>

<Card title="Submit your plugin or MCP server" icon="store" href="/docs/directory/publish" horizontal arrow>
  List it in Anthropic's directory so anyone can add it: who can submit, what review involves, and the developer portal steps. Submit your MCP server as a connector too, even when your plugin references it.
</Card>

<Note>
  * If you want to connect a tool or install a plugin for yourself, see the [Customize Claude](/docs/extend/overview) tab
  * If you're not sure whether your plugin needs an MCP server at all, see [Decide what to include in your plugin](/docs/connectors/building/what-to-build)
  * If you're distributing only inside your organization, see [Roll out a plugin to your whole organization](/docs/plugins/org-rollout)
  * If you're building only for Claude Code's terminal and IDE users, see the [Claude Code plugin docs](https://code.claude.com/docs/en/plugins/create), which cover what that surface alone supports
</Note>

## Steps to build and publish a plugin

Building and publishing a plugin follows these steps in order:

1. **Lay out the plugin**: create the folder and manifest and reference any MCP server it uses. Start with [Build your first plugin](/docs/plugins/quickstart) if you haven't made one before, or [Plugin structure and testing](/docs/plugins/build) for the full layout. Chat, Cowork, and Claude Code each load different parts of a plugin, so check [Plugin feature support across platforms](/docs/plugins/platform-support) before you commit to a design.
2. **Write the skills**: teach Claude your workflows in `SKILL.md` files inside the plugin. [Create a skill](/docs/skills/how-to) covers the frontmatter, the instructions, reference files, and scripts
3. **Build the MCP server**: if the plugin needs to reach your product or data, implement the server, get authentication right for Claude's clients, and test it against Claude. Start with [Build an MCP server for Claude](/docs/connectors/building/index), or with [Build your first MCP server for Claude](/docs/connectors/building/quickstart) if you haven't written one before. A local server can also be packaged as a [desktop extension](/docs/connectors/building/mcpb).
4. **Add interactive UI**: if you want your server to show interactive components in the conversation, build them with [MCP Apps](/docs/connectors/building/mcp-apps/getting-started). This step is optional.
5. **Test it**: try the plugin in Claude before you publish it. [Test the plugin on each surface](/docs/plugins/build#test-the-plugin-on-each-surface) covers claude.ai, Cowork, and Claude Code, and [Test your MCP server](/docs/connectors/building/testing) covers adding your server as a custom connector
6. **Publish**: submit the plugin to the directory, submit its MCP server as a connector, and maintain the listing. Start with [Publish to the directory](/docs/directory/publish).
7. **Measure**: after people have it, [see whether they use it](#measure-usage-of-what-you-built).

### Tools that help you build and check a plugin

Most of the tooling for building and checking a plugin lives in [Claude Code](https://code.claude.com/docs/en/overview), Anthropic's command-line coding tool. You don't need it to use plugins, but you'll want it to build one: it validates your plugin folder, runs evals, and loads a plugin from a local folder so you can try it before you push. If you don't have it yet, [install Claude Code](https://code.claude.com/docs/en/setup) first. These are the tools to know:

* **[`claude plugin validate`](https://code.claude.com/docs/en/plugins/cli-reference#plugin-validate)**: run in your terminal to check the manifest and component files before you push
* **[`claude --plugin-dir`](https://code.claude.com/docs/en/plugins/create#load-a-directory-or-archive-for-one-session)**: start Claude Code with your plugin loaded from a local folder, so you can try its skills and commands before it's in a repository
* **[`claude plugin eval`](https://code.claude.com/docs/en/plugin-evals)**: run eval cases you write and compare Claude's results with and without your plugin. Each run is a real model call that counts against your plan's usage or your API bill
* **[`/skill-doctor`](https://code.claude.com/docs/en/skills#find-unused-skills)**: in a Claude Code session, see what each installed skill costs in context and how often Claude has invoked it
* **[`skill-creator`](/docs/skills/how-to#measure-whether-the-skill-improves-the-output)**: a skill from Anthropic that drafts a skill with you and runs it on test prompts; available in claude.ai and Claude Code
* **[`plugin-dev`](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/plugin-dev)** and **[`mcp-server-dev`](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/mcp-server-dev)**: plugins Anthropic publishes for Claude Code whose skills walk Claude through building a plugin or an MCP server with you

## Measure usage of what you built

Usage figures for a directory listing are in the developer portal, and figures for a plugin you distribute yourself or inside your organization are in Claude Code or in **Customize**. Each of these pages covers one case:

* **A plugin listed in the directory**: [How a published plugin is used](/docs/connectors/building/after-publishing#track-published-plugin-usage) covers installs, versions, how often each skill and MCP server runs, and error rates
* **A connector listed in the directory**: [Manage your directory listing](/docs/connectors/building/managing-your-listing#server-health-and-usage-metrics) covers the dashboard's server health, usage by product and by tool, and error breakdown
* **A plugin you rolled out to your organization's Claude Code users**: [Measure and evaluate plugins](https://code.claude.com/docs/en/plugins/measure) covers what a plugin costs in context, whether it's used, and the OpenTelemetry events that answer organization-wide questions
* **A plugin or skill used inside your organization on claude.ai**: [How a plugin is used in your organization](/docs/plugins/overview#track-plugin-usage-in-your-organization) covers the adoption and activity figures on its page in **Customize**

## Next steps

* [Build your first plugin](/docs/plugins/quickstart): build a small example plugin, test it, and push it to GitHub, ready to submit your own
* [Plugin structure and testing](/docs/plugins/build): the folder layout, manifest, skills, MCP server reference, and testing
* [Build an MCP server for Claude](/docs/connectors/building/index): implement the server, authentication, and testing against Claude
* [Decide what to include in your plugin](/docs/connectors/building/what-to-build): decide whether your plugin needs an MCP server, commands, agents, or UI
