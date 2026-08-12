# Authorize MCP connectors for your entire organization

This article explains how Enterprise-managed auth works and how admins can authorize connectors for their organization through their identity provider. With Enterprise-managed auth, you authorize a connector once for your entire organization, and your team inherits access automatically on first login.

This feature is available in beta for Team and Enterprise plans on Claude. If you are a Claude customer, **[apply for access to get started](https://claude.com/form/ema-waitlist)**. If you are an MCP provider, **[apply here](https://docs.google.com/forms/d/e/1FAIpQLSf1goHGNDVFK7rncYuh6wnRpWSy7eGOcgL1i8uw3oyKFO9UUA/viewform?usp=sharing&ouid=101055591948883487705)**. We’ll share documentation with customers and MCP providers on how to get started once you have access.

## What is Enterprise-managed auth?

Enterprise-managed auth is an authorization and authentication model for connectors in Claude. Instead of having every person authenticate each connector individually, admins provision connector access centrally through the organization's identity provider.

Once you enable a connector for your organization, your team gets it automatically the first time they log in, with identity inherited from their existing identity provider groups and roles.

## What you control

You decide which connectors are enabled, which groups or roles get them, and at what access level:

- Auth connectors once for your organization, and access is given to your team automatically.

- Use role-based permissions to choose exactly which roles get each connector, so different teams get the access that fits their work. See **Choose which roles get managed auth** below.

- Choose which permissions Claude can request when members connect through your identity provider, and narrow that further for individual roles.

- Revoke access by deprovisioning someone in your identity provider, which removes their connector access at the same time.

- Require that a connector only ever connects through your identity provider so personal accounts stay out of work tools.

**Note:** Your identity provider and each connector are operated by third parties under their own terms. Claude relays the authorization your identity provider issues; access decisions, scoping, and the data each connector can reach are governed by your identity provider’s policies and the connected service’s permissions, not by Anthropic.

Token lifetimes and lifecycle are managed by the connected authorization server and identity provider. Existing sessions end when the connector’s access token expires or is revoked.

## Choose which roles get managed auth

When you set up Enterprise-managed auth for a connector, you choose which roles inherit the connector when you set up role-based permissions. You can use role-based permissions to pilot a connector with a specific team before turning it on for your whole organization.

1. Go to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)** and select a connector.

2. On the **Configuration** tab, click "Set up" next to **Managed authorization**.

3. On the **Connect** step, confirm your identity provider connection. Follow the setup guide to configure Enterprise-managed auth for this connector in your identity provider, and to enable managed auth in the connector's own admin settings. Click "Run test" to confirm the connection works.

4. On the **Roles** step, select who should get this connector automatically.

  1. **User, Admin, Owner, Primary owner**: your organization's built-in roles, as a group.

  2. Any custom role, selected individually.

To pilot a connector with one team, select only that team's custom role and leave the built-in roles unchecked. Members on the User, Admin, Owner, or Primary Owner role won't get the connector until you come back and add that option.

5. On the **Scopes** step, choose which permissions Claude can request when members connect through your identity provider. These apply to every role you selected. To narrow permissions for a specific role, use that role's **Connectors** tab instead (see below).

6. Click "Save & turn on."

Once set up, the connector's Configuration tab shows its current state: **Applied roles** lists which roles connect through managed authorization, and **Scopes** shows what's granted. To expand a pilot, click "Edit" next to **Applied roles** and add "User, Admin, Owner, Primary owner" or more custom roles.

**Note:** **Browser sign-in** and **Managed authorization** can be on for a connector at the same time. When they are, Claude tries **Managed authorization** first and prompts the user to sign in individually if that fails, so members aren't locked out while an identity provider issue gets resolved.

### Connector settings inside a custom role

You can also start from a role in **Organization settings** > **Roles** instead of a connector. On a custom role's **Connectors** tab, **How members connect** controls how that role's members authenticate, across every connector at once, or per connector:

- **Individually**: members sign in with their own accounts.

- **Managed authorization**: members connect through your identity provider.

- **Set per connector**: choose individually for each connector.

## What works with Enterprise-managed auth

Enterprise-managed auth brings together two things your organization already uses: your identity provider, which controls who gets access, and the connectors your teams work with day to day.

### Identity providers

Okta is supported at launch, with more identity providers coming soon. See **[Okta’s documentation](https://support.okta.com/help/s/article/claude-enterprise-managed-auth-with-okta-cross-app-access-xaa-beta-participation-guide?language=en_US)** for more details.

### Connectors

Currently, you can provision these connectors through Enterprise-managed auth:

- Asana

- Atlassian

- Canva

- Figma

- Granola

- Linear

- Supabase

- Slack (coming soon)

Any MCP provider can add support for Enterprise-managed auth. See **[Enterprise-Managed Authorization](https://modelcontextprotocol.io/extensions/auth/enterprise-managed-authorization)** for more details.

### Personal connectors

Your team can still add personal connectors on top of what you provision. Enterprise-managed auth handles the connectors you enable for your organization, while individuals can connect additional services for their own use.