> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Enable Claude Science

> Claude Science is a desktop app for scientific research.

Claude Science is a desktop app for scientific research. It's off by default for Team and Enterprise organizations. Turning it on in **Organization settings** > **Claude Science** opens a short dialog that covers who gets access and which connectors to turn on. You can change any of it later on the same page, which also holds the other [organization settings](/docs/claude-science/admin-controls#organization-settings) for Claude Science: which connectors, skills, compute, network access, and memory members can use.

## Availability

Claude Science is in beta.

| Plan        | Claude Science app access                 |
| ----------- | ----------------------------------------- |
| Team        | Off; turn on in **Organization settings** |
| Enterprise  | Off; turn on in **Organization settings** |
| Pro and Max | On; no admin action needed                |
| Free        | Not available                             |

If your organization has HIPAA compliance enabled, Claude Science app access is also off by default. You can turn it on, but usage isn't covered under your Business Associate Agreement (BAA) and the app shouldn't be used with protected health information (PHI). These organizations also start with stricter organization settings (see [HIPAA organizations](#hipaa-organizations)).

## Turn on Claude Science

Go to **Organization settings** > **Claude Science**.\
Turn on the **Enable for your organization** toggle. The **Turn on Claude Science** dialog opens.\
Complete each step of the dialog, described below, then select **Turn on Claude Science**. Nothing is saved until you do.\
Review the [organization settings](/docs/claude-science/admin-controls#organization-settings) below the toggle, which unlock once Claude Science is on.\
Members with access can [download Claude Science](https://claude.com/product/claude-science) and sign in with their claude.ai account.

You need an Owner or Primary Owner role to turn Claude Science on or off. If you have the Admin role, you can add members and assign seats, but you can't turn on Claude Science. Ask an Owner or Primary Owner to turn it on.

### Review role access

This step shows who gets access once Claude Science is on. On Team plans, everyone in your organization gets access automatically. On Enterprise plans, members in the built-in roles (User, Admin, Owner, and Primary Owner) get access automatically, and the step lists any custom roles that already include the **Claude Science** capability. To change which custom roles have access, select **Configure in role settings**, or continue and adjust roles later.

### Set up connectors

Turn on the tools and data sources your team will use in Claude Science. You can change all of it later.

Under **Featured connectors**, the **Claude Science local connectors** row covers the connectors that are built by Anthropic, ship with the app, and run on each member's computer. Expand it to turn individual connectors on or off for the whole organization; you can change this later under [Featured connectors and skills](/docs/claude-science/admin-controls#featured-connectors-and-skills), and members can also turn individual local connectors off for themselves in the app. The **PubMed**, **Clinical Trials**, **ChEMBL**, and **bioRxiv** rows are connectors Anthropic hosts. They start selected, and turning Claude Science on adds the selected ones to **Organization settings** > **Connectors** for your organization, which makes them available to members in Claude Science and in claude.ai.

Under **From the Claude connector directory**, you can select additional life-sciences connectors, which are added to your organization the same way.

The **PubMed**, **Clinical Trials**, **ChEMBL**, and **bioRxiv** rows and the directory list are read-only if your organization has HIPAA compliance enabled or your role can't add connectors for the organization; add those connectors from **Organization settings** > **Connectors** after enabling. The switches for the local connectors still work, and in an organization with HIPAA compliance enabled they start off so you can turn on the ones you have reviewed.

By continuing, you authorize your team to let Claude use the optional enabled resources on their behalf. These resources and content they reach may be subject to third-party terms (viewable in Settings), and your users are solely responsible for compliance.

## Who gets access after you enable

Turning on the **Enable for your organization** toggle controls whether Claude Science is accessible to your organization at all. Adding members or assigning seats doesn't turn it on. Once it's on, roles control which members can use it:

Built-in roles include the Claude Science entitlement, so those members can download and sign in immediately.\
Custom roles (Enterprise plans only) need the **Claude Science** capability added. Members on a custom role without the capability see the app as unavailable even after you enable it for the organization.\
A custom role whose **Capability access** setting is **All capabilities** already includes Claude Science. The **All generally available** setting excludes beta capabilities such as Claude Science, so for those roles also select the **Claude Science** capability.

This is the same pattern as other Claude apps you enable per organization.

## What members see

Once Claude Science is enabled and a member's role includes the entitlement, they can download the app from claude.com/product/claude-science and sign in with their claude.ai account.

If the **Enable for your organization** toggle is off, members are stopped at sign-in with a message such as "Your organization hasn't turned on Claude Science yet. Ask your admins for access." They can select **Request access** to send that request to the organization's admins, then sign in again once Claude Science is on. On Enterprise plans, members whose custom role doesn't include the capability are stopped the same way, with a message that Claude Science isn't available for their account yet, and can also request access. These requests appear under **Requests** in **Organization settings** > **Notifications**. Turning Claude Science on resolves them, and for a member whose custom role lacks the capability, you give the role access on the **Roles** page.

Members who belong to more than one organization on claude.ai, such as a personal account alongside yours, need to choose your organization when claude.ai asks which one to connect. Before they select **Authorize**, they can also select **Switch organization** on the authorization screen to change that choice. A member who connects a Free personal account instead sees "Claude Science requires a Pro or Max subscription." and can select **Switch account** to sign in again and choose your organization.

## HIPAA organizations

Organizations with HIPAA compliance enabled can turn on Claude Science during the beta, but usage isn't covered under your BAA, so keep protected health information out of it. The **Turn on Claude Science** dialog opens with a step that says so. In its connectors step the local connectors start off, and you can turn on the ones you have reviewed. The Anthropic-hosted and directory connectors in that step are read-only because the dialog's quick-enable path doesn't include the per-connector HIPAA attestation, so add those from **Organization settings** > **Connectors** instead, where the attestation is required.

These organizations also start with stricter organization settings. Featured connectors and skills, SSH hosts, Modal, model endpoints, and memory are off until you turn them on (including for members who were already using them), custom connectors can't be turned on, and the organization always manages the network allowlist. See [Defaults by plan](/docs/claude-science/admin-controls#defaults-by-plan).

## Turn off Claude Science

Go to **Organization settings** > **Claude Science** and turn off the **Enable for your organization** toggle. Members can no longer sign in to the app, and members who are already signed in lose access within a few minutes. The app stops accepting new messages and shows a notice that Claude Science isn't available for their account. The other settings on the page keep their values and apply again when you turn Claude Science back on. Data already on members' computers stays there; see [How Claude Science works with your data](/docs/claude-science/how-claude-science-works-with-your-data) for details.
