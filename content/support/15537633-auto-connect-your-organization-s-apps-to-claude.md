# Auto-connect your organization’s apps to Claude

This article explains how Enterprise-managed auth works and how admins can authorize connectors for their organization, either through their identity provider or directly with Claude-issued auth With Enterprise-managed auth, you authorize a connector once for your entire organization, and your team inherits access automatically on first login.

Enterprise-managed auth is available for Team and Enterprise plans on Claude. IdP-managed auth is generally available, and Claude-issued auth is in beta.

## What is Enterprise-managed auth?

Enterprise-managed auth is an authorization and authentication model for connectors in Claude. Instead of having every person authenticate each connector individually, admins provision connector access centrally.

Each connector uses one of two identity sources:

- **IdP-managed:** Your identity provider relies on single sign-on (SSO) being enabled on Claude and the connector. With that in place, the IdP signs the user into the connector.

- **Claude-issued (beta):** Claude can indicate to the connector which user signed into Claude, and use that information to the connector, under an issuer URL that’s unique to your organization. You don’t need an identity provider or SSO.

Once you enable a connector for your organization, your team gets it automatically the first time they log in. With IdP-managed auth, identity is inherited from their existing identity provider groups and roles. With Claude-issued auth, users are matched at the connector by email address.

## What you control

You decide which connectors are enabled, which groups or roles get them, and at what access level:

- Auth connectors once for your organization, and access is given to your team automatically.

- Use **[role-based permissions](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans)** to choose exactly which roles get each connector, so different teams get the access that fits their work. See **Choose which roles get managed auth** below.

- Choose which permissions Claude can request when members connect through your identity provider, and narrow that further for individual roles.

- Revoke access. With IdP-managed auth, deprovisioning someone in your identity provider removes their connector access at the same time. With Claude-issued auth, removing someone from your Claude organization stops Claude from signing them in. Remove them from the connected service as well.

- Require that a connector only ever connects through managed authorization so personal accounts stay out of work tools.

**Note:** Each connector, and your identity provider if you use one, is operated by a third party under its own terms. With IdP-managed auth, Claude relays the authorization your identity provider issues, and access decisions, scoping, and the data each connector can reach are governed by your identity provider’s policies and the connected service’s permissions, not by Anthropic. With Claude-issued auth, Claude signs the sign-in for current members of your organization.

At your instruction, Anthropic sends each member's email address and a unique identifier to the connector. Claude checks organization membership only, not SSO, MFA, or the connector's own sign-in rules. Access decisions, scoping, and the data each connector can reach are governed by your Claude settings and the connected service's permissions.

Token lifetimes and lifecycle are managed by the connected authorization server and, with IdP-managed auth, your identity provider. Existing sessions end when the connector’s access token expires or is revoked.

## Choose which roles get managed auth

When you set up Enterprise-managed auth for a connector, you choose which roles inherit the connector when you set up role-based permissions. You can use role-based permissions to pilot a connector with a specific team before turning it on for your whole organization.

1. Go to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)** and select a connector.

2. On the **Configuration** tab, click "Set up" next to **Managed authorization**.

3. On the **Connect** step, choose an **Identity source**:

  1. **IdP-managed:** Confirm your identity provider connection. Follow the setup guide to configure Enterprise-managed auth for this connector in your identity provider, and to enable managed auth in the connector's own admin settings. Click "Run test" to confirm the connection works.

  2. **Claude-issued:** Follow the steps in **Set up Claude-issued auth** below.

4. On the **Roles** step, select who should get this connector automatically.

  1. **User, Admin, Owner, Primary owner**: your organization's built-in roles, as a group.

  2. Any custom role, selected individually.

  3. To pilot a connector with one team, select only that team's custom role and leave the built-in roles unchecked. Members on the User, Admin, Owner, or Primary Owner role won't get the connector until you come back and add that option.

5. On the **Scopes** step, choose which permissions Claude can request when members connect. These apply to every role you selected. To narrow permissions for a specific role, use that role's **Connectors** tab instead (see below).

6. Click "Save & turn on."

Once set up, the connector's Configuration tab shows its current state: **Applied roles** lists which roles connect through managed authorization, and **Scopes** shows what's granted. To expand a pilot, click "Edit" next to **Applied roles** and add "User, Admin, Owner, Primary owner" or more custom roles.

**Note:** **Browser sign-in** and **Managed authorization** can be on for a connector at the same time. When they are, Claude tries **Managed authorization** first and prompts the user to sign in individually if that fails, so members aren't locked out while an identity provider issue gets resolved.

## Connector settings inside a custom role

You can also start from a role in **Organization settings** > **Roles** instead of a connector. On a custom role's **Connectors** tab, **How members connect** controls how that role's members authenticate, across every connector at once, or per connector:

- **Individually**: members sign in with their own accounts.

- **Managed authorization**: members connect through the identity source set for each connector.

- **Set per connector**: choose individually for each connector.

## Use Claude-issued auth

With Claude-issued auth, Claude sends a signed assertion to the connector, under an issuer URL that’s unique to your organization. The connected service uses this URL to confirm that Claude signed the sign-in for a current member of your organization, so the service has to list it as a *trusted issuer*.

You don’t need an identity provider or SSO, although we still recommend enforcing SSO for your Claude organization. Claude checks organization membership only, not SSO, MFA, or the connector's own sign-in rules.

**Note:** Claude-issued auth is in beta.

### Before you start

- **A supported connector:** Only connectors whose provider supports Claude-issued auth can use it. See **Connectors** below.

- **An admin of the connected service:** You need someone who can add a trusted issuer to your workspace. This might be you.

- **Matching email addresses:** Users are matched by email, so each user’s Claude email must match the email on their account in the connected service.

- **The provider’s own requirements:** Some providers have their own requirements, such as SSO on their side. Check the provider’s setup guide.

Each connector uses one identity source at a time. You can switch later on the same setup screen.

### Set up Claude-issued auth

Set up Claude-issued auth once for each connector.

1. Go to **Organization settings > Connectors** and select a connector.

2. On the **Configuration** tab, click "Set up" next to **Managed authorization**.

3. On the **Connect** step, select "Claude-issued" under **Identity source**.

4. Copy the issuer URL.

5. In the connected service’s admin console, add the URL as a trusted issuer for your workspace. Follow the provider’s setup guide, linked from the **Connect** step. If you’re not an admin of that service, share the URL and the guide with someone who is.

6. If the connected service gives you a workspace or tenant ID, paste it into the tenant field in Claude.

7. Back in Claude, click "Test connection" to run the connection test, then click “Enable and continue.”

8. Choose who gets the connector. All roles get it by default.

If the test fails, check that the issuer URL is trusted in the correct workspace, that the tenant ID is correct, and that the workspace has an account with your email address.

To turn off Claude-issued auth, open the connector’s **Managed authorization** settings and choose "Disable." Users then connect to the service themselves.

### What users see

The connector is already connected the first time a user needs it, with no sign-in page or consent screen. A user whose email doesn’t match an account in the connected service isn’t connected automatically and sees the usual Connect prompt.

Before you announce the connector to your organization, ask two or three users to confirm that it’s connected and run a real request.

### When someone leaves your organization

Claude only signs for current members of your organization. When you remove someone, Claude stops signing them in to connected services, but access already granted at a service lasts until it expires. Remove them from each connected service before that email address is reused, or a new person with that address could be signed in to the old account.

If you use directory sync (SCIM), check that the person no longer appears in your member list. Claude removes a member when your directory deletes them, but not when your directory only suspends them or marks them inactive.

## What works with Enterprise-managed auth

Enterprise-managed auth works with the connectors your teams use day to day. With IdP-managed auth, your identity provider controls who gets access. With Claude-issued auth, Claude signs in current members of your organization.

### Identity providers

IdP-managed auth requires SSO with a supported identity provider. Okta is supported, with more identity providers coming soon. See **[Okta’s documentation](https://developer.okta.com/docs/guides/xaa-agent-to-app/main/)** for more details.

Claude-issued auth doesn’t use an identity provider, so no identity provider setup is needed.

### Connectors

Currently, you can provision these connectors through Enterprise-managed auth:

- Amplitude (see **[Amplitude’s documentation](https://amplitude.com/docs/amplitude-ai/amplitude-mcp/enterprise-managed-auth)**)

- Apollo.io (see **[Apollo’s documentation](https://knowledge.apollo.io/hc/en-us/articles/43827318678541-Integrate-Apollo-with-Claude#tabs-2)**)

- Asana (see **[Asana’s documentation](https://help.asana.com/s/article/cross-app-access)**)

- Atlassian (see **[Atlassian’s documentation](https://support.atlassian.com/security-and-access-policies/docs/configuring-enterprise-managed-authentication/)**)

- Canva (see **[Canva’s documentation](https://www.canva.com/help/manage-cross-app-access/)**)

- Crossbeam (see **[Crossbeam’s documentation](https://help.crossbeam.com/en/articles/17758536-set-up-enterprise-managed-authentication-with-claude-and-crossbeam)**)

- Datadog (see **[Datadog’s documentation](https://docs.datadoghq.com/account_management/org_settings/cross_app_access/)**)

- Dropbox (see **[Dropbox’s documentation](https://help.dropbox.com/integrations/connect-dropbox-to-claude)**)

- Figma (see **[Figma’s documentation](https://help.figma.com/hc/articles/41992841175959)**)

- Granola (see **[Granola’s documentation](https://docs.granola.ai/help-center/sharing/integrations/mcp#enterprise-managed-authorization)**)

- HubSpot (see **[HubSpot’s documentation](https://knowledge.hubspot.com/integrations/set-up-enterprise-managed-authentication-in-claude)**)

- Linear (see **[Linear’s documentation](https://linear.app/docs/mcp#enterprise-managed-authorization)**)

- Lovable (see **[Lovable’s documentation](https://docs.lovable.dev/features/enterprise-managed-auth)**)

- Mixpanel (see **[Mixpanel’s documentation](https://docs.mixpanel.com/docs/mcp/claude-enterprise-managed-auth)**)

- Monday.com (see **[Monday’s documentation](https://developer.monday.com/api-reference/docs/mcp-enterprise-managed-auth)**)

- Notion (see **[Notion’s documentation](https://www.notion.com/help/set-up-enterprise-managed-connections-for-notion-mcp)**)

- PagerDuty (see **[Pagerduty’s documentation](https://docs.pagerduty.com/ai-automation/advance/pagerduty-mcp-server/claude-auto-connect)**)

- Semrush (see **[Semrush’s documentation](https://developer.semrush.com/api/v4/introduction/semrush-mcp/#set-up-enterprise-managed-authorization-for-the-semrush-mcp-connector-in-claude)**)

- Slack (see **[Slack’s documentation](https://slack.com/help/articles/54548358406419)**)

- Supabase (see **[Supabase’s documentation](https://supabase.com/docs/guides/platform/sso/enterprise-mcp-authentication)**)

- Unblocked

Claude-issued auth works only with connectors whose provider supports it. The beta includes: Amplitude, Apollo.io, Atlassian, Datadog, Dropbox, Figma, Granola, HubSpot, Linear, Mixpanel, Notion, PagerDuty, Semrush, and Supabase.

Any MCP provider can add support for Enterprise-managed auth. See **[Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization)** for more details.

### Personal connectors

Your team can still add personal connectors on top of what you provision. Enterprise-managed auth handles the connectors you enable for your organization, while individuals can connect additional services for their own use.