> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Skills in Claude Desktop

> Skills in Claude Desktop for Claude for Government: where they come from, how to create and manage your own, and how administrators distribute them.

> **Who this is for:** Anyone who uses Claude Desktop in Claude for Government. The last section is for administrators who distribute skills to members.

A skill is a set of instructions, with optional scripts and resources, that Claude loads when a task matches it, so you can teach Claude a workflow once and reuse it.

## Where skills come from

In Claude for Government, your skills come from these places:

* Skills you create yourself.
* Skills bundled in plugins your administrators deliver, which arrive with the plugin as described in [Plugins in Claude Desktop](https://claude.com/docs/government/desktop/plugins.md).
* Skills that ship with Claude Desktop for common document tasks, such as working with spreadsheets and presentations, which Claude loads automatically when a task calls for them.

## Create and manage skills

Go to **Customize > Skills** to see your skills and turn them on or off. If your administrators let you create skills, **Add** on that page lets you write one or upload a skill file you have, and you can ask Claude to save a workflow as a skill while you work on a task. If those options are missing, your administrators haven't allowed them. The [skill authoring guide](https://claude.com/docs/skills/how-to.md) describes the file format for skills you write yourself.

Open a skill you created to delete it. Skills you create are stored on your device, so they are available only there.

## Skills for administrators

The admin portal does not have a skills view or per-skill controls, so there is no setting that allows, blocks, or distributes a skill on its own. [**Let members create skills**](https://claude.com/docs/government/config/settings.md#let-members-create-skills) controls whether members can create or upload skills of their own.

To distribute skills to the members you manage, bundle them in a plugin, as described under [Package a skill as a plugin](https://claude.com/docs/government/config/plugins-and-connectors.md#package-a-skill-as-a-plugin). A skill you distribute this way is managed through the plugin that carries it, so to change or retire the skill, [update or remove the plugin](https://claude.com/docs/government/config/plugins-and-connectors.md#update-or-remove-a-plugin).
