Title: Manage plugins for your organization

URL Source: https://support.claude.com/en/articles/13837433-manage-plugins-for-your-organization

Markdown Content:
Plugin marketplaces let Team and Enterprise plan owners distribute curated plugins to everyone in their organization. You create a marketplace, add plugins to it, and control exactly which plugins your team members can see and use. Plugins you distribute appear in both chat (on the web and the Chat tab in Claude Desktop) and Claude Cowork.

**Requirements:** Cowork and Skills must both be enabled for your organization before you can use plugin marketplaces.

## Use Anthropic-built marketplaces

Anthropic provides built-in marketplaces of plugins for different functions, such as legal and finance. A Knowledge Work marketplace is added to your organization by default.

To add an Anthropic-built marketplace:

To remove the Knowledge Work marketplace if it isn't relevant to your teams:

Anthropic-built marketplaces show readable names, like "Knowledge Work," instead of the underlying repository slug.

## Create your own marketplace

Beyond the Anthropic-built marketplaces, you can create your own. There are two ways to add plugins to a marketplace you create:

You can use both approaches in parallel. For example, run a GitHub-synced marketplace for your core plugins and a separate manual marketplace for ad-hoc tools.

### Set up a manual marketplace

If you upload a plugin with the same name as an existing one, it overwrites the previous version automatically. You don't need to delete the old one first.

### Set up a GitHub-synced marketplace

GitHub syncing lets you manage plugins as code in a repository. When you push changes, you can trigger a sync to update your marketplace—either manually or automatically.

**Prepare your repository**

Your repository must be **private or internal**—public repos aren't allowed for organization marketplaces. Repos hosted on custom GitHub Enterprise Server instances aren't supported. Your repo must be hosted on github.com.

GitHub-synced marketplaces support a narrower set of `source` types in `marketplace.json` than the Claude Code CLI does. Relative paths to plugin folders inside the connected repository (for example, `"source": "./plugins/my-plugin"`) are fully supported. The `github`, `url`, and `git-subdir` source types are supported only when the target repository is public. The `npm` and `pip` source types are not supported. If your plugin code lives in separate private repositories, copy those plugin folders into the marketplace repository (a git submodule, git subtree, or a CI step works well) and reference them with relative paths.

Additional resources:

**Connect the repository**

Your personal GitHub token is verified to confirm you have access, then Cowork uses its GitHub App installation token for sync operations.

**Can't see your repo?** Make sure the Claude GitHub App is installed in that repository.

**How syncing works**

An initial sync runs automatically when you connect a repository. After that, organization owners can opt-in to continued automatic updates per marketplace by going to **Organization settings > Plugins** (under **Libraries**), clicking the menu button in the upper right corner of the marketplace, then toggling "Sync automatically" on:

[![Image 1](https://downloads.intercomcdn.com/i/o/lupk8zyo/2193200015/a239033a9ab19fbd39f1a0d9edce/CleanShot+2026-03-23+at+11_41_31%402x.png?expires=1781505900&signature=d41a495b0938da8762cf396b5c2ded7a8fb76a8cbbcbbe294ff8cfd89e4d9a36&req=diEuFct%2BnYFeXPMW1HO4zUYv5tz8wXodRDH%2FtUo5ov5JjqONo5T3Mhs5g42k%0AGkHCMDmF%2FTZ140TAzbI%3D%0A)](https://downloads.intercomcdn.com/i/o/lupk8zyo/2193200015/a239033a9ab19fbd39f1a0d9edce/CleanShot+2026-03-23+at+11_41_31%402x.png?expires=1781505900&signature=d41a495b0938da8762cf396b5c2ded7a8fb76a8cbbcbbe294ff8cfd89e4d9a36&req=diEuFct%2BnYFeXPMW1HO4zUYv5tz8wXodRDH%2FtUo5ov5JjqONo5T3Mhs5g42k%0AGkHCMDmF%2FTZ140TAzbI%3D%0A)

The GitHub marketplace will then be auto-synced whenever a PR is merged to that repo. You can also trigger syncs manually by clicking “Update” on the marketplace.

During a sync, Cowork compares the latest commit in your repo against the last-synced commit. If nothing has changed, the sync is skipped. If there are changes, Cowork reads the manifest, validates each plugin, and replaces all plugins in the marketplace with the current state of the repo. Syncs can take up to 30 minutes depending on the number of plugins.

### Choose between manual upload and GitHub sync

**Scenario****Recommended approach**
Plugins are maintained in version control with CI/CD GitHub sync
Multiple developers collaborate on plugins GitHub sync
You want automatic update propagation GitHub sync
You need more than 100 plugins in a marketplace GitHub sync
Quick prototyping or one-off tools Manual upload
Plugins built by non-engineering teams Manual upload
Environments without GitHub access Manual upload
Testing a plugin before adding it to a synced repo Manual upload

## Control plugin distribution

Once your marketplace has plugins, you control how they're distributed using installation preferences. For each plugin, you can set one of four options:

**Preference****What it does****What members see**
Installed by default Automatically installed for all org members The plugin appears in their installed list without any action. Members can uninstall if they choose.
Available for install Listed in the plugin catalog Members see it when browsing plugins and can install it themselves.
Not available Hidden from the catalog entirely Members can't see or install the plugin. Useful for staging or deprecating plugins.
Required Automatically installed for all org members without the option to remove it The plugin appears in their installed list without any action and cannot be disabled or uninstalled.

### Set preferences

### What members experience

Members browse available plugins through the **Browse plugins** modal. Auto-installed plugins appear in their installed list automatically. Available plugins show up in the catalog for self-service installation.

Members can't edit organization-managed plugins, which prevents conflicting changes to shared tooling.

## Customize plugin access by group

Enterprise admins can override a plugin's organization-wide installation preference for specific groups. For example, you can auto-install a plugin for the Engineering group, make it available for Legal to install on their own, and hide it from everyone else.

### How group overrides work

Each plugin in your marketplace has an organization-wide installation preference (Installed by default, Available for install, Required, or Not available). By default, every group inherits that organization-wide setting.

When you set a group-level override for a plugin, it replaces the org-wide setting for members of that group. The resolution order is: group setting, then org-wide setting, then marketplace default.

### Set plugin access for a group

Both manually created groups and SCIM-provisioned groups from your identity provider appear in the group picker and work the same way.

### What happens when a member is in multiple groups

If a member belongs to two or more groups with different settings for the same plugin, the **most permissive** setting applies. The order from most to least permissive is: Required > Installed by default > Available for install > Not available.

For example, if Group A sets a plugin to "Not available" and Group B sets it to "Installed by default," a member in both groups gets the plugin installed by default.

### What happens when a group is deleted

If a group is removed—for example, if it's deleted from your identity provider—the override remains in the admin UI but is flagged as orphaned. It has no effect on members (since no one belongs to a deleted group) and doesn't count toward the custom access badge. You can clear orphaned overrides from the plugin's custom access settings.

### Do group settings persist across marketplace re-syncs?

Yes. Group-level overrides persist when you re-sync a GitHub-connected marketplace. They're only removed if the plugin itself is deleted from the marketplace.

## Update and remove plugins

### Manual marketplaces

To update a plugin, upload a new ZIP file with the same plugin name. The new version overwrites the existing one automatically. Plugin names are the unique identifier — `legal` will always replace `legal`.

To remove a plugin, delete it from your marketplace in **Organization settings > Plugins**.

### GitHub-synced marketplaces

Push your changes to the connected repository, then go to **Organization settings > Plugins**, find your marketplace, and click "Update" to trigger a sync. Each sync replaces all plugins with the current state of the repo. Note that if an owner has enabled "Sync automatically" for the GitHub-synced marketplace, this will happen automatically after pushing changes to the repo.

To remove a plugin, delete it from the repository and trigger a sync.

## Limits

**Limit****Value****Notes**
Max plugin ZIP size (upload)50 MB Enforced both client-side and server-side
Max plugins per marketplace (manual)100 Per marketplace
Max plugins per marketplace (GitHub sync)500 Per marketplace
Max plugin name length 64 characters Must use lowercase words separated by hyphens
Sync timeout 30 minutes Per sync operation
GitHub repo visibility Private or internal only Must be hosted on github.com. Public repos and GitHub Enterprise Server instances aren't supported.

## Naming rules

Plugin names must use **lowercase words separated by hyphens** (for example, `deployment-tools`, not `Deployment Tools`). The following marketplace names are reserved and can't be used:

Names that impersonate official Anthropic marketplaces are also blocked.

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

A failed GitHub sync can temporarily remove plugins from your marketplace. Fix the underlying issue, re-sync successfully, then verify that installation preferences are set correctly—they may have been reset.

### Can't see a GitHub repo when connecting

Make sure the Claude GitHub App is installed in that repository. Your personal GitHub token is checked first to confirm access, but the sync itself uses the GitHub App installation token.

* * *

Related Articles

[Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)[Use plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)[Install financial services plugins](https://support.claude.com/en/articles/13851150-install-financial-services-plugins)[Set up Code Review for Claude Code](https://support.claude.com/en/articles/14233555-set-up-code-review-for-claude-code)[Open the Claude mobile app with a link](https://support.claude.com/en/articles/14898120-open-the-claude-mobile-app-with-a-link)
