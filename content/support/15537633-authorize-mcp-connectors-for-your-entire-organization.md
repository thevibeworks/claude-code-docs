# Authorize MCP connectors for your entire organization

This article explains how Enterprise-managed auth works and how admins can authorize connectors for their organization through their identity provider. With Enterprise-managed auth, you authorize a connector once for your entire organization, and your team inherits access automatically on first login.

This feature is available in beta for Team and Enterprise plans on Claude. If you are a Claude customer, **[apply for access to get started](https://claude.com/form/ema-waitlist)**. If you are an MCP provider, **[apply here](https://docs.google.com/forms/d/e/1FAIpQLSf1goHGNDVFK7rncYuh6wnRpWSy7eGOcgL1i8uw3oyKFO9UUA/viewform?usp=sharing&ouid=101055591948883487705)**. We’ll share documentation with customers and MCP providers on how to get started once you have access.

## What is Enterprise-managed auth?

Enterprise-managed auth is an authorization and authentication model for connectors in Claude. Instead of having every person authenticate each connector individually, admins provision connector access centrally through the organization's identity provider.

Once you enable a connector for your organization, your team gets it automatically the first time they log in, with identity inherited from their existing identity provider groups and roles.

## What you control

You decide which connectors are enabled, which groups or roles get them, and at what access level:

- Auth connectors once for your organization, and access is given to your team automatically.

- Scope access by group, team, or role, so different teams get the access that fits their work (integration with role-based permissions coming soon).

- Revoke access by deprovisioning someone in your identity provider, which removes their connector access at the same time.

- Require that a connector only ever connects through your identity provider so personal accounts stay out of work tools.

**Note:** Your identity provider and each connector are operated by third parties under their own terms. Claude relays the authorization your identity provider issues; access decisions, scoping, and the data each connector can reach are governed by your identity provider’s policies and the connected service’s permissions, not by Anthropic.

Token lifetimes and lifecycle are managed by the connected authorization server and identity provider. Existing sessions end when the connector’s access token expires or is revoked.

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