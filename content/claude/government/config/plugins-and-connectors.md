> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage plugins and connectors

> Choose between plugins and connectors in Claude for Government, prepare plugin archives for upload, decide how plugins install for members, update and remove plugins, and understand how connector tool policies apply to members.

> **Who this is for:** Tenant administrators and organization owners who deliver plugins and connectors to the members they manage.

You add plugins on the **Plugins** card and connectors on the **Connectors** card of the **Config** page in the admin portal. The card controls themselves are described under [Tool and connector cards](/docs/government/config/settings#tool-and-connector-cards), and this page covers the tasks around them, from choosing between a plugin and a connector to keeping plugins up to date. To distribute skills to members, bundle them in a plugin, as described under [Skills for administrators](/docs/government/desktop/skills#skills-for-administrators).

## Plugins versus connectors

A connector gives Claude access to another service, such as a search tool your agency runs, and the **Connectors** card is the way to deliver a connector to members. A plugin is a package that changes how Claude works. It can add skills, slash commands, and sub-agents, and it can carry hooks, which are scripts a plugin author includes to run automatically at defined points during a session, such as when a session starts. For adding a connector, see [Connectors](/docs/government/connectors/overview). For what a plugin can contain across Claude products, see the [Plugins overview](/docs/plugins/overview); the Claude for Government differences are covered below.

A plugin you upload on the **Plugins** card delivers its skills, slash commands, sub-agents, and hooks to members, and its hooks run on the member's machine. In Claude for Government, a connector declared in a plugin you upload here is not connected, so to give members a connector, add it on the **Connectors** card instead.

## Plugin archive formats

The **Plugins** card accepts a single `.zip` file. The file can be one plugin package or a marketplace archive that holds several plugins, such as the downloaded ZIP of a repository that publishes a set of plugins. A single plugin package can be up to 10 MB, and a marketplace archive can be up to 15 MB.

When you upload a marketplace archive, the preview lists the plugins it found, and you select which ones to add. Only plugins whose files are packaged inside the archive are added, so an entry in the marketplace listing that points to a plugin hosted elsewhere is skipped. The plugins you add from one archive are grouped under a **Tag**, prefilled from the marketplace's name, which lets you identify the set later.

To refresh the set, upload a new version of the same marketplace archive with the same **Tag**. The preview lists any plugin you added from that marketplace before that the new version no longer contains, and you can remove those plugins in the same step.

### What a plugin archive can contain

A plugin package is laid out around a manifest at `.claude-plugin/plugin.json`. The [plugins reference](https://code.claude.com/docs/en/plugins-reference) describes the general plugin format. Claude for Government accepts the narrower set described here, so a package that follows only the general reference can be rejected. The manifest is a JSON object, saved as UTF-8 without a byte-order mark, which some Windows editors add unless told otherwise. It has two required keys. `name` becomes the plugin's identity everywhere it appears, in lowercase letters, digits, hyphens, and underscores, up to 64 characters and starting with a letter or digit. `version` is 1 to 64 characters. Add a short `description` for the preview and the plugin's row. Uploading an archive whose name matches a plugin you already added replaces that plugin, whatever the two versions say.

Content sits in a fixed set of folders, all lowercase and case-sensitive: `skills/`, `commands/`, `agents/`, `hooks/`, and `monitors/`, plus `.claude-plugin/` for the manifest and an optional `icon.png`. Each folder accepts specific file types. `commands/` and `agents/` take `.md` files, `hooks/` and `monitors/` take `.json` files, and `skills/` takes six text formats (`.md`, `.txt`, `.json`, `.yaml`, `.yml`, `.csv`). The root can also hold `README.md`, `LICENSE`, `LICENSE.txt`, `CLAUDE.md`, `CONNECTORS.md`, and `.mcp.json`. Other text files in those six formats, at the root or in folders of your own, are accepted but not used by Claude. Any other file type, anywhere in the archive, is rejected.

Apart from the optional icon, everything in an archive must be text in UTF-8. There is no way to ship a script, or any other binary asset such as an image, through the card, which is narrower than what members can add to skills on their own devices. File and folder names must be ASCII. Nothing in the archive may start with a dot apart from `.claude-plugin/` and a root `.mcp.json`: repository files such as `.github/` or `.gitattributes` must be left out, while `.gitignore` and `.DS_Store` are dropped for you.

Paths inside the zip must use forward slashes: File Explorer's **Compress to ZIP file**, 7-Zip, `tar.exe`, PowerShell 7, and Python's `zipfile` all write them, while Windows PowerShell 5.1's `Compress-Archive` can write backslash paths, which the upload rejects. A zip that wraps everything in one top folder, which is what zipping the plugin folder or downloading a repository as a ZIP produces, works, as long as the repository holds no other dot-prefixed files. The upload looks inside the wrapper. Apple's `__MACOSX/` folders are dropped quietly too. A plugin package can hold up to 50 MB of uncompressed content, whether you upload it on its own or inside a marketplace archive.

Inside `skills/`, each skill is one folder holding a `SKILL.md` whose frontmatter `name` matches the folder name, with any reference files beside it. A bare skill archive, such as a zip of just the skill folder or a `.skill` file from Claude Desktop, is not a plugin: add the manifest and move the folder under `skills/` to convert it. For the path from writing a skill to delivering it, see [Building and deploying your own skills](/docs/government/desktop/skills#building-and-deploying-your-own-skills).

In a marketplace archive, each plugin sits in its own subdirectory, and the marketplace listing points at those subdirectories. A listing entry whose source is the archive root itself, `./`, is not supported and adds nothing, so for a repository laid out as a single plugin with its own marketplace file, remove the marketplace file and upload it as one plugin.

A package is marked **Runs code** when it declares components that can run code on members' machines. That means any file under `hooks/` or `monitors/`, a `.mcp.json` at the root, or a manifest key that declares them, such as `hooks` or `mcpServers`. Manifest keys that describe the plugin, such as `name`, `version`, `description`, `author`, and `license`, leave the marker off, as do the keys that point to its skills, commands, and agents. A manifest key that the upload does not recognize turns the marker on as a precaution.

## Plugins that run code

The upload preview marks any plugin that declares components that can run code on the member's machine, for example hooks or an [MCP server](/docs/connectors/overview), and you confirm that you trust such a package before it is added. For a marketplace archive, one confirmation covers every marked plugin in the batch. After you add it, the plugin's row on the **Plugins** card keeps a **Runs code** marker, so you can see at a glance which of the plugins you have added contain these components.

The marker reflects what a plugin declares. In Claude for Government, a marked plugin's hooks run on the member's machine at defined points during a session, its local MCP server never runs, and a connector declared in a plugin you upload here is not connected.

Treat the marker as a prompt to review the package yourself. You are responsible for the plugins you distribute to members, so read each plugin's contents before you upload it.

## Install behavior

Each plugin on the **Plugins** card has an install behavior that you set when you add it and can change later on its row. **Auto-install** installs the plugin on every member's Claude Desktop without the member doing anything. **Members choose** offers the plugin to members, who install it themselves from their organization's plugins in Claude Desktop, as described in [Plugins in Claude Desktop](/docs/government/desktop/plugins).

You do not need to push anything for a plugin to reach members. Claude Desktop syncs your organization's plugin list when it starts and periodically while it runs, so an auto-installed plugin appears on its own, and a member who already has the application open receives it at the next sync. A member can remove a plugin you installed automatically, and it stays removed for that member.

In Claude Desktop, members can also add plugins of their own, by uploading a plugin file or having Claude create one, as described in [Plugins in Claude Desktop](/docs/government/desktop/plugins). Those plugins are separate from the ones you add and do not appear on the **Plugins** card.

## Where plugins are added

Plugins are added at the tenant or organization level. Plugins the tenant adds flow to every organization and appear on each organization's **Plugins** card under **From levels above**, as described under [Tool and connector cards](/docs/government/config/settings#tool-and-connector-cards). A tenant administrator can lock the plugin list, which makes it read-only for organizations, following the lock behavior in [How Config works](/docs/government/config/overview#locks). [Group levels](/docs/government/config/overview#group-specific-settings) inherit the plugins of their tenant or organization, so the **Plugins** card is read-only when you view a group.

## Update or remove a plugin

To update a plugin, upload the new version's archive. Because its name matches the plugin you added, the upload updates that plugin, the preview marks the update before you save, and members who have the plugin receive the new version automatically.

To remove a plugin, click its remove icon and save the change. Removing a plugin stops delivering it, and there is not currently a way to uninstall a plugin remotely from members' devices, so members who already installed it keep their copy until they remove it themselves, as described under [Tool and connector cards](/docs/government/config/settings#tool-and-connector-cards).

## Connector tool policies for members

You add and edit connectors on the **Connectors** card, and for each one you choose the products that receive it and set a policy for each of its tools. See [Connectors](/docs/government/connectors/overview) for the three-step wizard.

On Claude Desktop, that tool policy shapes what members experience. A tool you switch off is blocked, so Claude cannot use it. A tool you switch on is available and asks the member on every use, and members are not offered a lasting approval for it. A tool you do not list is left to the member to turn on or off, and its approval prompts follow the member's own choices, which can include lasting approval unless your organization turns that off.
