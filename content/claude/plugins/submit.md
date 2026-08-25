> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Submitting your plugin

> Submit your plugin to the plugin directory for Cowork

The [plugin directory](https://claude.com/plugins-for/cowork) is a community-driven directory where developers can submit plugins for use in Cowork and Claude Code. In Claude Code, this directory is surfaced as the official `claude-plugins-official` marketplace and is automatically available to all users — see [Discover and install plugins](https://code.claude.com/docs/en/discover-plugins#official-anthropic-marketplace). This is a separate and complementary directory from the [Connectors Directory](/docs/connectors/directory), which is specific to MCP connectors.

## Getting your plugin to users

Once you've built a plugin, there are several ways to get it to users:

1. **Direct install** — You can install specific plugins yourself, or guide select users to install them. This is the simplest path for internal tools or small teams.
2. **Your own plugin marketplace** — You can serve your own [plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces), which allows a subset of opted-in users to access any plugin you share. This is a great fit for enterprise contexts or communities with shared tasks. See the [Claude Code docs on sharing a marketplace](https://code.claude.com/docs/en/plugin-marketplaces) for setup instructions.
3. **[Submit to the Claude plugin directory](#submitting-your-plugin)** — You can submit to the Claude plugin directory, which is made available to all users of Cowork and Claude Code.

## Plugin Directory: Community vs. Anthropic Verified

Plugins are submitted by developers and creators in the community. Anthropic performs basic automated review on submissions before adding them to the directory. Plugins with an "Anthropic Verified" badge have undergone additional review from a quality and safety perspective. That said, there are limits to what Anthropic is able to review — you should only install plugins from developers you trust.

There are no guarantees that any community plugin will become Anthropic Verified.

<Warning>
  Exercise caution when installing community plugins. Always review a plugin's permissions, connected services, and data access before use.
</Warning>

## What makes a good plugin

The best plugins bundle related capabilities together into a coherent package that solves a specific job function or workflow end-to-end. Rather than exposing a single tool, a good plugin combines skills, connectors, slash commands, and sub-agents so Claude has everything it needs to handle a category of work.

For example, a sales plugin might bundle a CRM connector, a skill that teaches Claude your sales process, slash commands for common tasks like prospect research and call follow-ups, and a sub-agent that handles competitive analysis in parallel. Together, these components make Claude a specialist — individually, they're just building blocks.

Plugins can include any combination of:

* **Skills** — Task-specific instructions that Claude activates dynamically based on context
* **MCP connectors** — Connections to external tools and data sources. Plugins can contain any MCP, including remote MCPs, local MCPs, and MCPBs. The MCP configuration within a plugin is highly customizable.
* **Slash commands** — User-invoked commands for triggering specific workflows
* **Sub-agents** — Custom agent definitions for delegating complex work

### Guiding Claude through MCP setup

Plugins can include a `SETUP.md` skill to guide Claude through configuring and connecting any MCP servers bundled in the plugin. This lets you define step-by-step setup instructions that Claude follows when a user installs or activates your plugin.

### Using safe MCP connectors in plugins

While a plugin can include any MCP of any kind in its `.mcp.json` definition, we strongly encourage using connectors that already exist in the [Connectors Directory](/docs/connectors/directory) or come from well-known developers. This will increase the likelihood of verification and will reduce the number of warnings shown to users.

## Directory terms & conditions

All plugins in the directory must comply with:

* [Anthropic Software Directory Terms](https://support.claude.com/en/articles/13145338-anthropic-software-directory-terms)
* [Anthropic Software Directory Policy](https://support.claude.com/en/articles/13145358-anthropic-software-directory-policy)

## Security

Each plugin in the directory includes a link to where you can review its contents before installing. Plugins are capable of loading remote MCP servers, local MCP servers, and other local software tools to assist you in doing work. You should review any additional software that may be installed by a plugin, as community plugins may install unverified, third-party software that could be malicious or result in unintended behavior.

Best practices when using community plugins:

* Review the plugin's source code before installing
* Check which MCP connectors are included and what permissions they request
* Prefer Anthropic Verified plugins for production workflows
* Report any suspicious activity to Anthropic

## Submitting your plugin

To submit a plugin to the directory, share a GitHub link to your plugin. The repo must be public—closed-source plugins are not accepted.

Before submitting, run `claude plugin validate` to check formatting and structure. Review times vary with queue volume.

### Before you start

Both submission forms require you to be signed in with sufficient permissions:

* **claude.ai** requires a Team or Enterprise organization and directory management access. Organization Owners have this by default; on Enterprise, an Owner can delegate it through a custom role, as described in the [connector submission access requirements](/docs/connectors/building/submission#before-you-start).
* **Console** requires a Developer, Admin, or Owner role on a Console organization. Individual authors who aren't part of a claude.ai Team or Enterprise organization can sign up for Console at [platform.claude.com](https://platform.claude.com) and submit there.

To submit please use one of our in-app submission forms:

* **Claude.ai** — [https://claude.ai/admin-settings/directory/submissions/plugins/new](https://claude.ai/admin-settings/directory/submissions/plugins/new)
* **Console** — [https://platform.claude.com/plugins/submit](https://platform.claude.com/plugins/submit)

After you submit on claude.ai, the **Directory** page in your organization settings ([claude.ai/admin-settings/directory/submissions](https://claude.ai/admin-settings/directory/submissions)) lists your submissions with their review status.

After your plugin is published, updates pushed to your GitHub repo are picked up automatically—CI mirrors changes to the public marketplace and runs automated screening on each update. You do not need to re-submit the form for updates.

<Note>
  Need help building your plugin? See the [Claude Code plugin guide](https://code.claude.com/docs/en/plugins) for a complete walkthrough of plugin structure, manifests, and testing, or the [plugins reference](https://code.claude.com/docs/en/plugins-reference) for full technical specifications.
</Note>
