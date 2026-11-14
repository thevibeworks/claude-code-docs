# Get started with centralized management

Centralized management gives your parent organization its own admin console at **[admin.claude.com](https://admin.claude.com)**, where you manage company-wide settings such as single sign-on (SSO), directory sync, verified domains, and groups in one place. This article explains what changes when you enroll, how to enroll your parent organization, and how to use each part of the console.

Centralized management is available in beta on Enterprise plans.

## How parent and child organizations work

Centralized management uses two terms throughout:

- **Parent organization:** Represents your company and your commercial relationship with Anthropic. Company-wide settings live here, including identity providers, domain verification, and, where applicable, your Business Associate Agreement (BAA).

- **Child organization:** An individual Claude organization under the parent, such as a Claude Enterprise organization, a Team plan, or a Claude Platform organization bought directly from Anthropic. Each one has its own users, admins, and settings.

Enrolling doesn't merge your child organizations. Each one stays a separate organization with a hard data boundary, and keeps its own users, roles, and projects.

## Parent organization roles

Your parent organization gets two new roles to run the console. These roles are separate from child organization permissions.

| **Role**                        | **What they can do**                                                                                                                        |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Parent organization owner (new) | Everything at the parent level, including choosing who holds the owner and admin roles. Every parent organization needs at least one owner. |
| Parent organization admin (new) | Everything at the parent level except choosing owners and admins.                                                                           |
| Child organization admin        | Everything inside their own organization. They can't see or change parent-level settings, such as SSO enforcement.                          |

A parent role doesn't add someone to a child organization or let them sign in to it. A parent owner or admin who needs to work in a child organization needs to be added like any other user. Parent owners and admins can audit configuration and view compliance data across child organizations through the API. Learn more in the API keys section below.

## Controls that move to the parent organization

These controls already applied at the parent level, but you managed them from child organization admin settings. After you enroll, parent owners and admins manage them once for every organization, in the parent organization console.

| **Control**                        | **Now managed in**               | **What it does**                                                                                                                                  |
| ---------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| SSO and Require SSO                | Identity providers and Domains   | Sign-in for your verified domains, for Claude and Console. Require SSO is set per domain.                                                         |
| Directory sync (SCIM)              | Identity providers               | Provisions users and groups from your identity provider.                                                                                          |
| Domain verification                | Domains                          | Verifies the email domains your users sign in with.                                                                                               |
| Connector domain restriction       | Domains                          | Limits connectors on your domains to accounts in your enterprise.                                                                                 |
| Restrict organization creation     | Organizations (Security section) | Blocks new organizations, including personal accounts, on your verified domains.                                                                  |
| Compliance API keys                | API keys                         | See, disable, and delete parent-level keys created from any child organization.                                                                   |
| Groups                             | Groups                           | Directory groups synced from your identity provider, plus groups created by hand.                                                                 |
| Invite organizations to the parent | Organizations                    | Self-serve for Claude Platform organizations and Team plans on a verified domain. For Claude Enterprise organizations, contact your account team. |

Child organization admins keep everything inside their own organization: users, roles, organization settings, and organization-level security controls such as IP allowlisting and session duration.

## New parent-level controls

Centralized management also adds controls that didn't exist before:

| **Control**                      | **Where**                      | **What it does**                                                                                                                 |
| -------------------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- |
| Organizations overview           | Organizations                  | Shows every child organization in one place, with its type and ID                                                                |
| Parent organization roles        | Admin roles                    | Assigns the parent owners and admins who manage company-wide settings                                                            |
| Multiple identity providers      | Identity providers             | Connects more than one SSO and SCIM configuration under one parent, with each domain routed to one or more of them               |
| Split domains                    | Domains and Identity providers | Routes one domain to more than one identity provider for sign-in, and lets you choose who sees each identity provider at sign-in |
| Parent-level Compliance API keys | API keys                       | Creates parent-level keys from admin.claude.com. Child organizations can still create keys for their own organization            |

Learn more about **[setting up multiple identity providers and split domains](https://support.claude.com/en/articles/18246779)**.

Group availability, which will let you choose which child organizations can see and use each group, isn’t available yet. Until it is, every Enterprise child organization admin can see every group under the parent.

## Current limitations

These limits apply during the beta:

- **Child organization creation:** New child organizations go through your account team. There’s no self-serve option.

- **Billing:** Invoicing doesn't change when you enroll.

- **Cloud marketplace organizations:** Claude Platform organizations bought through the AWS or Azure marketplace can't join a parent organization.

Two kinds of parent organization can't enroll:

- Parent organizations with a HIPAA-enabled child organization

- Parent organizations whose only child organizations are Team plans

## Enroll your parent organization

An eligible admin of any child organization can start enrollment at **admin.claude.com**. Eligible admins are the Primary Owner of a Claude Enterprise or Team organization, and the Admins of a Console organization. Enrollment is a short approval flow in which every child organization signs off on who the parent organization admins will be. Everyone proposed who’s still eligible when enrollment completes becomes a parent organization owner. Owners can add admins afterward on the **Admin roles** page.

**Warning:** Enrollment can't be undone, and it can complete as soon as someone starts setup.

### Before you start

If your network uses tenant restrictions, add the parent organization ID to your list of allowed organization IDs (the anthropic-allowed-org-ids header) before anyone starts setup, and keep the IDs already there. Without the parent ID, parent owners and admins on that network can't manage the parent console.

Copy the parent organization ID from **Organization settings > Organization** in Claude, or from **Settings > Organization** in Console. The child organizations you administer also need to be on the list, or setup may fail.

### Complete setup

1. Go to **[admin.claude.com](https://admin.claude.com)** and start setup. You see the child organizations you administer.

2. Propose parent organization admins from those organizations. Search by name, email, or organization to find people. Starting setup counts as approval for the organizations you administer.

3. If other child organizations remain, wait for their eligible admins to review the proposal. They can nominate admins from their own organizations, and approve. You can remind anyone who hasn't approved yet.

4. When setup finishes, select "Done". The console opens on the **Organizations** page.

If you administer every organization under the parent, your parent organization is enrolled immediately. Otherwise, the last approval enrolls it. SSO, SCIM, verified domains, and security settings move to the parent, and each child organization keeps its own users, roles, and projects.

Changing the proposed admins asks every child organization to approve again. If an organization still hasn't approved after seven days, an eligible admin of another organization may be able to approve on its behalf.

## Manage your parent organization

The console has a page for each area of your parent organization. Parent owners and admins can use all of them.

### General

Change the parent organization's name here. The name appears wherever the parent is named, including the organization switcher. You can also find the parent organization ID on this page.

### Organizations

This page lists every child organization under the parent, with its type (for example Claude Enterprise, Claude Team, or Claude Platform) and ID.

To bring an existing organization under your parent, select "Invite" under **Merge organizations**. Invites are self-serve for Claude Platform organizations and Team plans on one of your verified domains. To bring a Claude Enterprise organization under the parent, contact your account team.

### Domains

This page holds the verified email domains for the parent, which every child organization shares. Each domain signs in through the identity provider you choose for it, or through several with split domains. A domain with no identity provider has no SSO sign-in.

To add and route a domain:

1. Select "Add domain" and verify the domain. A verified domain can belong to only one parent organization.

2. Select the pencil icon in the **SSO sign-in at** column.

3. Select each identity provider the domain should sign in through, and clear any it should stop using.

4. Select "Save.” The change applies to sign-in as soon as you save.

Turn on **Restrict verified-domain connectors to your enterprise** to stop Claude accounts outside your enterprise from connecting supported connectors, such as Google Drive, Gmail, Microsoft 365, and Slack, with an email on your domains.

### Identity providers

This page lists each SSO and SCIM configuration connected to the parent, with its sign-in status, directory sync status, and domains. Open one to manage it:

- **Single sign-on:** Select "Manage SSO" to open the setup portal and review or change the SAML or OIDC connection. Below that, choose who can sign in with this identity provider and whether it's shown on the sign-in page.

- **Directory sync:** Select "Set up directory sync" to open the setup portal and connect SCIM. Once it's connected, select "Resync now" to pull the latest changes. The page lists the groups syncing from your directory.

- **Domains:** Shows the verified domains that sign in here. Turn on **Require SSO for Claude** and **Require SSO for Console** to force SSO for those users. These settings apply per domain, and you can also change them on the **Domains** page.

To add, route, or remove an identity provider, learn more about **[setting up multiple identity providers and split domains](https://support.claude.com/en/articles/18246779)**.

### API keys

This page shows parent-level keys, with each key's scopes, organization, creator, and creation date. Keys belong to the parent organization and stay active after the person who created them is removed from it. Keys scoped to a single child organization don't appear here. They stay in that organization's admin settings.

The **Compliance API** switch above the keys turns the Compliance API on or off for every organization under the parent. While it's off, existing API keys can't use compliance scopes.

**Create a key**

Creating keys requires at least one Claude Enterprise organization under the parent. Each key you create here works across every organization under the parent.

1. Select "Create key.”

2. Name the key and select its scopes. Compliance scopes, such as read:compliance_activities, give the key access to the Compliance API. If you don't see them, turn on the **Compliance API** switch first, which also turns on compliance event logging for every organization under the parent. Group scopes (read:rbac_groups and write:rbac_groups) let the key read or manage groups and their members.

3. Select "Create.” A key with delete:compliance_user_data can permanently delete data in any organization under the parent, so you confirm it first.

4. Select "Copy key" and store the key somewhere safe. You won't be able to view it again.

**Manage keys**

Select a key's actions menu to disable, re-enable, or delete it. A key you create here shows the parent organization's name in the **Organization** column. A key created from a child organization that works across every organization shows that organization's name with a warning icon. Those keys keep working, and you manage them here too.

**Keys in child organizations**

- Child organization admins can still create keys scoped to their own organization.

- They can't create a key that works across every organization, or turn one back on once it's disabled.

- In Claude Enterprise organizations, primary owners can also create keys with read:org_audit or group scopes for their own organization. These keys still reach all of the parent's groups.

- Keys scoped to one organization can't read sign-ins or other parent-level events, such as changes to Require SSO. To read those, use a key that works across every organization.

### Security

On the **Organizations** page, under **Security**, turn on **Restrict organization creation** to stop anyone on your verified domains from creating a new organization, including a personal account. The **Security** page in the side menu lists each organization's HIPAA status.

Parent owners and admins also start a domain claim here, instead of from a child organization's settings. You choose one child organization for accounts to migrate to, and the claim covers every Free, Pro, Max, and Ultra account on the domains verified at that point. Each person chooses **Bring what you can** or **Start fresh**. Their personal account closes either way, and not everything can move (see **[What moves when you migrate](https://support.claude.com/en/articles/9267400-move-your-personal-claude-account-to-a-team-or-enterprise-organization#h_4e63ef6e87)**). They need a seat in that organization to bring their data. Learn more about **[responding to an enterprise domain claim](https://support.claude.com/en/articles/14625626-respond-to-an-enterprise-domain-claim-on-your-claude-account)**.

Session duration stays with each child organization during the beta, and each child organization keeps its own IP allowlist.

Tenant restrictions already apply to the parent console. If your network uses them, keep the parent organization ID from the **General** page on your list of allowed organization IDs, along with your child organization IDs, because the parent's ID doesn't cover them.

### Groups

Groups are collections of users who share the same roles. They live at the parent, so one group can be given roles in any child organization. Child organization admins assign those roles inside their own organization.

- The **Groups** tab shows every group under the parent, with its member count. You can filter by source and search by name.

- Groups synced from your directory carry a SCIM badge. Open one to see its members. Its name and membership come from your identity provider.

- Select "Add group" to create a group by hand. Open it to rename it, or to add and remove members by name or email.

- Delete a group from its actions menu.

**Note:** Until group availability is available, every Enterprise child organization admin can see every group under the parent.

### Admin roles

This page lists the people who administer the parent organization. Select "Add admin" to give someone a parent role.