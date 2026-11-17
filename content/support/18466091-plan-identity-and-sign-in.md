# Plan identity and sign-in

A Claude Desktop on 3P deployment has several separate sign-ins, and most can use a different identity system. List them before you schedule your move. If you're also changing identity providers (IdPs), the order of the two projects matters, because by default claude.ai accepts one IdP at a time.

This guide is for admins of organizations on Claude Enterprise plans.

This article is part of **[Move from Claude Enterprise to Claude Desktop on a cloud provider](https://support.claude.com/en/articles/18426225)**, which defines the terms wave, overlap period, and cutoff date.

## Sign-ins your users will see

| **Sign-in**                                     | **Who sees it**                                                                                                                                                                                          | **What it uses**                                                                                                                                                                                                                                |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| claude.ai (your Claude Enterprise organization) | Every user, until their last import. The import wizard **[opens claude.ai in the browser to sign in and authorize](https://claude.com/docs/third-party/claude-desktop/import)**.                         | The SSO connection held by your **[parent organization](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)**.                                               |
| Enterprise Admin Console                        | Only users whose app is managed from the console. With MDM, a local file, or a bootstrap server, **[users have no Anthropic account](https://claude.com/docs/third-party/claude-desktop/data-storage)**. | A Claude account under the user's work email, **[through your SSO if you connect it](https://claude.com/docs/third-party/claude-desktop/admin-console)**. SSO is recommended but not required. The sign-in expires about once a month.          |
| Your provider                                   | Every user, unless you deploy a shared key, a credentials file, or a credential helper.                                                                                                                  | IAM Identity Center, Google or Workforce Identity, or Entra ID. It's **[separate from the Claude sign-in](https://claude.com/docs/third-party/claude-desktop/admin-console)**, and the app never sends Claude credentials to your provider.     |
| Bootstrap server                                | Only deployments that use one with per-user sign-in.                                                                                                                                                     | Your own IdP. It's **[independent of the inference sign-in](https://claude.com/docs/third-party/claude-desktop/bootstrap)**, except in device-code mode, where one sign-in covers both if the gateway and the bootstrap server share an origin. |
| Connectors                                      | Each user, once per connector.                                                                                                                                                                           | **[The IdP of the connector's vendor](https://claude.com/docs/third-party/claude-desktop/mcp-sign-in)**. The app stores each connector token on the device, so users connect each one again in the new app.                                     |
| Claude Code CLI                                 | Developers.                                                                                                                                                                                              | The cloud provider's own credential chain. See **Move Claude Code CLI users**.                                                                                                                                                                  |

## Connect your IdP to your cloud provider

Each provider's setup guide explains how to connect your IdP.

- **Amazon Bedrock:** Make your IdP **[the identity source for IAM Identity Center](https://claude.com/docs/third-party/claude-desktop/bedrock)**. AWS allows **[only one identity source per organization in AWS Organizations](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source.html)**. Before you change it, read AWS's **[considerations for changing your identity source](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-considerations.html)**.

- **Google Cloud:** Use **[Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation)** with **[an OIDC provider in the pool](https://claude.com/docs/third-party/claude-desktop/vertex)**. A pool can federate one or more IdPs.

- **Microsoft Foundry:** Foundry uses **[Entra ID directly](https://claude.com/docs/third-party/claude-desktop/foundry)**. If you have Conditional Access rules, see **[Sign in through the OS identity broker](https://claude.com/docs/third-party/claude-desktop/entra-broker)**.

- **LLM gateway:** Users sign in to **[your IdP](https://claude.com/docs/third-party/claude-desktop/gateway)**, and your gateway checks each user's token.

## If you're changing IdPs

- **By default, claude.ai takes one IdP.** **[Each parent organization links to one IdP](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)**, and **[all verified domains must use it](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)**. The exception is a beta: parent organizations enrolled in centralized management can **[connect more than one IdP](https://support.claude.com/en/articles/18246779-set-up-multiple-identity-providers-and-split-domains)**. A domain can't get a second IdP while any organization uses JIT provisioning, or while Microsoft Login is turned on for that domain. Outside the beta, you can't run the old and new IdPs side by side there.

- **Follow our steps for switching IdPs.** See **[Switching to a different Identity Provider (IdP)](https://support.claude.com/en/articles/13443687-switching-to-a-different-identity-provider-idp)**. Resetting the SSO connection signs out all users. They can sign in by email link until the new connection is live. For Entra ID, see **[Microsoft Entra ID SSO setup](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup)**.

- **Make sure email addresses match exactly.** Claude **[matches SSO logins to seats by email](https://support.claude.com/en/articles/13917829-microsoft-entra-id-sso-scim-email-mismatch)**. A mismatch in the new IdP **[creates duplicate accounts](https://support.claude.com/en/articles/13443687-switching-to-a-different-identity-provider-idp)**, and a SCIM email change **[removes the old user and creates a new one](https://support.claude.com/en/articles/14499648-how-scim-sync-works-for-enterprise-organizations)**. Fix mismatches before anyone imports.

- **Check whether your Enterprise Admin Console organization shares the connection.** If it **[uses the existing SSO connection, SCIM directory, and verified domains](https://claude.com/docs/third-party/claude-desktop/admin-console)**, one IdP serves both. Before you reset SSO or close the older organization, ask your Anthropic account team how it affects the Enterprise Admin Console organization and the devices it manages.

We recommend this order:

1. Connect the new IdP to your cloud provider first, and pilot sign-in there. On AWS, if IAM Identity Center already uses the old IdP, this step replaces that organization's one identity source. You can't pilot the two side by side in the same AWS organization.

2. If the old IdP will stay in service long enough, leave the claude.ai SSO connection alone until the last wave has imported.

3. If the old IdP retires sooner, make the switch between waves. Don't switch while a wave is importing. Compare the email attributes in both IdPs first.

4. Keep claude.ai sign-in and member data export working until the final import is done.

## Settings for the overlap period

- **Sign-in screen:** Users can choose claude.ai or your provider configuration. **[`deploymentMode`](https://claude.com/docs/third-party/claude-desktop/mdm#restrict-a-device-to-one-deployment-mode)** set to `3p` hides the claude.ai option (Claude Desktop 4.16336.0 or later). Set it in a device profile that also sets your connection. For earlier versions, also set `disableDeploymentModeChooser` to `true`. You can't set either key in the console. Don't set them on a device the console manages, because they **[make the app stop using the console](https://claude.com/docs/third-party/claude-desktop/admin-console#keep-a-device-on-its-managed-profile)**.

- **Organization lock:** **[`forceLoginOrgUUID`](https://claude.com/docs/third-party/claude-desktop/admin-console#keep-a-device-on-its-managed-profile)** limits standard sign-in on the device to your organization. It also accepts **[a list of organization IDs](https://support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop)**. With the console, include your Enterprise Admin Console organization's ID as well as your Claude Enterprise organization's, and update devices to 2.37337.0 or later first. Otherwise, the console's settings don't apply.

- **Network allowlist:** **[Tenant Restrictions](https://support.claude.com/en/articles/13198485-enforce-network-level-access-control-with-tenant-restrictions)** uses a header that lists allowed organization IDs. Make sure it includes every organization your users still sign in to.

- **Users in two organizations:** A console user who also belongs to another organization is **[asked whether to switch, and each switch restarts the app](https://claude.com/docs/third-party/claude-desktop/admin-console)**. Turn on **Require this organization in Claude Desktop** so users can't dismiss the prompt. If your Claude Enterprise organization blocks other accounts in Claude Desktop, first add the Enterprise Admin Console organization's ID to its Allowed organizations list.

- **Claude Code CLI:** List both providers in `allowedProviders` during the overlap period. **[`CLAUDE_CONFIG_DIR`](https://code.claude.com/docs/en/authentication)** gives each account its own configuration directory.