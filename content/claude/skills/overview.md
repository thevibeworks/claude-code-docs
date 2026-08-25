> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Skills overview

> Extend Claude's capabilities with specialized instructions and workflows

Skills are directories containing instructions, scripts, and resources that Claude dynamically loads to handle specific tasks. Each skill has a `SKILL.md` file that defines when it should be activated and what instructions Claude should follow.

## Availability

Skills are available for users on Pro, Max, Team, and Enterprise plans. The Skills feature requires code execution to be enabled.

## How skills work

Skills use progressive disclosure to manage context efficiently:

1. **Metadata loading**: Claude reads skill names and descriptions at startup (\~100 tokens each)
2. **Activation**: When a task matches a skill's description, Claude loads the full `SKILL.md` content
3. **Resource loading**: Additional files (scripts, references) are loaded only when needed

This approach prevents context window overload while providing specialized capabilities on demand.

## Types of skills

* **Anthropic skills**: Pre-built skills for document creation (Excel, Word, PowerPoint, PDF) that activate automatically when relevant.
* **Partner skills**: Skills from partners like Notion, Figma, and Atlassian designed for seamless MCP connector integration.
* **Organization-provisioned skills**: Skills deployed organization-wide by Team and Enterprise administrators.
* **Custom skills**: Skills you create for specialized workflows—generating emails, applying brand guidelines, integrating with tools like JIRA or Linear, and more!

## Skills vs. other features

| Feature                          | Purpose                                                                           |
| -------------------------------- | --------------------------------------------------------------------------------- |
| **Skills**                       | Task-specific procedures that load dynamically                                    |
| **[Plugins](/docs/plugins/overview)** | Shareable packages that bundle skills, connectors, slash commands, and sub-agents |
| **Projects**                     | Static background knowledge always loaded in specific chats                       |
| **MCP**                          | Connects Claude to external services                                              |
| **Custom Instructions**          | Broad preferences applied to all conversations                                    |

## Open standard

Skills follow the [Agent Skills specification](https://agentskills.io/specification), a platform-agnostic standard. Skills you create can work across any platform adopting the standard.

See [Creating custom skills](/docs/skills/how-to) to learn how to build your own, or bundle skills into [plugins](/docs/plugins/overview) to share them with your team.

## Related topics

<Columns cols={2}>
  <Card title="Skills in Claude Code" icon="terminal" href="https://code.claude.com/docs/en/skills">
    Create, install, and invoke skills from the Claude Code CLI.
  </Card>

  <Card title="Plugins" icon="puzzle-piece" href="/docs/plugins/overview">
    Bundle skills with connectors and commands.
  </Card>
</Columns>
