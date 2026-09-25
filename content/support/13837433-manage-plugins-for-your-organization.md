# Manage plugins for your organization

Plugin marketplaces let Team and Enterprise plan owners distribute curated plugins to everyone in their organization. You create a marketplace, add plugins to it, and control exactly which plugins your team members can see and use. Plugins you distribute appear in chat (on the web and the Chat tab in Claude Desktop), in Claude Cowork, and in Claude Code sessions where members sign in with the same Claude account.

Owners and Primary Owners of Team and Enterprise plans can manage organization plugins in **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)**. On Enterprise plans, members with a custom role that includes managing the organization's libraries can too.

**Requirements:** Cowork and Skills must both be enabled for your organization before you can use plugin marketplaces.

For a reference version of these controls, see **[Manage plugins for your organization](https://code.claude.com/docs/en/plugins/org)** in the Claude Code docs.

**Note:** Turning off Skills for your organization also stops skills and plugins from syncing to Claude Code, and removes the ones that already synced there. Turning off Cowork doesn't affect the sync to Claude Code. To keep skills and plugins in Claude but stop only the sync, set `syncClaudeAiSkills` and `syncClaudeAiPlugins` to `false` in Claude Code managed settings. Learn more about **[Claude Code admin setup](https://code.claude.com/docs/en/setup#advanced-setup)**.

**Note:** Marketplaces are how owners distribute plugins to their organization. Users can also share a plugin they built with specific colleagues or groups, or submit it to be published to your organization's library. Sharing and publishing are controlled by the settings in **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** in the “Policy” tab, and plugin submissions are reviewed there on the "Requests" tab. Learn more about **[using plugins in Claude](https://support.claude.com/en/articles/13837440-use-plugins-in-claude)** and **[letting users publish skills and plugins to your organization](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization#h_1abc45a27c)**[.](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization#h_1abc45a27c)

---

## See what's in your organization

The “Inventory” tab lists every skill and plugin your organization governs, including the ones users created for themselves. Skills and plugins now live on the same page, so you don't need to switch between settings.

For each item, the table shows its source, version, capabilities, audience, and how many people used it in the last 30 days.

To find an item, search by name or use the filters:

- **Source:** Your organization, Organization library, or a specific marketplace

- **Audience:** Who can use the item

- **Type:** Skills or plugins

Skills your organization manages appear under **Organization library**. You manage plugin marketplaces in the **Marketplaces** tab.

To act on an item, click the menu button at the end of its row. You can view details and files, see version history, and change default and group access.

For skills and plugins that users created, the Inventory tab shows metadata and sharing status. It doesn't show the files themselves.

## Use Anthropic-built marketplaces

Anthropic provides built-in marketplaces of plugins for different functions, such as legal and finance. A Knowledge Work marketplace is added to your organization by default.

To add an Anthropic-built marketplace:

1. Go to **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** and click the “Marketplaces” tab.

2. Click “Add,” then select “Add marketplace.”

3. Select "Browse Anthropic sources."

4. Click "Add" on each one you want to appear for everyone in your organization.

To remove the Knowledge Work marketplace if it isn't relevant to your teams:

1. Go to **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** and click the “Marketplaces” tab.

2. Find **Knowledge Work**.

3. Click the menu button in the upper right corner.

4. Select "Remove."

Anthropic-built marketplaces show readable names, like "Knowledge Work," instead of the underlying repository slug.

---

## Create your own marketplace

Beyond the Anthropic-built marketplaces, you can create your own. There are two ways to add plugins to a marketplace you create:

- **Manual upload:** Upload individual plugin ZIP files through the admin UI. Best for quick iteration, one-off tools, or teams that don't keep plugins in a Git repository.

- **Repository syncing:** Connect a private GitHub or GitLab repository and Claude syncs plugins from it. Best when multiple developers collaborate on plugins or you want version-controlled updates.

You can use both approaches in parallel. For example, run a GitHub-synced marketplace for your core plugins and a separate manual marketplace for ad-hoc tools.

### Set up a manual marketplace

1. Go to[https://claude.ai/admin-settings/plugins](https://claude.ai/admin-settings/plugins)**[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)**.

2. Click “Add,” then select “Upload a plugin.”

3. If this is your first time setting up a marketplace, "Upload to a new marketplace" is auto-selected. You'll be able to choose "Add to an existing marketplace" when uploading plugins later.

4. Enter a name for your marketplace.

5. Either drag your files in, or click the upload prompt and select your file. The file must be a valid .zip under 200 MB.

6. Repeat for each plugin you want to add.

7. Click "Upload" to add your plugins to a new marketplace.

If you upload a plugin with the same name as an existing one, it overwrites the previous version automatically. You don't need to delete the old one first.

### Set up a GitHub-synced marketplace

GitHub syncing lets you manage plugins as code in a repository. When you push changes, you can trigger a sync to update your marketplace, either manually or automatically.

**Prepare your repository**

You can connect a repo hosted on github.com or on your organization's GitHub Enterprise host. On github.com, your repository must be **private or internal**—public repos aren't allowed for organization marketplaces. To sync from GitLab, see **[Set up a GitLab-synced marketplace](#h_6be3dfbfbc)**.

GitHub-synced marketplaces support a narrower set of `source` types in `marketplace.json` than Claude Code does. Relative paths to plugin folders inside the marketplace repository (for example, `"source": "./plugins/my-plugin"`) are fully supported, and are the simplest option. The `github`, `url`, and `git-subdir` source types are also supported. The `npm`, `archive`, and `command` source types are not supported.

A plugin source can be private in three cases:

- A github.com source that shares your marketplace repository's owner, which organization sync fetches through the Claude GitHub App.

- A source on your organization's GitHub Enterprise host with your organization's GitHub Enterprise App installed on that repository.

- A url or git-subdir source on the same GitLab host as your marketplace repository. On gitlab.com, the source must also be under the same top-level group or user namespace as the marketplace repository.

Every other source is fetched without credentials, so it must be a public repository on github.com, gitlab.com, or bitbucket.org. Sources on any other host are rejected.

If your plugin code lives in a private repository that doesn't meet the criteria above, copy those plugin folders into the marketplace repository and change each plugin's source to a relative path (a git subtree or a CI step that vendors the files works well).

For details on plugin structure and formatting, see the **[plugin manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference)**.

Additional resources:

- **[Create a marketplace](https://code.claude.com/docs/en/plugins/create-marketplace)**

- **[Create a plugin](https://code.claude.com/docs/en/plugins/create)**

- **[Creating a new GitHub repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository)**

**Connect the repository**

1. Make sure both Cowork and Skills are enabled for your organization.

  1. **[Enable Cowork](https://support.claude.com/en/articles/13455879-use-cowork-on-team-and-enterprise-plans#h_71cdc52dfc)**

  2. **[Enable Skills](https://support.claude.com/en/articles/13119606-provision-and-manage-skills-for-your-organization#h_7673241237)**

2. Go to **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** and click the “Marketplaces” tab.

3. Click “Add plugins,” then select “Sync from GitHub.”

4. Enter the repository in `owner/repo` format (for example, `acme-corp/claude-plugins`).

Your personal GitHub token is verified to confirm you have access, then Cowork uses its GitHub App installation token for sync operations.

**Can't see your repo?** Make sure the Claude GitHub App is installed in that repository.

**How syncing works**

An initial sync runs automatically when you connect a repository. In the GitHub creation flow, you can also turn off "Sync automatically," which is on by default. With it on, a sync runs when a pull request is merged into the branch the marketplace follows, or when someone pushes to that branch directly.

The person turning automatic sync on or off must have admin-level access to that repository on GitHub. This is checked through their personal GitHub connection, which is separate from the Claude GitHub App installation. Without admin access, the page shows "Cannot access repository. Ensure the repository exists and the Claude GitHub App is installed," even when the App is installed correctly and manual updates work.

The Claude GitHub App's **Webhooks (Read & Write)** permission must also be approved on the installation. On installations created before this permission was introduced, GitHub shows a "Claude is requesting updated permissions" prompt that a repository or organization admin needs to approve.

Once enabled, automatic sync for a GitHub repository runs when a pull request that includes a plugin version bump is merged to the repository's default branch. Direct pushes to the default branch don't trigger a sync. You can always trigger a sync manually by clicking "Re-sync" on the marketplace.

During a sync, Cowork compares the latest commit in your repo against the last-synced commit. If nothing has changed, the sync is skipped. If there are changes, Cowork reads the manifest, validates each plugin, and replaces all plugins in the marketplace with the current state of the repo. Syncs can take up to 30 minutes depending on the number of plugins.

**Important:** If a sync fails, members keep the last synced version of each plugin. Check the failure message, fix the repo, and re-sync.

### Set up a GitLab-synced marketplace

You can sync an organization marketplace from a repository on gitlab.com or on a self-managed GitLab instance. For supported plugin source types and which sources can be private, see **Prepare your repository** above.

GitLab support is in beta and applies to plugin marketplace sync only. Claude Code on the web doesn't support GitLab repositories yet.

**Before you start**

- **Role.** You need the Owner or Primary Owner role to add a GitLab configuration.

- **Project visibility.** On gitlab.com, the marketplace project must be private or internal. On a self-managed instance, any visibility works.

- **Access token.** Create a GitLab access token for Claude to read the marketplace project and any plugin source projects on the same host. Personal, group, and project access tokens all work. The token's user needs at least the Reporter role on those projects.

  - Legacy (scoped) token: at least the `read_api` scope.

  - Fine-grained personal access token: the Project: Read, Branch: Read, and Repository: Read permissions.

  - Optional, for automatic webhook setup (step 3): the Maintainer role on the marketplace project plus the `api` scope (legacy) or the Webhook: Create and Delete permission (fine-grained). Without these, you add the webhook by hand once (step 4).

- **Self-managed instances only.**

  - The instance's hostname must resolve to a public IP address, and the instance must accept HTTPS connections from **[Anthropic's outbound IP addresses](https://platform.claude.com/docs/en/api/ip-addresses#outbound-ip-addresses)**.

  - If a private certificate authority issued its TLS certificate, have the CA certificate (PEM) ready.

  - Webhook deliveries for automatic sync come from your instance to api.anthropic.com, so the instance must be able to make outbound HTTPS requests to that host.

**Step 1: Add a GitLab configuration**

To add a GitLab configuration:

1. Go to **[Organization settings > Claude Code](https://claude.ai/admin-settings/claude-code)**.

2. Under **Self-hosted infrastructure**, find **GitLab** and click "Add configuration."

3. Enter a display name, the hostname (gitlab.com, or your instance's hostname such as gitlab.example.com), the access token, and, for a self-managed instance with a private CA, the CA certificate.

4. Click "Add configuration." Claude runs a connection test right away and shows the results in a **GitLab connection test** dialog.

5. (Optional) To check that the token can read your marketplace project, enter its path (for example, `platform/claude-plugins`) under **Project path** and click "Test sync access."

You can re-run the test at any time from the configuration's menu with **Test connection**. The hostname can't be changed later. If it changes, delete the configuration and add a new one.

**Step 2: Add the marketplace**

To add the marketplace:

1. Go to **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** and click the "Marketplaces" tab.

2. Click "Add," then select "Sync from GitLab."

3. In **GitLab repository URL**, enter the project's HTTPS URL, for example <https://gitlab.example.com/platform/claude-plugins>. Projects in nested subgroups work.

4. Leave **Sync automatically** on if you want pushes to trigger a sync (see **Step 3**).

5. Choose the **Default access** for the plugins the marketplace contains.

6. Click "Create."

Claude reads the project's default branch and validates the marketplace file before creating the marketplace, which is named after the project path.

**Step 3: Automatic sync**

With **Sync automatically** on, every push to the project's default branch triggers a sync through a webhook on the GitLab project. If your token can manage webhooks (see **Before you start**), Claude creates the webhook for you and there's nothing else to do.

You can turn **Sync automatically** on or off later from the marketplace's menu. Turning it on sets up the webhook the same way.

**Step 4: If Claude can't create the webhook**

If the token can't manage webhooks, Claude shows a **Finish webhook setup in GitLab** message on screen with a **Webhook URL** and a token. The token is shown only once, so finish this step before closing the message.

1. In your GitLab project, open **Settings > Webhooks** and add a new webhook with the URL from the message.

2. Paste the token into the field.

  1. If the message shows a **Secret token**, paste it into GitLab's Secret token field.

  2. If the message shows a **Signing token** (gitlab.com and self-managed versions 19.1 or later), select "Generate signing token" in GitLab and replace the generated value with the one from Claude.

3. Enable **Push events** and save.

4. (Optional) Use **Test > Push events** on the new webhook in GitLab and confirm it reports HTTP 200.

If you lose the token, open **Configure webhook** from the marketplace's menu, click "Remove webhook," then "Enable webhook" to get a new one. The old token will stop working.

### Choose between manual upload and repository sync

| **Scenario**                                         | **Recommended approach** |
| ---------------------------------------------------- | ------------------------ |
| Plugins are maintained in version control with CI/CD | GitHub or GitLab sync    |
| Multiple developers collaborate on plugins           | GitHub or GitLab sync    |
| You want automatic update propagation                | GitHub or GitLab sync    |
| Quick prototyping or one-off tools                   | Manual upload            |
| Plugins built by non-engineering teams               | Manual upload            |
| Environments without GitHub or GitLab access         | Manual upload            |
| Testing a plugin before adding it to a synced repo   | Manual upload            |

---

## Control plugin distribution

Once your marketplace has plugins, you control how they're distributed using installation preferences. For each plugin, you can set one of four options:

| **Preference**       | **What it does**                                                            | **What members see**                                                                                                                                                                                                               |
| -------------------- | --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Installed by default | Pre-installs the plugin for all org members                                 | The plugin appears in their list without any action. Members can turn it off if they choose.                                                                                                                                       |
| Available to install | Listed on the **Discover** tab                                              | Users see it on the **Discover** tab and can add it themselves.                                                                                                                                                                    |
| Not available        | Hidden entirely                                                             | Users can't see or add the plugin. Useful for staging or deprecating plugins.                                                                                                                                                      |
| Required             | Pre-installs the plugin for all org members without the option to remove it | The plugin appears in their list without any action, marked "This plugin is required by your organization." Users can't turn it off or remove it. It also stays on in Claude Code sessions that sync the member's account plugins. |

**Important:** Plugins set to "Installed by default" or "Required" also install in Claude Code for users who sign in with their Claude account. In Claude Code, the plugin's hooks, sub-agents, and MCP servers run on the user's computer, and a "Required" plugin can't be disabled there. Review a plugin's hooks before you set it to "Required." Learn more about **[synced plugins](https://code.claude.com/docs/en/plugins-reference#synced-plugins)** in the Claude Code docs.

### Set preferences

1. In **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)**, click the “Inventory” tab.

2. Find the plugin and click the menu button at the end of its row.

3. Click “Default access,” then select an option under **Install**.

4. Changes take effect on each member's next session or plugin refresh.

### What members experience

Members browse available plugins on the **Discover** tab in **Customize > Plugins**. Plugins you set to "Installed by default" or "Required" appear in their list automatically. Plugins you set to "Available to install" show up on **Discover** for members to add themselves.

Members can't edit organization-managed plugins, which prevents conflicting changes to shared tooling.

---

## Customize plugin access by group

Enterprise admins can override a plugin's organization-wide installation preference for specific groups. For example, you can auto-install a plugin for the Engineering group, make it available for Legal to install on their own, and hide it from everyone else.

Group-level plugin access is available on Enterprise plans. You set it on the same **Organization settings > Plugins & skills** page, which requires an Owner or a custom role that includes managing the organization's libraries.

### How group overrides work

Each plugin in your marketplace has an organization-wide installation preference (Installed by default, Available to install, Required, or Not available). By default, every group inherits that organization-wide setting.

When you set a group-level override for a plugin, it replaces the org-wide setting for members of that group. The resolution order is: group setting, then org-wide setting, then marketplace default.

### Set plugin access for a group

1. In[https://claude.ai/admin-settings/plugins](https://claude.ai/admin-settings/plugins)**[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)**[,](https://claude.ai/admin-settings/skills)click the “Inventory” tab.

2. Find the plugin you want to customize and click the menu button at the end of its row.

3. Click “Group access…”.

4. Click “Add groups” next to **Install targeting**.

5. Select the group and choose one of the installation preferences listed above.

Both manually created groups and SCIM-provisioned groups from your identity provider appear in the group picker and work the same way.

### What happens when a member is in multiple groups

If a member belongs to two or more groups with different settings for the same plugin, the **most permissive** setting applies. The order from most to least permissive is: Required > Installed by default > Available to install > Not available.

For example, if Group A sets a plugin to "Not available" and Group B sets it to "Installed by default," a member in both groups gets the plugin installed by default.

**Note:** This differs from how group spend limits resolve. Spend limits apply either the higher or lower group value depending on your **Multi-group spend limit** setting. Plugin access applies the most permissive value, because groups here are meant to enable access for teams that need a tool, not to act as a security boundary. If you need to hard-block a plugin, set its org-wide preference to "Not available" and only grant access to the groups that should have it.

### What happens when a group is deleted

If a group is removed (for example, deleted from your identity provider), the override remains in the admin UI but is flagged as orphaned. It has no effect on members (since no one belongs to a deleted group) and doesn't count toward the custom access badge. You can clear orphaned overrides from the plugin's “Group access…” settings.

### Do group settings persist across marketplace re-syncs?

Yes. Group-level overrides persist when you re-sync a GitHub- or GitLab-connected marketplace. They're only removed if the plugin itself is deleted from the marketplace.

---

## Update and remove plugins

### Manual marketplaces

To update a plugin, upload a new ZIP file with the same plugin name. The new version overwrites the existing one automatically. Plugin names are the unique identifier, so `legal` will always replace `legal`.

To remove a plugin, delete it from your marketplace in **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** under the “Inventory” tab.

### GitHub-synced marketplaces

Push your changes to the connected repository, then go to **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** and click the “Marketplaces” tab, find your marketplace, and click "Update" to trigger a sync. Each sync replaces all plugins with the current state of the repo. If an owner has enabled "Sync automatically" for the marketplace, a sync also runs whenever a pull request with a plugin version bump is merged to the repository's default branch.

For GitLab-synced marketplaces, see **[Set up a GitLab-synced marketplace](#h_6be3dfbfbc)**.

To remove a plugin, delete it from the repository and trigger a sync.

---

## Limits

| **Limit**                                           | **Value**                                             | **Notes**                                                                                                                                                                                                                                                                                           |
| --------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Max plugin ZIP size (upload)                        | 200 MB                                                | Enforced both client-side and server-side                                                                                                                                                                                                                                                           |
| Max plugins per marketplace (manual)                | 1000                                                  | Per marketplace                                                                                                                                                                                                                                                                                     |
| Max plugins per marketplace (GitHub or GitLab sync) | 1000                                                  | Per marketplace                                                                                                                                                                                                                                                                                     |
| Max plugin name length                              | 64 characters                                         | Must use lowercase words separated by hyphens                                                                                                                                                                                                                                                       |
| Sync timeout                                        | 30 minutes                                            | Per sync operation                                                                                                                                                                                                                                                                                  |
| Synced repository visibility                        | Private or internal only on github.com and gitlab.com | Hosted on github.com, GitHub Enterprise Server, gitlab.com, or a self-managed GitLab instance. GitLab hosts (including gitlab.com) require a GitLab configuration in **[Organization settings > Claude Code](https://claude.ai/admin-settings/claude-code)**.
​
Public repos aren't supported. |

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

Common causes: the file exceeds 200 MB, it isn't a valid ZIP file, or the marketplace has reached the 1000-plugin limit. Check the file size and format, and remove unused plugins if you're at capacity. If skill and plugin scanning is on, a plugin can also be rejected because it was flagged for malicious content. Review the reason, fix the issue, and upload the plugin again.

### Plugin not appearing for members

Check the plugin's installation preference in your marketplace settings. If it's set to **Not available**, members won't see it. Also confirm that Cowork and Skills are both enabled for your organization.

### Updated plugin not reflecting for members

Changes take effect on each member's next session or plugin refresh. In Claude Code, users get the change the next time they start Claude Code. If the update still isn't showing, confirm the upload succeeded by checking the plugin version in your marketplace.

### GitHub sync fails with a content error

One or more plugins in your repo is likely formatted incorrectly. Fix the formatting issue, push the update to GitHub, and trigger the sync again. For plugin structure requirements, see the **[plugin manifest reference](https://code.claude.com/docs/en/plugins/manifest-reference)**.

### Sync fails with "External plugin source type is not supported. Supported types: git-subdir, github, url" or plugins are skipped with "Repository not found on gitlab.com. Check the URL and make sure the repository is public."

One or more plugin entries in your `marketplace.json` use a `source` that points outside the connected repository (a `github`, `url`, or `git-subdir` source), and organization sync can't fetch it. A private source only works in three cases: a github.com repository shares your marketplace repository's owner, a repository on your organization's GitHub Enterprise host with your GitHub Enterprise App installed on it, or a url or git-subdir source on the same GitLab host as your marketplace repository (on gitlab.com, also under the same top-level group or user namespace).

For any other private source, move the plugin folders into the marketplace repository and change each entry's `source` to a relative path (for example, `"./plugins/my-plugin"`), then push and re-sync. Alternatively, upload the affected plugins individually via **[Organization settings > Plugins & skills](https://claude.ai/admin-settings/skills)** Click “Add,” “Upload a plugin,” then select "Add to an existing marketplace." Plugins uploaded through a member's own Customize menu are installed only for that member and aren't distributed to your organization, although members can share plugins with specific colleagues or groups if sharing is turned on.

### Can't see a GitHub repo when connecting

Make sure the Claude GitHub App is installed in that repository. Your personal GitHub token is checked first to confirm access, but the sync itself uses the GitHub App installation token.

### "Cannot access repository" when turning on "Sync automatically"

If manual updates work but turning on "Sync automatically" shows "Cannot access repository. Ensure the repository exists and the Claude GitHub App is installed," there are two likely causes:

- **You don't have admin access to the repository.** Turning on automatic sync creates a webhook, which requires admin-level access to the repo through your personal GitHub connection. Ask a repository admin to enable the toggle, or have your GitHub access upgraded.

- **The Claude GitHub App's Webhooks permission hasn't been approved.** On older installations, GitHub shows a "Claude is requesting updated permissions" prompt. A repository or organization admin needs to approve the **Webhooks (Read & Write)** permission on the installation.

### "No GitLab instance is configured for your organization yet. Add one under Claude Code settings, then come back here" when adding a marketplace

If you see this message when adding a marketplace in GitLab, make sure you’ve added the GitLab configuration first. See **Step 1: Add a GitLab configuration** under **[Set up a GitLab-synced marketplace](#h_6be3dfbfbc)**.

### "This URL isn’t on a configured GitLab instance"

Make sure the URL's hostname matches a configured GitLab hostname exactly.

### Adding a gitlab.com project fails with "Failed to create marketplace. Try again."

Check that the project's visibility is private or internal. Public gitlab.com projects can't be used as organization marketplaces.

### The connection test fails at Reach host (for example "The hostname couldn’t be resolved," "The connection was refused," or "GitLab didn’t respond in time"), or adding a marketplace on a self-managed instance fails with a generic error

Confirm the instance is reachable from the public internet over HTTPS and that Anthropic's outbound IP addresses are allowed through your firewall. "A secure connection couldn’t be established" usually means the CA certificate is missing or wrong.

### Errors that start with "Authentication to … failed" or "Access denied"

The token is expired, revoked, or missing a scope or role listed in the **Before you start** section under **[Set up a GitLab-synced marketplace](#h_6be3dfbfbc)**. Create a new token and paste it into the configuration (**Edit > Access token**).