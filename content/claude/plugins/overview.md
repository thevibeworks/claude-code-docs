> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Plugins overview

> Extend Claude with reusable capability packages that bundle MCP connectors, skills, slash commands, and sub-agents

Plugins are reusable capability packages that extend Claude with custom functionality. They bundle together [MCP connectors](/docs/connectors/overview), [skills](/docs/skills/overview), slash commands, and sub-agents into a single shareable unit — turning Claude into a specialist tailored to your role, team, and company.

## What plugins do

Plugins let you define how you like work done, which tools and data to pull from, how to handle critical workflows, and what slash commands to expose so your team gets consistent outcomes. Every component is file-based, so plugins are easy to build, edit, and share.

As your team builds and shares plugins, Claude becomes a cross-functional expert. Best practices get baked into every interaction, so leaders and admins can spend less time enforcing processes and more time improving them.

## Plugin directory

To help you get started, Anthropic has open-sourced 11 plugins built and used internally:

| Plugin                 | What it does                                                  |
| ---------------------- | ------------------------------------------------------------- |
| **Productivity**       | Manage tasks, calendars, and daily workflows                  |
| **Enterprise search**  | Find information across your company's tools and docs         |
| **Sales**              | Research prospects, prep deals, and follow your sales process |
| **Finance**            | Analyze financials, build models, and track key metrics       |
| **Data**               | Query, visualize, and interpret datasets                      |
| **Legal**              | Review documents, flag risks, and track compliance            |
| **Marketing**          | Draft content, plan campaigns, and manage launches            |
| **Customer support**   | Triage issues, draft responses, and surface solutions         |
| **Product management** | Write specs, prioritize roadmaps, and track progress          |
| **Biology research**   | Search literature, analyze results, and plan experiments      |
| **Plugin Create**      | Create and customize new plugins from scratch                 |

Browse the full collection at [claude.com/plugins](https://claude.com/plugins-for/cowork) or use the Plugin Create plugin to build your own.

## Origins in Claude Code

Plugins originated in [Claude Code](https://code.claude.com/docs/en/plugins), where developers create and distribute them as versioned, shareable directories. A Claude Code plugin lives in a directory with a manifest (`plugin.json`) that defines its identity, version, and available components.

<Note>
  For technical details on plugin structure, manifests, and configuration, see the [Claude Code plugins reference](https://code.claude.com/docs/en/plugins-reference).
</Note>

## Plugins in Cowork

Plugins are fully supported in [Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork), Anthropic's agentic workspace for complex, multi-step knowledge work. In Cowork, Claude runs inside an isolated virtual machine environment, executes tasks in parallel workstreams, and writes outputs directly to your file system — and plugins extend all of that capability.

A sales plugin, for example, could connect Claude to your CRM and knowledge base, teach it your sales process, and give you slash commands for everything from prospect research to call follow-ups. You define what goes in the plugin once, and Claude pulls from that context whenever it's relevant.

## How plugins compose capabilities

| Plugin component   | What it adds                                                      | Example                                                                         |
| ------------------ | ----------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **Skills**         | Specialized instructions Claude follows when relevant tasks arise | A "brand voice" skill that activates when drafting external communications      |
| **MCP connectors** | Access to external tools and data                                 | A connector to a CRM that lets Claude read and update deal records              |
| **Slash commands** | Explicit, user-triggered workflows                                | `/sales:prospect-research` to kick off a structured research workflow           |
| **Sub-agents**     | Delegated workstreams that run in parallel                        | A sub-agent that handles competitive analysis while another drafts the proposal |

## Availability

Plugin support in Cowork is available as a beta for all paid Claude users. Plugins are currently saved locally to your machine. Org-wide sharing and management are coming in the weeks ahead.

| Platform          | Plugin support                                                     |
| ----------------- | ------------------------------------------------------------------ |
| **Claude Code**   | Full plugin support — create, install, and use plugins             |
| **Claude Cowork** | Full plugin support — plugins extend agentic, multi-step workflows |

Looking to submit your own plugin? See [Submitting your plugin](/docs/plugins/submit#submitting-your-plugin).

## Next steps

<Columns cols={2}>
  <Card title="Plugin directory" icon="grid-2" href="https://claude.com/plugins-for/cowork">
    Browse the full plugin collection.
  </Card>

  <Card title="Create plugins" icon="code" href="https://code.claude.com/docs/en/plugins">
    Build and distribute plugins in Claude Code.
  </Card>

  <Card title="Skills overview" icon="sparkles" href="/docs/skills/overview">
    Learn how skills work as a core plugin component.
  </Card>

  <Card title="Connectors overview" icon="plug" href="/docs/connectors/overview">
    Understand MCP connectors that plugins can bundle.
  </Card>
</Columns>
