# Manage plugins for your organization

Plugin marketplaces let Team and Enterprise plan owners distribute curated plugins to everyone in their organization. You create a marketplace, add plugins to it, and control exactly which plugins your team members can see and use. Plugins you distribute appear in both chat (on the web and the Chat tab in Claude Desktop) and Claude Cowork.

Owners and Primary Owners of Team and Enterprise plans can manage organization plugins in **[Organization settings > Plugins](https://claude.ai/admin-settings/plugins)**.

**Requirements:** Cowork and Skills must both be enabled for your organization before you can use plugin marketplaces.

---

## Use Anthropic-built marketplaces

Anthropic provides built-in marketplaces of plugins for different functions, such as legal and finance. A Knowledge Work marketplace is added to your organization by default.

To add an Anthropic-built marketplace:

1. Go to **[Organization settings > Plugins](https://claude.ai/admin-settings/plugins)**.

2. Click "Add plugins."

3. Select "Browse Anthropic sources."

4. Click "Add" on each one you want to appear for everyone in your organization.

To remove the Knowledge Work marketplace if it isn't relevant to your teams:

1. Go to **[Organization settings > Plugins](https://claude.ai/admin-settings/plugins)**.

2. Find **Knowledge Work**.

3. Click the menu button in the upper right corner.

4. Select "Remove."

Anthropic-built marketplaces show readable names, like "Knowledge Work," instead of the underlying repository slug.

---

## Create your own marketplace

Beyond the Anthropic-built marketplaces, you can create your own. There are two ways to add plugins to a marketplace you create:

- **Manual upload:** Upload individual plugin ZIP files through the admin UI. Best for quick iteration, one-off tools, or teams that don't use GitHub for plugin development.

- **GitHub syncing:** Connect a private GitHub repository and Cowork automatically syncs plugins from it. Best when multiple developers collaborate on plugins or you want version-controlled updates.

You can use both approaches in parallel. For example, run a GitHub-synced marketplace for your core plugins and a separate manual marketplace for ad-hoc tools.

### Set up a manual marketplace

1. Go to **[Organization settings > Plugins](https://claude.ai/admin-settings/plugins)**.

2. Click "Add plugins" and select "Upload a file" as the source.

3. If this is your first time setting up a marketplace, "Upload to a new marketplace" is auto-selected. You'll be able to choose "Add to an existing marketplace" when uploading plugins later.

4. Enter a name for your marketplace.

5. Either drag your files in, or click the upload prompt and select your file. The file must be a valid .zip under 50 MB.

6. Repeat for each plugin you want to add.

7. Click "Upload" to add your plugins to a new marketplace.

If you upload a plugin with the same name as an existing one, it overwrites the previous version automatically. You don't need to delete the old one first.

### Set up a GitHub-synced marketplace

GitHub syncing lets you manage plugins as code in a repository. When you push changes, you can trigger a sync to update your marketplace, either manually or automatically.

**Prepare your repository**

Your repository must be **private or internal**—public repos aren't allowed for organization marketplaces. You can connect a repo hosted on github.com or on a self-hosted GitHub Enterprise Server instance.

GitHub-synced marketplaces support a narrower set of `source` types in `marketplace.json` than the Claude Code CLI does. Relative paths to plugin folders inside the connected repository (for example, `"source": "./plugins/my-plugin"`) are fully supported. The `github`, `url`, and `git-subdir` source types are supported only when the target repository is public. The `npm` and `pip` source types are not supported. If your plugin code lives in separate private repositories, copy those plugin folders into the marketplace repository (a git submodule, git subtree, or a CI step works well) and reference them with relative paths.

For details on plugin structure and formatting, see the **[plugin reference documentation](https://code.claude.com/docs/en/plugins-reference)**.

Additional resources:

- **[Create and distribute a plugin marketplace](https://code.claude.com/docs/en/plugin-marketplaces)**

- **[Create plugins](https://code.claude.com/docs/en/plugins)**

- **[Creating a new GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)**

**Connect the repository**

1. Make sure both Cowork and Skills are enabled for your organization.

  1. **[Enable Cowork](https://support.claude.com/en/articles/13455879-use-cowork-on-team-and-enterprise-plans#h_71cdc52dfc)**

  2. **[Enable Skills](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization#h_7673241237)**

2. Go to **[Organization settings > Plugins](https://claude.ai/admin-settings/plugins)**.

3. Click "Add plugin" and select "GitHub" as the source.

4. Enter the repository in `owner/repo` format (for example, `acme-corp/claude-plugins`).

Your personal GitHub token is verified to confirm you have access, then Cowork uses its GitHub App installation token for sync operations.

**Can't see your repo?** Make sure the Claude GitHub App is installed in that repository.

**How syncing works**

An initial sync runs automatically when you connect a repository. After that, organization owners can opt-in to continued automatic updates per marketplace by going to **[Organization settings > Plugins](https://claude.ai/admin-settings/plugins)**, clicking the menu button in the upper right corner of the marketplace, then toggling "Sync automatically" on:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/2193200015/a239033a9ab19fbd39f1a0d9edce/CleanShot+2026-03-23+at+11_41_31%402x.png?expires=1784796300&amp;signature=d7a6a99057c5fce02ec0a72242efd23d6043c27589164e77aae9eabb6b86eb92&amp;req=diEuFct%2BnYFeXPMW1HO4zUYv5tn%2ByHkXRDH%2FtUo5ov4n%2F1InsG89S%2FT3d7ii%0AkUWP03DS0B1Uky58EdM%3D%0A)

Enabling automatic sync creates a webhook on the connected repository. The person turning the toggle on must have admin-level access to that repository on GitHub. This is checked through their personal GitHub connection, which is separate from the Claude GitHub App installation. Without admin access, the page shows "Cannot access repository. Ensure the repository exists and the Claude GitHub App is installed," even when the App is installed correctly and manual updates work.

The Claude GitHub App's **Webhooks (Read & Write)** permission must also be approved on the installation. On installations created before this permission was introduced, GitHub shows a "Claude is requesting updated permissions" prompt that a repository or organization admin needs to approve.

Once enabled, automatic sync runs when a pull request that includes a plugin version bump is merged to the repository's default branch. Direct pushes to the default branch don't trigger a sync. You can always trigger a sync manually by clicking "Update" on the marketplace.

During a sync, Cowork compares the latest commit in your repo against the last-synced commit. If nothing has changed, the sync is skipped. If there are changes, Cowork reads the manifest, validates each plugin, and replaces all plugins in the marketplace with the current state of the repo. Syncs can take up to 30 minutes depending on the number of plugins.

**Important:** If a sync fails, plugins may be temporarily removed for your team members. If this happens, check the failure message, fix the issue in your repo, push the update, and trigger the sync again. Once the sync succeeds, verify that your installation preferences are still set correctly, since they may have been reset during the failure.

### Choose between manual upload and GitHub sync

| **Scenario**                                         | **Recommended approach** |
| ---------------------------------------------------- | ------------------------ |
| Plugins are maintained in version control with CI/CD | GitHub sync              |
| Multiple developers collaborate on plugins           | GitHub sync              |
| You want automatic update propagation                | GitHub sync              |
| You need more than 100 plugins in a marketplace      | GitHub sync              |
| Quick prototyping or one-off tools                   | Manual upload            |
| Plugins built by non-engineering teams               | Manual upload            |
| Environments without GitHub access                   | Manual upload            |
| Testing a plugin before adding it to a synced repo   | Manual upload            |

---

## Control plugin distribution

Once your marketplace has plugins, you control how they're distributed using installation preferences. For each plugin, you can set one of four options:

| **Preference**        | **What it does**                                                            | **What members see**                                                                                 |
| --------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Installed by default  | Automatically installed for all org members                                 | The plugin appears in their installed list without any action. Members can uninstall if they choose. |
| Available for install | Listed in the plugin catalog                                                | Members see it when browsing plugins and can install it themselves.                                  |
| Not available         | Hidden from the catalog entirely                                            | Members can't see or install the plugin. Useful for staging or deprecating plugins.                  |
| Required              | Automatically installed for all org members without the option to remove it | The plugin appears in their installed list without any action and cannot be disabled or uninstalled. |

### Set preferences

1. In **[Organization settings > Plugins](https://claude.ai/admin-settings/plugins)**, navigate to your marketplace.

2. Select the installation preference for each plugin.

3. Changes take effect on each member's next session or plugin refresh.

### What members experience

Members browse available plugins through the **Browse plugins** modal. Auto-installed plugins appear in their installed list automatically. Available plugins show up in the catalog for self-service installation.

Members can't edit organization-managed plugins, which prevents conflicting changes to shared tooling.

---

## Customize plugin access by group

Enterprise admins can override a plugin's organization-wide installation preference for specific groups. For example, you can auto-install a plugin for the Engineering group, make it available for Legal to install on their own, and hide it from everyone else.

Group-level plugin access is available on Enterprise plans and configurable by Admins and above.

### How group overrides work

Each plugin in your marketplace has an organization-wide installation preference (Installed by default, Available for install, Required, or Not available). By default, every group inherits that organization-wide setting.

When you set a group-level override for a plugin, it replaces the org-wide setting for members of that group. The resolution order is: group setting, then org-wide setting, then marketplace default.

### Set plugin access for a group

1. In **[Organization settings > Plugins](https://claude.ai/admin-settings/plugins)**, navigate to your marketplace.

2. Find the plugin you want to customize.

3. In the **Custom access** column, click “Add groups.”

4. Select the group and choose one of the installation preferences listed above.

Both manually created groups and SCIM-provisioned groups from your identity provider appear in the group picker and work the same way.

### What happens when a member is in multiple groups

If a member belongs to two or more groups with different settings for the same plugin, the **most permissive** setting applies. The order from most to least permissive is: Required > Installed by default > Available for install > Not available.

For example, if Group A sets a plugin to "Not available" and Group B sets it to "Installed by default," a member in both groups gets the plugin installed by default.

**Note:** This differs from how group spend limits resolve. Spend limits apply either the higher or lower group value depending on your **Multi-group spend limit** setting. Plugin access applies the most permissive value, because groups here are meant to enable access for teams that need a tool, not to act as a security boundary. If you need to hard-block a plugin, set its org-wide preference to "Not available" and only grant access to the groups that should have it.

### What happens when a group is deleted

If a group is removed (for example, deleted from your identity provider), the override remains in the admin UI but is flagged as orphaned. It has no effect on members (since no one belongs to a deleted group) and doesn't count toward the custom access badge. You can clear orphaned overrides from the plugin's custom access settings.

### Do group settings persist across marketplace re-syncs?

Yes. Group-level overrides persist when you re-sync a GitHub-connected marketplace. They're only removed if the plugin itself is deleted from the marketplace.

---

## Update and remove plugins

### Manual marketplaces

To update a plugin, upload a new ZIP file with the same plugin name. The new version overwrites the existing one automatically. Plugin names are the unique identifier, so `legal` will always replace `legal`.

To remove a plugin, delete it from your marketplace in **[Organization settings > Plugins](https://claude.ai/admin-settings/plugins)**.

### GitHub-synced marketplaces

Push your changes to the connected repository, then go to **[Organization settings > Plugins](https://claude.ai/admin-settings/plugins)**, find your marketplace, and click "Update" to trigger a sync. Each sync replaces all plugins with the current state of the repo. If an owner has enabled "Sync automatically" for the marketplace, a sync also runs whenever a pull request with a plugin version bump is merged to the repository's default branch.

To remove a plugin, delete it from the repository and trigger a sync.

---

## Limits

| **Limit**                                 | **Value**                | **Notes**                                                                        |
| ----------------------------------------- | ------------------------ | -------------------------------------------------------------------------------- |
| Max plugin ZIP size (upload)              | 50 MB                    | Enforced both client-side and server-side                                        |
| Max plugins per marketplace (manual)      | 100                      | Per marketplace                                                                  |
| Max plugins per marketplace (GitHub sync) | 500                      | Per marketplace                                                                  |
| Max plugin name length                    | 64 characters            | Must use lowercase words separated by hyphens                                    |
| Sync timeout                              | 30 minutes               | Per sync operation                                                               |
| GitHub repo visibility                    | Private or internal only | Hosted on github.com or GitHub Enterprise Server. Public repos aren't supported. |

---

## Naming rules

Plugin names must use **lowercase words separated by hyphens** (for example, `deployment-tools`, not `Deployment Tools`). The following marketplace names are reserved and can't be used:

- `claude-code-marketplace`

- `claude-code-plugins`

- `claude-plugins-official`

- `anthropic-marketplace`

- `anthropic-plugins`

- `agent-skills`

- `life-sciences`

Names that impersonate official Anthropic marketplaces are also blocked.

**Note:** Plugin authors can set a `displayName` so a plugin shows a readable name in the catalog instead of its slug. If an author doesn't set one, the plugin shows its slug (for example, `deployment-tools`).

---

## Troubleshooting

### Upload rejected

Common causes: the file exceeds 50 MB, it isn't a valid ZIP file, or the marketplace has reached the 100-plugin limit. Check the file size and format, and remove unused plugins if you're at capacity.

### Plugin not appearing for members

Check the plugin's installation preference in your marketplace settings. If it's set to **Not available**, members won't see it. Also confirm that Cowork and Skills are both enabled for your organization.

### Updated plugin not reflecting for members

Changes take effect on each member's next session or plugin refresh. If the update still isn't showing, confirm the upload succeeded by checking the plugin version in your marketplace.

### GitHub sync fails with a content error

One or more plugins in your repo is likely formatted incorrectly. Fix the formatting issue, push the update to GitHub, and trigger the sync again. For plugin structure requirements, see the **[plugin reference documentation](https://code.claude.com/docs/en/plugins-reference)**.

### Sync fails with "External plugin sources are not yet supported," or plugins are skipped with "Repository not found on github.com. Check the URL and make sure the repository is public."

One or more plugin entries in your `marketplace.json` use a `source` that points outside the connected repository (a `github`, `url`, or `git-subdir` source), and the target repository is private. The organization sync can currently only fetch external sources from public repositories. Move the plugin folders into the marketplace repository and change each entry's `source` to a relative path (for example, `"./plugins/my-plugin"`), then push and re-sync. Alternatively, upload the affected plugins individually via **Customize > Add plugin > Create plugin > Upload plugin**.

### Plugins disappeared after a failed sync

A failed GitHub sync can temporarily remove plugins from your marketplace. Fix the underlying issue, re-sync successfully, then verify that installation preferences are set correctly, since they may have been reset.

### Can't see a GitHub repo when connecting

Make sure the Claude GitHub App is installed in that repository. Your personal GitHub token is checked first to confirm access, but the sync itself uses the GitHub App installation token.

### "Cannot access repository" when turning on "Sync automatically"

If manual updates work but turning on "Sync automatically" shows "Cannot access repository. Ensure the repository exists and the Claude GitHub App is installed," there are two likely causes:

- **You don't have admin access to the repository.** Turning on automatic sync creates a webhook, which requires admin-level access to the repo through your personal GitHub connection. Ask a repository admin to enable the toggle, or have your GitHub access upgraded.

- **The Claude GitHub App's Webhooks permission hasn't been approved.** On older installations, GitHub shows a "Claude is requesting updated permissions" prompt. A repository or organization admin needs to approve the **Webhooks (Read & Write)** permission on the installation.