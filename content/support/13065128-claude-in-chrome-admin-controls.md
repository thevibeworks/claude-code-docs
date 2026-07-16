# Claude in Chrome admin controls

Claude in Chrome admin controls are available for Team and Enterprise plans.

This article explains how Team and Enterprise owners can manage Claude in Chrome for their organization.

Claude in Chrome is a browser extension that allows Claude to read, click, and navigate websites on behalf of your users. As an owner, you control whether the extension is available for users to install and which sites they can access.

**Important:** Before enabling Claude in Chrome for your organization, review **[Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-for-chrome-safely)** to understand the risks of browser-based AI, including the prompt injection classifiers, the safeguards in place, and remaining risks.

## Access Claude in Chrome settings

To manage Claude in Chrome settings for your organization:

1. Sign in to Claude with your Owner or Primary Owner account.

2. Navigate to **[Organization settings > Claude in Chrome](http://claude.ai/admin-settings/browser-extension)**.

## Enable or disable the extension

Use the toggle to enable or disable Claude in Chrome for your entire organization.

- **Team plans:** The extension is enabled by default. Disable it if you prefer users not to have access.

- **Enterprise plans:** The extension is disabled by default. Enable it when you're ready for users to access the feature.

Claude in Chrome and Claude Cowork are managed separately. Enabling Claude in Chrome for your organization lets users use the extension. Whether Claude can use it within Cowork is a separate capability setting, and users' browsers still need the extension deployed or installed. For Cowork admin settings, see **[Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)**.

**Note:** When you enable the extension for an Enterprise organization, users are not automatically notified. You may want to communicate availability through your internal channels.

## Configure site access

Use allowlists and blocklists to control which websites Claude can access when users are working with the extension.

**Allowlist:** Specify which sites Claude is permitted to access by adding them to the allowlist. We recommend starting with a restrictive allowlist, especially during initial rollout.

**Blocklist:** Specify sites Claude should never access, regardless of other settings, by adding them to the blocklist. This adds an extra layer of protection beyond **[Claude's default blocked categories](https://support.claude.com/en/articles/12902428-using-claude-for-chrome-safely#h_34f8d5ca87)**.

**Recommendation:** Start with a more restrictive allowlist for the security of your organization's data, then expand access over time as you become comfortable with the extension's behavior.

## Control password manager access

1Password for Claude lets macOS users complete tasks that require signing in, with 1Password filling the credential directly on the page so Claude never sees the password or one-time code. The integration is off by default for your organization.

Once enabled, eligible users will see the integration surfaced in Claude Desktop. Users also need the 1Password desktop app, the 1Password browser extension, Claude Desktop, and Claude in Chrome installed on a Mac. For setup details and requirements, see **[Get started with 1Password for Claude](https://support.claude.com/en/articles/15936181)**.

## Manage user access on Claude Desktop

Users with both Claude in Chrome and Claude Desktop installed will now have the option to start a task on the desktop app and let it handle work in the browser without switching windows.

If you want to disable this for members of your organization, you can toggle the extension off entirely, or edit your Enterprise configuration.

**Disable the Chrome extension in organization settings:**

1. Sign in to Claude with your Owner account.

2. Navigate to **[Organization settings > Claude in Chrome](http://claude.ai/admin-settings/browser-extension)**.

3. Toggle the extension off.

Alternatively, disable `isLocalDevMcpEnabled` in **[your Enterprise configuration](https://support.claude.com/en/articles/12622667-enterprise-configuration)**.

## Deployment options

Once enabled, users can access Claude in Chrome in two ways:

- **Self-service:** Users install the extension themselves from the **[Chrome Web Store](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn)**.

- **Managed deployment:** Use your existing Chrome management tools (Google Workspace admin console or MDM) to deploy the extension to specific users or groups.

Most Enterprise organizations already have Chrome extension management in place. You can use these existing controls to limit which employees can install the extension during a pilot phase.

## Run a pilot

To test Claude in Chrome with a subset of users before broader rollout:

1. Enable the extension at the organization level.

2. Configure a restrictive allowlist limiting Claude to specific, trusted sites.

3. Use your IT controls to limit which employees can install the extension.

4. Share **[Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-for-chrome-safely)** with pilot users.

5. Gather feedback and expand access over time.

## How Claude in Chrome fits your existing controls

- **Role-based permissions:** Claude in Chrome has its own permission, separate from Claude Cowork. Two settings control Claude in Chrome: an organization-level toggle, and a per-role capability that admins can grant or withhold. That per-role capability applies to Enterprise organizations using custom roles. Claude in Chrome doesn't inherit a user's Cowork access.

- **Network controls:** Claude in Chrome sends its chat traffic through your existing Claude endpoints (`claude.ai`, `api.anthropic.com`, `platform.claude.com`), so any controls you've set on those apply here too. It also connects to the same bridge endpoint Claude Desktop uses (`wss://bridge.claudeusercontent.com`) and to standard telemetry services. In restrictive network environments, allow these connections. To limit which organization the extension can be used with, deploy the `forceLoginOrgUUID` Chrome enterprise policy.

- **Zero data retention (ZDR):** Not supported for Claude in Chrome, the same as Cowork.

## Educate your users

We recommend sharing these resources with users before they start using Claude in Chrome:

- **[Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-getting-started-with-claude-for-chrome)**: Installation and core capabilities

- **[Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-for-chrome-safely)**: Risks and best practices

- **[Claude in Chrome permissions guide](https://support.claude.com/en/articles/12902446-claude-for-chrome-permissions-guide)**: How users control what Claude can access