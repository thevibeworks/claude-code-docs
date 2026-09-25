> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Skills overview

> Find, turn on, and use skills: directories of instructions, scripts, and resources that Claude loads to handle specific tasks

Skills are directories containing instructions, scripts, and resources that Claude dynamically loads to handle specific tasks. Each skill has a `SKILL.md` file that defines when it should be activated and what instructions Claude should follow.

This page is for people who want to find, turn on, and use skills in Claude.

<Note>
  * Skills are available on Pro, Max, Team, and Enterprise plans. They run in Claude's code sandbox, so **Code execution and file creation** must be on: turn it on under [**Settings > Capabilities**](https://claude.ai/settings/capabilities), or on Team and Enterprise plans ask an Owner to turn it on under **Organization settings > Capabilities**
  * If you want to write a skill of your own, see [Create custom skills](/docs/skills/how-to)
</Note>

For the steps, go to [Find, turn on, and use skills](#find-turn-on-and-use-skills).

## Understand how skills work

Claude doesn't read every skill in full at the start of a conversation. It works through three stages:

* **Knows what's available**: Claude sees each skill's name and one-line description
* **Loads the one that fits**: when your request matches a description, Claude reads that skill's `SKILL.md` instructions
* **Opens extra files only when needed**: if the instructions point to scripts or reference files, Claude opens them at that point

A skill's description matters because it's the only part Claude sees before deciding to use the skill.

## Find, turn on, and use skills

All of your skills are listed at [**Customize > Skills**](https://claude.ai/customize/skills) in claude.ai and the desktop app, including skills that came inside a plugin.

<Steps>
  <Step title="Open Customize > Skills">
    The **Your skills** tab lists the skills you have, grouped by where they came from: **Created by you**, **From your organization**, **Shared with you**, and **From Anthropic & Partners**. The **Discover** tab lists skills you can add.
  </Step>

  <Step title="Turn a skill on">
    Select **Turn on** on the skill's row, or open the skill and use the switch at the top of its page. A skill's instructions and any scripts it carries run as part of your conversation, and skills someone shares with you or that you upload yourself aren't reviewed by Anthropic, so open the skill and read its `SKILL.md` and files before you turn it on.
  </Step>

  <Step title="Use it in a conversation">
    Describe your task, and Claude loads a skill that's turned on when the task matches the skill's description. To pick one yourself, type `/` in the message box and select the skill.
  </Step>
</Steps>

A plugin's skills appear on **Your skills** too, labeled with the plugin's name. They turn on and off with the plugin, which you manage from [**Customize > Plugins**](/docs/plugins/overview#manage-installed-plugins).

On Team and Enterprise plans, a skill's page also shows **Adoption**, **Activity**, and **You** figures for how much your organization and you have used it. [How a plugin is used in your organization](/docs/plugins/overview#track-plugin-usage-in-your-organization) explains each one.

## Types of skills

The skills available to you come from several sources:

* **Anthropic skills**: pre-built skills for creating Excel, Word, PowerPoint, and PDF documents that activate automatically when relevant
* **Partner skills**: skills from Anthropic's partners, built to work with their MCP connectors
* **Organization-provisioned skills**: skills that an Owner on a Team or Enterprise plan deploys organization-wide
* **Custom skills**: skills you create for specialized workflows, such as generating emails, applying brand guidelines, and integrating with your issue tracker

## Compare skills with other features

| Feature                                                                          | Purpose                                                                                                               |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **Skills**                                                                       | Task-specific procedures that Claude loads when a request matches                                                     |
| **[Plugins](/docs/plugins/overview)**                                                 | Packages that contain several skills together with connectors, commands, and agents, so that you add them as one unit |
| **[Projects](https://support.claude.com/en/articles/9517075-what-are-projects)** | Background knowledge that's always loaded in that project's chats                                                     |
| **[MCP connectors](/docs/connectors/getting-started)**                                | Connections that let Claude reach external services and data                                                          |

## Use skills beyond Claude

Skills follow the [Agent Skills specification](https://agentskills.io/specification), an open standard, so a skill you write for Claude also works in other tools that adopt the specification.

## Next steps

* [Create custom skills](/docs/skills/how-to): create, structure, and test your own skill
* [Plugins](/docs/plugins/overview): add a plugin that bundles skills with connectors and commands
* [Skills in Claude Code](https://code.claude.com/docs/en/skills): create, install, and invoke skills from the Claude Code CLI
