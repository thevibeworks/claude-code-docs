> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Skills in Claude Desktop

> What skills are in Claude for Government, where they come from, how to create and manage your own, and how administrators distribute skills to members.

> **Who this is for:** Anyone who uses Claude Desktop in Claude for Government. The last two sections are for administrators who distribute skills to members.

A skill is a set of instructions, with optional scripts and resources, that Claude loads when a task matches it, so you can teach Claude a workflow once and reuse it. See the [Skills overview](/docs/skills/overview) for how skills work.

## Where skills come from

In Claude for Government, your skills come from three places:

* Skills you create yourself, which are stored on your device.
* Skills bundled in plugins your administrators deliver, which arrive with the plugin as described in [Plugins in Claude Desktop](/docs/government/desktop/plugins).
* Skills that ship with Claude Desktop for common document tasks, such as working with spreadsheets and presentations, which Claude loads automatically when a task calls for them.

## Create and manage skills

Open **Customize** in the sidebar, then **Skills**, to see your skills and turn any of them on or off. Select **Add skill**, then choose **Create with Claude** to build one with Claude's help, **Write skill instructions** to write it yourself, or **Upload a skill** to add a skill file you have. You can also ask Claude to save a workflow as a skill while you work on a task. The [skill authoring guide](/docs/skills/how-to) describes the file format for skills you write by hand.

Open a skill you created to rename or delete it. Skills you create are stored on your device, so they are available only there.

If your organization restricts skill creation through device managed configuration, the options to create and upload skills are hidden, and Claude does not offer to create or update skills in your conversations.

## Skills for administrators

The admin portal does not currently have a skills view or per-skill controls, so there is no setting that allows, blocks, or distributes a skill on its own. To distribute skills to the members you manage, bundle them in a plugin, which can be as small as the skill plus a plugin manifest, and add it on the **Plugins** card, as described in [Manage plugins and connectors](/docs/government/config/plugins-and-connectors).

A plugin set to **Auto-install** delivers its skills to every member without the member doing anything. A skill you distribute this way is managed through the plugin that carries it, so to change or retire the skill, update or remove the plugin.

## Building and deploying your own skills

This section walks the full path from writing a skill to delivering it to the members you manage: write the skill, package it as a plugin, upload the plugin, and check the result on a device. The packaging rules live under [Plugin archive formats](/docs/government/config/plugins-and-connectors#plugin-archive-formats).

**Write the skill.** A skill is a folder named after the skill, holding a `SKILL.md` file. The file starts with YAML frontmatter carrying `name` and `description`, followed by the instructions as markdown. The folder name must match the `name` in the frontmatter. The [skill authoring guide](/docs/skills/how-to) covers the format and what makes instructions work well. You can also have Claude help, with **Create with Claude** as described under [Create and manage skills](#create-and-manage-skills), or by asking Claude to draft the skill in a Cowork task, where those are available in your deployment. If Claude hands back a `.skill` file, keep the folder it came from instead. A `.skill` file is a zip of the bare skill folder, and the **Plugins** card accepts only plugin packages, so the folder needs the plugin wrapper described next.

**Mind the text-only rule.** A skill delivered through the admin portal can contain only text files, in these formats: `.md`, `.txt`, `.json`, `.yaml`, `.yml`, `.csv`. Skills you create on your own device can include scripts and binary assets such as images, and the skill authoring guide describes those, but a plugin upload that contains them is rejected, so keep a skill you plan to distribute textual.

**Package it as a plugin.** Arrange the skill inside a plugin and zip it. The smallest valid package is the manifest plus your skill folder under `skills/`:

```text theme={null}
acme-skills.zip
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── brand-guidelines/
        ├── SKILL.md
        └── palette.csv
```

`plugin.json` needs two keys, and a description is worth adding, for example `{"name": "acme-skills", "version": "1.0.0", "description": "Agency writing skills"}`. One plugin can carry several skills, one folder per skill. Zipping the plugin folder itself also works, since the upload accepts the single wrapping folder. Claude can do the assembly in a Cowork task: give it the layout above, paste in the full rules from [Plugin archive formats](/docs/government/config/plugins-and-connectors#plugin-archive-formats), and ask it to arrange the files and produce the zip. Claude Desktop in Claude for Government does not include a packaging skill, so put the layout in your request rather than assuming Claude knows it.

**Upload it.** On the **Config** page, open the **Plugins** card, click **Add plugins**, and drop the zip. The preview shows the plugin's name, version, and description. A plugin packaged as above, with only skills and the three manifest keys, is not marked **Runs code**. The marker and its confirmation appear when a package declares components that can run code on members' machines, or carries a manifest key the upload does not recognize, as described under [Plugins that run code](/docs/government/config/plugins-and-connectors#plugins-that-run-code). Choose **Auto-install** to deliver the skills to every member, or **Members choose** to let members install the plugin themselves.

**Check it on a device.** The upload checks packaging, not skill content, so a plugin whose `SKILL.md` is malformed uploads without complaint and simply never loads as a skill. After adding the plugin, open Claude Desktop as a member: install the plugin if you chose **Members choose**, then give Claude a task the skill should match and confirm Claude picks it up. To change the skill later, update the plugin, as described under [Update or remove a plugin](/docs/government/config/plugins-and-connectors#update-or-remove-a-plugin).
