> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Design and Slides in Claude Desktop on 3P

> Turn on Design and Slides in Claude Desktop on 3P so that users can make designs and slide decks with Claude, and give Claude your brand with a design system

> [!NOTE]
>
> Design and Slides are in beta. They're off by default.

Design and Slides let users of [Claude Desktop on third-party (3P)](https://claude.com/docs/third-party/claude-desktop/overview.md) ask Claude for a slide deck or a design, such as a wireframe, and directly edit the result in the artifact. With design systems, you can provide brand and style templates that Claude follows when it creates designs and slides. Design and Slides require Claude Desktop 4.16336.0 or later.

## Turn on Design and Slides

### In the Enterprise Admin Console

In the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md):

1. Go to **Organization settings > Desktop 3P > Capabilities**.
2. Turn on the **Artifacts** switch. The **Design** and **Slides** switches appear under it.
3. Turn on the **Design** switch, the **Slides** switch, or both.
4. Click **Save changes**.

A [group's permission policy](https://claude.com/docs/third-party/claude-desktop/admin-console.md#per-group-permission-policies) has the same switches, and its settings override the organization's settings for that group.

### In MDM or a bootstrap server

Set these keys in your [MDM configuration](https://claude.com/docs/third-party/claude-desktop/configuration-format.md) or [bootstrap response](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#response-schema). To turn on only one of Design and Slides, leave out the other's key.

```json theme={null}
{
  "artifactsEnabled": true,
  "artifactsDesignEnabled": true,
  "artifactsSlidesEnabled": true
}
```

The other two keys work only while `artifactsEnabled` is `true`. `artifactsEnabled` controls only Design and Slides artifacts, so live artifacts (interactive pages) don't depend on it.

## Use Design and Slides

Design and Slides work in [Unified Claude](https://claude.com/docs/third-party/claude-desktop/unified-claude.md), which is on by default. All of a user's designs and decks are listed under **Artifacts** in the sidebar. To export one, users open it, click its title, and click **Export**. To delete one, they right-click it in the list and click **Delete**. You don't need to allow any hosts for Design and Slides, other than your plugin marketplace if you provide design systems, and Design and Slides work with [`disableNonessentialServices`](https://claude.com/docs/third-party/claude-desktop/configuration#disablenonessentialservices) on.

Claude's design and deck tools aren't available in Code sessions or in runs of [scheduled tasks](https://claude.com/docs/third-party/claude-desktop/scheduled-tasks.md).

These restrictions apply to Design and Slides in Claude Desktop on 3P:

* **Sharing with other users**: not available.
* **Comments**: users can comment on designs and decks. They can also send a comment to Claude, with **Send to Claude** or `@claude`. The comment goes to the chat or Cowork task that the design or deck was last open beside, or else to the chat or task that made the design or deck. If each of those is a Cowork task that is archived or deleted, or if the design or deck never had a chat or task, a comment sent from the design's or deck's own page starts a new Cowork task, unless Cowork is off. Claude's comment tools show Claude only the comment threads sent to Claude. Claude can reply to those threads and mark them as resolved without asking the user.
* **Export**: designs export to HTML, PDF, and PNG, and **Entire project (.zip)** exports a design's pages, files, and uploads. Decks export to PowerPoint, PDF, and HTML. In Claude Desktop 6.28899.2 or later, users can also export a slide as PNG. Users can't export a design to PowerPoint, or send designs and decks to Google Slides, other tools, or Claude Code.
* **Connectors**: designs and decks can't use connectors.
* **Web content**: designs and decks don't load images, fonts, or scripts from the web in Claude Desktop. Their exported HTML files can, when someone opens them in a browser.
* **Migration**: the [migration to Claude Enterprise](https://claude.com/docs/third-party/claude-desktop/move-to-claude-enterprise.md) and a [Claude Desktop export](https://claude.com/docs/third-party/claude-desktop/import.md#what-a-claude-desktop-export-moves) leave out designs, decks, and the design systems that users added on the computer. Before you move to Claude Enterprise, have users export to files the designs and decks that they need. The originals stay on the computer. To move them to a new device, [copy the data](https://claude.com/docs/third-party/claude-desktop/data-storage.md#copy-the-data-to-the-new-device). In Claude Desktop 7.37095.0 or later, the [automatic import of earlier third-party sessions](https://claude.com/docs/third-party/claude-desktop/import.md#automatic-import-of-earlier-third-party-sessions) includes designs and decks, but not the design systems that users added on the computer.

## Design systems

A design system gives Claude your brand: your colors, type, logos, and rules, in a folder of plain files. Claude uses it when it creates designs and slide decks. Design systems require Claude Desktop 5.11492.0 or later. **Artifacts** must be on, and so must **Design**, **Slides**, or both. In versions before 6.6395.0, **Design** must be on.

| | On one computer | For your organization |
| - | - | - |
| **Who sets it up** | Any user, in Settings | An admin, as a plugin |
| **Who can use it** | The user who added it | All users your settings reach |
| **How you update it** | Choose the folder again | Publish a new version and change the commit in your settings |

Users can have both kinds and choose which one Claude uses.

### Create a design system

Write the files yourself, or have Claude draft them with a skill:

1. Put your brand's logos, fonts, guidelines, and any decks or code that show the brand well in one folder.
2. Start a conversation from the home screen, add that folder with **Project or folder**, type `/`, choose **draft-design-system**, and describe what you want. For example: "Draft a design system for Acme from the files in this folder."
3. Claude writes the design system as a new folder, and tells you what it assumed and what's missing.

A design system has these files. To change them later, edit them yourself or ask Claude.

| File or folder | What it holds |
| - | - |
| `README.md` | Your brand in words: voice, look, and the rules that always apply. Claude reads all of it every time, so keep it short. Claude finds your other files through it, so name each one by its path. You can also use this file to list skills that you want Claude to follow, but Claude may not always use them, so write the rules that matter most here. |
| `tokens.json` | Your exact colors, text styles, spacing, and corner radius. Give each a name and a note on when to use it. |
| `tokens.css` | The same values as a stylesheet, which also loads your fonts in designs. If you edit `tokens.json`, make the same change here. |
| `fonts/` | Font files: `.woff2`, `.woff`, `.ttf`, or `.otf`. Include only fonts whose license lets you share them. |
| `assets/` | Logos, icons, and pictures, with one folder for each group. Leave out design source files such as `.ai`, `.psd`, and `.tiff`. |
| `components/` | Optional: interface parts, such as buttons, as code. |

To create a design system yourself instead of with the skill, write a `README.md`, a `tokens.json`, and a `tokens.css`. Below is an example `tokens.json`. Keep its structure, use each name only once, and write colors as hex, `rgb()`, `hsl()`, or `oklch()`.

> [accordion] Example tokens.json
>
> ```json tokens.json theme={null}
> {
>   "version": 1,
>   "color": {
>     "themes": [{ "id": "light", "name": "Light" }],
>     "tokens": [
>       { "name": "surface", "value": "#ffffff", "usage": "Page background." },
>       { "name": "ink", "value": "#1f2933", "usage": "Text on surface." },
>       { "name": "brand", "value": "#0b5fff", "usage": "Main buttons." },
>       { "name": "on-brand", "value": "#ffffff", "usage": "Text on brand." }
>     ]
>   },
>   "type": {
>     "fonts": [
>       { "family": "Acme Sans", "file": "fonts/AcmeSans-Regular.woff2", "weight": "400" },
>       { "family": "Acme Sans", "file": "fonts/AcmeSans-Bold.woff2", "weight": "700" }
>     ],
>     "families": { "sans": "\"Acme Sans\", Arial, sans-serif" },
>     "groups": [
>       {
>         "name": "Text",
>         "family": "sans",
>         "styles": [
>           { "name": "heading", "fontSize": "32px", "lineHeight": "40px", "fontWeight": 700, "usage": "Page and slide titles." },
>           { "name": "body", "fontSize": "16px", "lineHeight": "24px", "fontWeight": 400, "usage": "All other text." }
>         ]
>       }
>     ]
>   },
>   "spacing": {
>     "tokens": [
>       { "name": "space-1", "value": "8px", "usage": "Small gaps." },
>       { "name": "space-2", "value": "24px", "usage": "Large gaps." }
>     ]
>   },
>   "radius": {
>     "tokens": [{ "name": "radius-md", "value": "8px", "usage": "Cards." }]
>   }
> }
> ```

Below is an example `tokens.css` with the same values.

> [accordion] Example tokens.css
>
> ```css tokens.css theme={null}
> /* Acme Design System */
> :root {
>   --surface: #ffffff;
>   --ink: #1f2933;
>   --brand: #0b5fff;
>   --on-brand: #ffffff;
>   --space-1: 8px;
>   --space-2: 24px;
>   --radius-md: 8px;
>   --font-sans: "Acme Sans", Arial, sans-serif;
> }
>
> .heading {
>   font-family: var(--font-sans);
>   font-size: 32px;
>   line-height: 40px;
>   font-weight: 700;
> }
> .body {
>   font-family: var(--font-sans);
>   font-size: 16px;
>   line-height: 24px;
>   font-weight: 400;
> }
>
> @font-face {
>   font-family: "Acme Sans";
>   src: url("fonts/AcmeSans-Regular.woff2") format("woff2");
>   font-weight: 400;
> }
> @font-face {
>   font-family: "Acme Sans";
>   src: url("fonts/AcmeSans-Bold.woff2") format("woff2");
>   font-weight: 700;
> }
> ```

In Claude Desktop 6.6395.0 or later, you can leave out `tokens.css` when you add a folder in Settings. Claude Desktop generates it from `tokens.json`. It also replaces any `tokens.css` whose first comment says it was generated from `tokens.json`. Plugins must always include `tokens.css`.

### Add a design system on one computer

1. Go to **Settings > Design systems** and click **New design system**.
2. Choose the folder, with `README.md` at its top level, and confirm. The folder's name becomes the design system's title.
3. Open the **⋯** menu on its row to make it the default, update it, or remove it.

![Settings, Design systems, with one design system named Acme Design System. Its menu offers Update, Set as your default, and Remove.](https://mintcdn.com/claude-ai/msdr55ad2blOjJDO/images/third-party/design-systems-settings.png?fit=max\&auto=format\&n=msdr55ad2blOjJDO\&q=85\&s=e12c7297fb76bdb241f7289b5310aae8)

A design system added from a folder, with its menu open.

You can add up to 1,024 files and 256 MB. Files larger than 20 MB are skipped. If you set [`allowedWorkspaceFolders`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders), the design system folder must be inside one of the folders you allow.

### Package a design system as a plugin

To share a design system with your organization, put it in a [plugin marketplace](https://claude.com/docs/third-party/claude-desktop/extensions.md#plugin-marketplaces-admin), such as a Git repository. Make one plugin for each design system. Inside the plugin, name the folder exactly `design-system`:

> [accordion] Example repository
>
> ```text theme={null}
> acme/brands                      your repository
>   .claude-plugin/
>     marketplace.json
>   acme-design-system/            one plugin
>     .claude-plugin/
>       plugin.json
>     design-system/               the design system folder
>       README.md
>       tokens.json
>       tokens.css
>       fonts/  assets/
> ```

Add the following to `.claude-plugin/marketplace.json`:

> [accordion] Example marketplace.json
>
> ```json .claude-plugin/marketplace.json theme={null}
> {
>   "name": "acme-brands",
>   "owner": { "name": "Acme" },
>   "plugins": [
>     {
>       "name": "acme-design-system",
>       "source": "./acme-design-system"
>     }
>   ]
> }
> ```

Add the following to `acme-design-system/.claude-plugin/plugin.json`:

> [accordion] Example plugin.json
>
> ```json acme-design-system/.claude-plugin/plugin.json theme={null}
> {
>   "name": "acme-design-system",
>   "displayName": "Acme Design System",
>   "version": "1.0.0",
>   "description": "The Acme brand."
> }
> ```

| Field | Value |
| - | - |
| `name` in marketplace.json | The marketplace's name, without spaces. |
| `owner.name` | Your company or team. |
| `plugins[].name` | The plugin's name, without spaces. Put the same name in plugin.json. |
| `plugins[].source` | The plugin's folder. It must be in the same repository, not a Git submodule. |
| `displayName` | The title users see. If you leave it out, users see the plugin's name. |
| `version` | Raise it whenever you change the files. |

If you don't use Git, a marketplace can also be a [file on a web server](https://claude.com/docs/third-party/claude-desktop/extensions.md#host-the-marketplace-over-https-instead-of-git). For design systems, serve it from your inference gateway or bootstrap server. In Claude Desktop 6.6395.0 or later, you can use another web server if you set `manifestSha256` in the marketplace's entry and `sha256` for the plugin's archive in marketplace.json.

### Choose which plugins are design systems

Write each design system as `plugin@marketplace`, using both names from marketplace.json. The first design system that you list is your organization's default. In the marketplace entry, set `ref` to a full 40-character commit, not a branch or tag. For the other fields, see [Plugin marketplaces](https://claude.com/docs/third-party/claude-desktop/extensions.md#plugin-marketplaces-admin).

In the [Enterprise Admin Console](https://claude.com/docs/third-party/claude-desktop/admin-console.md):

1. Go to **Organization settings > Desktop 3P > Plugins** and add the marketplace. Enter the commit in **Ref**.
2. Go to **Organization settings > Desktop 3P > Capabilities** and list the plugins in the **Design systems** row.
3. Click **Save changes**.

![The Design systems row in the Enterprise Admin Console, listing acme-design-system@acme-brands and acme-events@acme-brands.](https://mintcdn.com/claude-ai/msdr55ad2blOjJDO/images/third-party/design-systems-console.png?fit=max\&auto=format\&n=msdr55ad2blOjJDO\&q=85\&s=8f02c0a866cc775591417eb7de33e560)

The Design systems row on the console's Capabilities page.

In MDM or on a bootstrap server, set `allowedPluginMarketplaces` and `artifactsDesignSystemPlugins`. In an MDM profile, write each list as a string, as shown in [Configuration format](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#value-types-in-a-profile-or-registry-policy).

> [accordion] Example configuration
>
> ```json theme={null}
> {
>   "allowedPluginMarketplaces": [
>     {
>       "source": "github",
>       "repo": "acme/brands",
>       "ref": "3f9c1a7be04d52816f0c9d3e8a7b64125de0f983",
>       "credentialKind": "userGit"
>     }
>   ],
>   "artifactsDesignSystemPlugins": [
>     "acme-design-system@acme-brands"
>   ]
> }
> ```

After you change the list of design systems, users see the new list once they restart Claude Desktop.

![Settings, Design systems, with Acme Design System marked Org default and Acme Events marked Organization.](https://mintcdn.com/claude-ai/msdr55ad2blOjJDO/images/third-party/design-systems-organization.png?fit=max\&auto=format\&n=msdr55ad2blOjJDO\&q=85\&s=ca900a4e60abbf58fecb7e5b0dc1a400)

What users see in Settings.

Users can choose their own default, but they can't update or remove your organization's design systems. When a user asks for a design or a deck, Claude uses the default or the one the user requests.

### If a design system doesn't appear

Open `main.log` in the app's [logs folder](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) and look for the plugin's name and one of these words:

| Word in the log | What to fix |
| - | - |
| `unpinned` | For a Git marketplace, set `ref` to the full commit. For a web server, set `manifestSha256`. |
| `external` | Move the plugin into the marketplace's own repository. |
| `unverified` | In marketplace.json, add the `sha256` of the plugin's archive. |
| No line for the plugin | Check that `plugin@marketplace` is spelled correctly, that the computer can fetch the repository, and that Artifacts and Design, Slides, or both are on. |

If the design system appears but Claude can't read it, check that its folder is named `design-system`.
