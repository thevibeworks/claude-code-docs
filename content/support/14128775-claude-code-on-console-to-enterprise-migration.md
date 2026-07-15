# Claude Code on Console to Enterprise migration

## Overview

This guide is built for teams migrating from Console-based Claude Code access to Claude Enterprise. Note that individual users don’t need to migrate session history for CLI sessions since these are stored locally. You only need to provision Claude Enterprise accounts for each user, and then users should switch their login method from Console to Claude Enterprise.

## Why migrate to Claude Enterprise

Claude Code on the Console API is a fast way to get developers started, but it leaves governance up to each individual machine. Claude Enterprise puts the same Claude Code your developers already use behind the controls that security, IT, and finance teams need to run it at scale. You get centralized identity and access through your existing IdP, server-managed settings that enforce tool, file, and MCP policies on every client without MDM, and granular spend caps that cascade from the org down to individual users.

Claude Enterprise adds rich analytics and audit logs (including contribution metrics like PRs and lines committed), custom data retention controls, and additional product surfaces—Claude Code on the web, mobile, and Slack (Claude Tag), plus Code Review—that aren't available on Console. And because Claude Enterprise is available via AWS Marketplace, procurement can run through the channel you already have.

---

## Claude Enterprise compared to Console

| **Capability**                           | **Claude Console/API**                                                                                                                                                 | **Claude Enterprise**                                                                                                                                                                                                                                                                                                                                        |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Claude Code on the web and mobile app    | ❌                                                                                                                                                                      | ✅                                                                                                                                                                                                                                                                                                                                                            |
| Claude Tag                               | ❌                                                                                                                                                                      | ✅                                                                                                                                                                                                                                                                                                                                                            |
| Code Review                              | ❌                                                                                                                                                                      | ✅                                                                                                                                                                                                                                                                                                                                                            |
| Enforce which tools Claude Code can use  | ❌ No native UI<br>*\*Settings can be pushed to developer machines via MDM (Jamf, Intune) or config management (Ansible, Puppet, etc.)*                                 | ✅ Native UI to set managed-settings.json allow/deny rules                                                                                                                                                                                                                                                                                                    |
| Block specific bash commands             | ❌ No native UI\*                                                                                                                                                       | ✅ Bash(curl:\*), Bash(sudo:\*), etc.                                                                                                                                                                                                                                                                                                                         |
| Prevent access to sensitive files        | ❌ No native UI\*                                                                                                                                                       | ✅ Read(.env), Read(./secrets/\*\*)                                                                                                                                                                                                                                                                                                                           |
| Control which MCP servers are allowed    | ❌ No native UI\*                                                                                                                                                       | ✅ allowedMcpServers / deniedMcpServers                                                                                                                                                                                                                                                                                                                       |
| Deploy pre-approved MCP servers org-wide | ❌ No native UI\*                                                                                                                                                       | ✅ managed-mcp.json                                                                                                                                                                                                                                                                                                                                           |
| Force sandbox mode                       | ❌ No native UI\*                                                                                                                                                       | ✅ sandbox.enabled                                                                                                                                                                                                                                                                                                                                            |
| Disable --dangerously-skip-permissions   | ❌ No native UI\*                                                                                                                                                       | ✅ permissions.disableBypassPermissionsMode: disable                                                                                                                                                                                                                                                                                                          |
| Disable auto mode                        | ❌ No native UI\*                                                                                                                                                       | ✅ disableAutoMode: disable                                                                                                                                                                                                                                                                                                                                   |
| Custom roles (RBAC)                      | ❌                                                                                                                                                                      | ✅ Scope feature access by group and delegate specific admin areas like billing, user management, and identity without granting the Owner role. **[Manage custom roles on Enterprise plans](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans)**                                                                        |
| Model governance                         | ❌ No native UI\*                                                                                                                                                       | ✅ Set an organization default model for chat and Cowork (beta) from the admin console, and restrict Claude Code model selection with `availableModels` in managed settings. **[Set a default model for your organization](https://support.claude.com/en/articles/15330088-set-a-default-model-for-your-organization)**                                       |
| Audit logs                               | ❌ No audit log support<br>🟡 Claude Code does have support for **[OpenTelemetry](https://code.claude.com/docs/en/monitoring-usage)**                                    | 🟡 Audit logs and the **[Compliance API](https://support.claude.com/en/articles/13015708-access-the-compliance-api)**, which includes audit log events. Transcripts of local CLI sessions stay on the developer's machine and aren't available via the Compliance API.                                                                                        |
| Usage analytics                          | ✅ Lines of code written, acceptance rate, daily active users, daily spend.<br>**[Docs](https://code.claude.com/docs/en/analytics#access-analytics-for-api-customers)** | ✅ Lines of code written, acceptance rate, daily active users, and month-to-date spend per member in **Organization settings** → **Usage.**<br>**[Docs](https://code.claude.com/docs/en/analytics#access-analytics-for-teams-and-enterprise)**                                                                                                                |
| Programmatic usage and cost reporting    | ✅ **[Claude Code Analytics API](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api)**                                                         | ✅ The **[Claude Enterprise Analytics API](https://platform.claude.com/docs/en/manage-claude/analytics-api)** returns per-user engagement and Claude Code metrics (commits, pull requests, lines of code) plus usage and cost endpoints. The **[Admin API](https://platform.claude.com/docs/en/manage-claude/admin-api)** covers programmatic org management. |
| Contribution metrics                     | ✅ Via the Claude Code Analytics API                                                                                                                                    | ✅ PRs created and lines of code committed with Claude Code assistance.                                                                                                                                                                                                                                                                                       |
| Granular spend controls                  | ✅ Org and workspace limits, plus per-developer limits in Claude Code workspaces                                                                                        | ✅ Org → Group → Individual, integrated with RBAC groups                                                                                                                                                                                                                                                                                                      |

**Docs: [Roles and permissions](https://support.claude.com/en/articles/9267276-roles-and-permissions)**, **[Purchasing and managing seats on Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans), [How am I billed for my Enterprise plan?](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)**, **[Using Claude Code with your Enterprise plan](https://support.claude.com/en/articles/11845131-using-claude-code-with-your-team-or-enterprise-plan)**

---

## SCIM provisioning

Here’s what your identity team needs to do:

1. **Update IdP group mappings** — Create or repurpose IdP groups to map users to the Claude Enterprise organization. Enable group mappings to assign seats automatically.

2. **Ensure sufficient seats are purchased** — Before triggering a SCIM sync, verify the Claude Enterprise org has enough seats available. Users without available seats will be set to “Unassigned” status.

3. **Confirm Claude Code access is enabled** — Confirm Claude Code is enabled for the Enterprise organization in admin settings, and — if you scope features with custom roles or groups — that your developer groups are granted Claude Code access.

4. **Trigger a sync** — Navigate to **[Organization settings → Organization and access](https://claude.ai/admin-settings/organization)**, find **Directory sync (SCIM)**, and click “Sync.” Note that this may be slow as this can trigger a big sync.

5. **Verify seat assignments** — After sync, check **[Organization settings → Organization and access](https://claude.ai/admin-settings/organization)** to confirm users landed on the correct seat type.

6. **Optional: Adjust Console org mappings** — If some users should retain Console API access, keep their group mapped to the Console organization. Users can belong to both orgs simultaneously.

**Note:** Microsoft Entra SCIM changes sync every ~40 minutes. Use the “Sync” button to trigger on-demand after group changes.

If your Enterprise organization's SSO is configured as login-only, signing in does not create accounts — users must be invited manually. Enable JIT or SCIM provisioning before directing developers to log in. See **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning).**

---

## Spend limits

Claude Enterprise plans offer a hierarchical spend control system. Limits cascade—a user can never exceed the org limits.

| **Level**         | **Scope**             | **Who sets it**       | **What it controls**                             |
| ----------------- | --------------------- | --------------------- | ------------------------------------------------ |
| 1. Organization   | Entire Enterprise org | Primary Owner / Owner | Maximum monthly spend across all seats and usage |
| 2. Group controls | Groups with RBAC      | Primary Owner / Owner | Spend limit for a group using RBAC               |
| 3. Individual     | Specific user         | Primary Owner / Owner | Spend limit for a single team member             |

### How to set and edit spend limits

1. Sign in as an Owner or Primary Owner.

2. Navigate to **[Organization settings → Usage](https://claude.ai/admin-settings/usage)**.

3. Set the Organization level limit — this is the global ceiling for all monthly spend.

4. Set Group level limits — under the "By group" tab. See **[Manage groups and group spend limits on Enterprise plans](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)**.

5. Set Individual level limits — find specific users in the **Spending defaults** section under the “By member” tab.

Owners can set limits to "unlimited," but all consumption is still billed. If a user on a consumption seat hits their limit, they cannot use Claude or Claude Code until the next billing period or until an admin increases their limit.

**Docs: [Configuring spend limits](https://support.claude.com/en/articles/11526368-how-am-i-billed-for-my-enterprise-plan)**, **[Manage groups and group spend limits on Enterprise plans](https://support.claude.com/en/articles/13799932-manage-groups-and-group-spend-limits-on-enterprise-plans)**

---

## Issuing new seats and re-authentication

### Adding seats

1. Log in as Primary Owner or Owner.

2. Go to **[Organization settings → Billing](https://claude.ai/admin-settings/billing)**.

3. Click the pencil icon under Seats.

4. Enter the new seat counts.

5. Review and click “Upgrade” to confirm. New seats are prorated.

### Assigning users to seats

1. Go to **[Organization settings → Members](https://claude.ai/admin-settings/members)**.

2. Click “Add member” (or “Bulk add” for multiple).

3. Enter the user’s @ email address.

4. Set role (User, Admin, Owner) and send invite.

For SCIM-provisioned users, seat assignment happens automatically based on group mappings. Users default to the highest-available seat tier if no group mapping is configured.

### Re-authentication for Claude Code users

Developers currently authenticated against the Console org will need to re-authenticate against the Claude Enterprise organization:

1. Remove any leftover Console credentials before logging in. Check for `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` environment variables in shell profiles, dotfiles, and CI configs, and remove any `apiKeyHelper` setting. Also check for `CLAUDE_CODE_OAUTH_TOKEN`, `ANTHROPIC_BASE_URL`, and the `CLAUDE_CODE_USE_BEDROCK / _VERTEX / _FOUNDRY` flags — these also override or bypass `/login`. Credentials can also hide in the env block of Claude Code's own settings files (~/.claude/settings.json, and the .claude/settings*.json files in repos). If these remain, they silently take precedence over the new login: `/login` will appear to succeed, but usage continues billing to the old Console organization.

2. In the terminal, run `claude` and then run `/login` to switch authentication method.

3. Select “Claude account with subscription” as the login method.

4. Choose the Claude Enterprise organization (not the Console org or a personal account).

5. Authorize, return to the terminal, and run `/status` to confirm Claude Code shows your Enterprise organization.

**CI and automation**

Pipelines and scripts don't use `/login`. Either keep a Console org (and its API keys) for automation and migrate only interactive developer seats, or switch CI to an Enterprise credential: run `claude setup-token` while signed in to the Enterprise organization and set the printed token as `CLAUDE_CODE_OAUTH_TOKEN` in your CI environment. Don't remove CI credentials until one of these is in place.

**Tip for IT:** Deploy managed settings with `forceLoginOrgUUID` set to your Enterprise organization UUID as a standard part of every migration. Deliver the pin as an endpoint-managed file or MDM policy — server-managed settings only arrive after a user signs in, so they can't catch a wrong first login. If you also use server-managed settings, set `forceLoginOrgUUID` there too: the two channels don't merge. This blocks login to any other organization, and it turns the leftover-credential failure mode above from silent misbilling into a loud one: Claude Code refuses to start and tells the user that a leftover credential (`ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, or `apiKeyHelper`) must be removed.

**After validating the migration**

Remove migrated developers from the Console org (or rotate their keys). Removal revokes their Console login tokens and disables their Claude Code workspace key, stopping further Console billing from interactive use. API keys they created in other Console workspaces are not disabled by removal — review and disable those separately. Don't remove members until you've confirmed Enterprise access works; there is no automated rollback.

**Docs: [Purchasing and managing seats on Enterprise plans](https://support.claude.com/en/articles/13393991-purchasing-and-managing-seats-on-enterprise-plans)**

---

## Improvements in reporting

Moving from Console API to Claude Enterprise unlocks richer analytics for Claude Code usage:

| **Metric**                                          | **Console API**                                       | **Claude Enterprise**                                                                                                                                                                                                                           |
| --------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Token consumption                                   | ✅                                                     | ✅                                                                                                                                                                                                                                               |
| Lines of code accepted                              | ✅                                                     | ✅                                                                                                                                                                                                                                               |
| Suggestion acceptance rate                          | ✅                                                     | ✅                                                                                                                                                                                                                                               |
| PRs created with Claude Code assistance             | ✅ Via the Claude Code Analytics API                   | ✅                                                                                                                                                                                                                                               |
| Lines of code committed with Claude Code assistance | ✅ Via the Claude Code Analytics API                   | ✅                                                                                                                                                                                                                                               |
| Spend limit notifications                           | ✅ Notify-at-limit emails with configurable recipients | ✅<br>Threshold alerts                                                                                                                                                                                                                           |
| Month-to-date spend per member                      | ❌                                                     | ✅<br>Admin settings → Usage                                                                                                                                                                                                                     |
| Compliance audit trail                              | ❌                                                     | ✅ The **[Compliance API](https://support.claude.com/en/articles/13015708-access-the-compliance-api)** includes audit log events. Transcripts of local CLI sessions stay on the developer's machine and aren't available via the Compliance API. |

All reporting is accessible from **[Analytics](https://claude.ai/analytics/activity)** in the Claude admin panel. For programmatic access, the **[Claude Enterprise Analytics API](https://platform.claude.com/docs/en/manage-claude/analytics-api)** returns per-user engagement metrics, Claude Code activity (commits, pull requests, lines of code), and usage and cost data. Analytics do not migrate: the Enterprise organization starts with fresh reporting history, and its Analytics/Admin API requires a new API key created in the Enterprise organization — Console keys don't carry over. Export any Console analytics you need for historical dashboards before cutover. Traffic that remains on Console API keys (for example CI) continues to appear only in Console reporting.

**Docs: [Claude Code Usage Analytics](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)**

---

## Managed policy settings — deep dive

This is the most significant upgrade for the security and IT teams. **[Server-managed settings](https://code.claude.com/docs/en/server-managed-settings)** allow centralized, enforceable control over what Claude Code can and cannot do across every developer’s machine. There are two ways to deliver them, and you don't need MDM to use the first one.

### How it works

Claude Code reads configuration from a hierarchy of settings sources. The managed-settings.json file sits at the top and cannot be overridden by user or project settings:

| **Priority** | **Source**                                            | **Scope**                | **Who controls it**                                                                                                 |
| ------------ | ----------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------- |
| 1 (Highest)  | Managed settings (server-managed or endpoint-managed) | Enterprise-wide          | Owner / Primary Owner (when pushed from the claude.ai admin console) or your IT/MDM team (when deployed as a file). |
| 2            | Command-line arguments                                | Session                  | Developer                                                                                                           |
| 3            | .claude/settings.local.json                           | Project (personal)       | Developer                                                                                                           |
| 4            | .claude/settings.json                                 | Project (shared, in Git) | Team                                                                                                                |
| 5 (Lowest)   | ~/.claude/settings.json                               | User (global)            | Developer                                                                                                           |

### Two ways to deliver managed settings

**Server-managed settings (no MDM required):** An Owner or Primary Owner defines settings in **Organization settings** → **Claude Code** → **Managed settings** in the admin console. Every Claude Code client signed in to the organization fetches them automatically at startup and polls hourly for updates. This is the right choice for organizations without device management infrastructure or with users on unmanaged devices. Learn more about **[server-managed settings](https://code.claude.com/docs/en/server-managed-settings)**.

**Endpoint-managed settings:** IT deploys settings directly to devices, either through native OS policies (macOS managed preferences or the Windows registry, via Jamf, Intune, Group Policy, etc.) or as a managed-settings.json file pushed to the system paths below. Protect the file with OS-level permissions so end users cannot modify it. On enrolled devices, this provides stronger guarantees than server-managed delivery because the OS prevents user tampering.

**Note:** Both channels occupy the same highest-priority tier and use the same JSON format, but they don't merge. The first source that delivers a non-empty configuration wins: server-managed settings are checked first, and if they deliver any keys at all, endpoint-managed settings are ignored entirely. Run /status to see which managed source is active.

### File locations (endpoint-managed)

| **OS**  | **Path**                                                      |
| ------- | ------------------------------------------------------------- |
| macOS   | /Library/Application Support/ClaudeCode/managed-settings.json |
| Linux   | /etc/claude-code/managed-settings.json                        |
| Windows | C:\Program Files\ClaudeCode\managed-settings.json             |

### Key settings reference

These are the settings most relevant to a Console-to-Enterprise migration. Claude Code supports many more: for the complete, current list, see **[Claude Code settings](https://code.claude.com/docs/en/settings)**.

| **Setting**                                | **Purpose**                                                                                                                                                                                  | **Example**                    |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| `permissions.deny`                         | Block specific tools/commands org-wide                                                                                                                                                       | Bash(curl:\*), Read(.env)      |
| `permissions.allow`                        | Explicitly allow trusted commands                                                                                                                                                            | Bash(npm run test:\*)          |
| `permissions.ask`                          | Require user approval each time                                                                                                                                                              | Bash(rm:\*)                    |
| `permissions.disableBypassPermissionsMode` | Prevent --dangerously-skip-permissions                                                                                                                                                       | "disable"                      |
| `forceLoginOrgUUID`                        | Restrict login to specific Enterprise org(s). Accepts one org UUID or an array; login to any other org is blocked. A single UUID also auto-selects that org at login.                        | "298e7cb2…"                    |
| `forceLoginMethod`                         | Force the login method (claudeai, console, or gateway). Recommended alongside `forceLoginOrgUUID` so users skip the account-type chooser, but not required for the org restriction to apply. | "claudeai"                     |
| `allowedMcpServers`                        | Allow only approved MCP servers, matched by name, command, or URL pattern                                                                                                                    | [{"serverName": "github"}]     |
| `deniedMcpServers`                         | Blacklist specific MCP servers                                                                                                                                                               | [{"serverName": "filesystem"}] |
| `allowManagedPermissionRulesOnly`          | Only permission rules from managed settings apply; users and projects can't add their own                                                                                                    | true                           |
| `allowManagedMcpServersOnly`               | Only the managed MCP allowlist applies; deny lists still merge from all sources                                                                                                              | true                           |
| `allowManagedHooksOnly`                    | Only managed and admin-approved hooks run                                                                                                                                                    | true                           |
| `enforceAvailableModels`                   | Extends the `availableModels` allowlist to the Default model option                                                                                                                          | true                           |
| `sandbox.enabled`                          | Force sandbox mode                                                                                                                                                                           | true                           |
| `sandbox.allowUnsandboxedCommands`         | Block unsandboxed execution                                                                                                                                                                  | false                          |
| `cleanupPeriodDays`                        | Retention period for local session data (transcripts and other application files). Default: 30 days                                                                                          | 7                              |
| `companyAnnouncements`                     | Display messages to all Claude Code users                                                                                                                                                    | Array of strings               |

**Deployment:** Use your MDM tool (Intune, Jamf, SCCM, Puppet, etc.) to push managed-settings.json to all developer machines. Protect the file with OS-level permissions so end users cannot modify it.

**Docs: [Claude Code settings](https://code.claude.com/docs/en/settings)**, **[Managed settings](https://code.claude.com/docs/en/permissions#managed-settings)**, **[MCP installation scopes](https://code.claude.com/docs/en/mcp#managed-mcp-configuration)**