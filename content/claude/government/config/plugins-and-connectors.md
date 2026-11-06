> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage plugins and connectors

> Upload plugins in Claude for Government: archive rules, size limits, skills packaged as plugins, the Runs code marker, install behavior, updates, and removal.

> **Who this is for:** Tenant administrators and organization owners who deliver plugins and connectors to the members they manage.

You add plugins on the **Plugins** card and connectors on the **Connectors** card, under **Settings > Config** in the admin portal. The cards themselves are listed under [Integrations](https://claude.com/docs/government/config/settings.md#integrations) in Available settings.

## Plugins versus connectors

A connector gives Claude access to another service, such as a search tool your agency runs. For adding a connector, see [Connectors](https://claude.com/docs/government/connectors/overview.md), and for what its tool policy means for members, see [Tool policy](https://claude.com/docs/government/connectors/overview.md#adding-a-connector).

A plugin is a package that changes how Claude works. It can add skills, slash commands, and sub-agents, and it can carry [hooks](https://code.claude.com/docs/en/hooks), which a plugin author sets to run automatically at defined points during a session, such as a command that runs when a session starts. Its hooks run on the member's machine. A plugin can also declare MCP servers of its own, and [Plugins that run code](#plugins-that-run-code) describes how they behave.

## Plugin archive formats

On the **Config** page, open the **Plugins** card, click **Add plugins**, and drop the zip. The preview shows the plugin's name, version, description, and any [**Runs code**](#plugins-that-run-code) marker. For one plugin, choose its [install behavior](#install-behavior). The add button saves at once.

The **Plugins** card accepts a single `.zip` file. The file can be one plugin package or a marketplace archive that holds several plugins, such as the downloaded ZIP of a repository that publishes a set of plugins. A single plugin package can be up to 10 MB, and a marketplace archive can be up to 15 MB. A plugin package can hold up to 50 MB of uncompressed content, whether you upload it on its own or inside a marketplace archive.

From a marketplace archive you select which plugins to add:

* **Plugins hosted elsewhere**: Only plugins whose files are packaged inside the archive are added, so an entry in the marketplace listing that points to a plugin hosted elsewhere is skipped.
* **Layout**: In a marketplace archive, each plugin sits in its own subdirectory, and the marketplace listing points at those subdirectories. A listing entry whose source is the archive root itself, `./`, is not supported and adds nothing, so for a repository laid out as a single plugin with its own marketplace file, remove the marketplace file and upload it as one plugin.

### What a plugin archive can contain

A plugin package is laid out around a manifest at `.claude-plugin/plugin.json`. The [plugins reference](https://code.claude.com/docs/en/plugins-reference) describes the general plugin format. Claude for Government accepts the narrower set described here, so a package that follows only the general reference can be rejected.

* **Manifest**: The manifest is a JSON object, saved as UTF-8 without a byte-order mark. `name` and `version` are required. `name` becomes the plugin's identity everywhere it appears, in lowercase letters, digits, hyphens, and underscores, up to 64 characters and starting with a letter or digit. Add a short `description`.
* **Folders**: Content sits in a fixed set of folders, all lowercase and case-sensitive: `skills/`, `commands/`, `agents/`, `hooks/`, and `monitors/`, plus `.claude-plugin/` for the manifest and an optional `icon.png`. `commands/` and `agents/` take `.md` files, `hooks/` and `monitors/` take `.json` files, and `skills/` takes text files in these formats: `.md`, `.txt`, `.json`, `.yaml`, `.yml`, `.csv`.
* **Other files**: The root can also hold files such as `README.md`, `LICENSE`, and `CONNECTORS.md`. Other text files in those formats, at the root or in folders of your own, are accepted. Any other file type, anywhere in the package, is rejected.
* **Text only**: Apart from the optional icon, everything in a package must be text in UTF-8.
* **Names**: File and folder names must be ASCII. Nothing in the package may start with a dot apart from `.claude-plugin/` and a root `.mcp.json`: repository files such as `.github/` or `.gitattributes` must be left out, while `.gitignore`, `.DS_Store`, and Apple's `__MACOSX/` folders are dropped for you.
* **Zip paths**: Paths inside the zip must use forward slashes. File Explorer's **Compress to ZIP file** writes them, while Windows PowerShell 5.1's `Compress-Archive` can write backslash paths, which the upload rejects. A zip that wraps everything in one top folder, which is what zipping the plugin folder or downloading a repository as a ZIP produces, works, as long as the plugin holds no other dot-prefixed files.

### Package a skill as a plugin

To distribute skills to members, bundle them in a plugin. The smallest valid package is the manifest plus your skill folder under `skills/`:

```text theme={null}
acme-skills.zip
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── brand-guidelines/
        ├── SKILL.md
        └── palette.csv
```

Here `plugin.json` can be `{"name": "acme-skills", "version": "1.0.0", "description": "Agency writing skills"}`. Inside `skills/`, each skill is one folder holding a `SKILL.md` whose frontmatter carries a `description` and a `name` that matches the folder name, with any reference files beside it. One plugin can carry several skills, one folder per skill. The [skill authoring guide](https://claude.com/docs/skills/how-to.md) covers the format, but an upload that contains the scripts or binary assets it describes is rejected. [What a plugin archive can contain](#what-a-plugin-archive-can-contain) has the full rules.

A bare skill archive, such as a zip of the skill folder alone or a `.skill` file from [Claude Desktop](https://claude.com/docs/government/desktop/skills.md), which is a zip of the bare skill folder, is not a plugin: add the manifest and move the folder under `skills/` to convert it.

The upload checks packaging, not skill content. After [adding the plugin](#plugin-archive-formats), open Claude Desktop as a member: install the plugin if you chose [**Members choose**](#install-behavior), then give Claude a task the skill should match and confirm Claude picks it up.

## Plugins that run code

A **Runs code** marker in the upload preview warns that the plugin can run code on the member's machine, for example through hooks or an MCP server. You confirm that you trust a marked package before it is added, and for a marketplace archive one confirmation covers every marked plugin in the batch. After you add it, the plugin's row on the **Plugins** card keeps the marker. You are responsible for the plugins you distribute to members, so read each plugin's contents before you upload it, marked or not.

Claude Desktop can run a local MCP server that the plugin declares on the member's machine, or connect to a remote one. If the server does not start or connect, check [**Let members add their own connectors**](https://claude.com/docs/government/config/settings.md#let-members-add-their-own-connectors), [**Member-added connectors**](https://claude.com/docs/government/config/settings.md#member-added-connectors), and [**Blocked connectors**](https://claude.com/docs/government/config/settings.md#blocked-connectors).

## Install behavior

Each plugin on the **Plugins** card has an install behavior. To change it, set it on the plugin's row and save the change. **Auto-install** installs the plugin on every member's Claude Desktop without the member doing anything. **Members choose** offers the plugin to members, who install it themselves from their organization's plugins in Claude Desktop, as described in [Plugins in Claude Desktop](https://claude.com/docs/government/desktop/plugins.md). Plugins you add from a marketplace archive start as **Members choose**.

Claude Desktop syncs your organization's plugin list when it starts and periodically while it runs, so you do not need to push anything. A member can remove a plugin you installed automatically, and it stays removed on the device where they removed it.

**Let members add plugin marketplaces** and **Let members add their own plugins** control whether members can also add plugins of their own, as described under [Integrations](https://claude.com/docs/government/config/settings.md#member-added-plugins-and-marketplaces) in Available settings. Both are off by default. Plugins that members add are separate from the ones you add and do not appear on the **Plugins** card.

## Where plugins are added

Plugins are added at the tenant or organization level. Plugins the tenant adds flow to every organization and appear on each organization's **Plugins** card under **From levels above**. A plugin an organization adds with the same name takes priority over the tenant's for that organization's members.

A tenant administrator can lock the plugin list, under **Advanced: raw configuration** on the card, which makes it read-only for organizations, following the lock behavior in [How Config works](https://claude.com/docs/government/config/overview.md#locks).

## Update or remove a plugin

To update a plugin, go to **Settings > Config**, open the **Plugins** card, click **Add plugins**, and upload the new version's archive. An archive whose manifest `name` matches a plugin you already added replaces that plugin, whatever the two versions say, and members who have the plugin receive the new version automatically. Give each upload a new `version`, so that older Claude Desktop versions pick it up. To refresh the plugins you added from a marketplace archive, upload a new version of it with the same **Tag**, which the preview fills in from the marketplace's name. Plugins under that tag that the new archive lacks are removed unless you choose in the preview to keep them.

To remove a plugin, click its remove icon and save the change. Claude for Government stops delivering the plugin, and Claude Desktop removes it for members who have it the next time it [syncs your organization's plugin list](#install-behavior). After that sync the plugin's hooks no longer run. A new chat cannot use the plugin's skills or commands, but a chat the member was using at the time can still use them. Claude Desktop versions earlier than 1.46388.1 keep the plugin, hooks included, until the member removes it.
