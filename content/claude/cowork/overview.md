> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

> Learn about Cowork, Anthropic's agentic workspace

Cowork uses the same agentic architecture that powers Claude Code, accessible within Claude Desktop without opening the terminal. Rather than responding to prompts sequentially, Claude tackles intricate, multi-step tasks autonomously. Describe a desired outcome, then return later to completed work — polished documents, organized files, synthesized research, and more.

## Key capabilities

* **Works directly on your computer** — Claude reads and writes local files without requiring manual uploads or downloads.
* **Claude in Chrome** — Pair [Claude in Chrome](https://claude.com/chrome) with Cowork to automate your tasks on any website.
* **Sub-agent coordination** — Complex work gets divided into smaller tasks with parallel workstreams for faster results.
* **Professional outputs** — Creates polished deliverables including Excel spreadsheets with functional formulas, PowerPoint presentations, and formatted documents.

## Extend Cowork with integrations

Cowork supports the same extensibility features available across Claude products:

<Columns cols={2}>
  <Card title="Connectors" icon="plug" href="/docs/connectors/overview">
    Connect Claude to your tools and data sources using MCP.
  </Card>

  <Card title="Skills" icon="wand-magic-sparkles" href="/docs/skills/overview">
    Teach Claude reusable workflows with custom instructions.
  </Card>

  <Card title="Plugins" icon="puzzle-piece" href="/docs/plugins/overview">
    Bundle skills, connectors, and more into shareable packages.
  </Card>

  <Card title="Monitoring" icon="chart-line" href="/docs/cowork/monitoring">
    Track usage and activity across your organization.
  </Card>
</Columns>

You manage connectors, skills, and plugins from **Customize** in the sidebar. Cowork loads the ones enabled for your claude.ai account, synced at session start, and doesn't read the [Claude Code](https://code.claude.com/docs/en/skills) CLI's `~/.claude` directory on your machine. To use a skill or plugin that exists only in `~/.claude`, add it in **Customize**.
