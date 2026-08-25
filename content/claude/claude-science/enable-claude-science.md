> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Enable Claude Science

> Claude Science is a desktop app for scientific research.

Claude Science is a desktop app for scientific research. It's off by default for Team and Enterprise organizations. Turning it on in Organization settings > Claude Science walks you through a short setup wizard that covers what's not supported yet, which roles get access, and which connectors to publish.

## Availability

Claude Science is in beta.

| Plan        | Claude Science app access             |
| ----------- | ------------------------------------- |
| Team        | Off; turn on in Organization settings |
| Enterprise  | Off; turn on in Organization settings |
| Pro and Max | On; no admin action needed            |
| Free        | Not available                         |

If your organization has HIPAA compliance enabled, Claude Science app access is also off by default. You can turn it on, but usage isn't covered under your Business Associate Agreement (BAA) and the app shouldn't be used with protected health information (PHI).

## Turn on Claude Science

Go to Organization settings > Claude Science.\
Turn on the Enable for your organization toggle. The setup wizard opens.\
Complete each step of the wizard, then select Enable Claude Science.\
Members with access can [download Claude Science](https://claude.com/product/claude-science) and sign in with their claude.ai account.

You need an Owner or Primary Owner role to turn Claude Science on or off. If you have the Admin role, you can add members and assign seats, but you can't turn on Claude Science. Ask an Owner or Primary Owner to turn it on.

### Reviewing role access

This step appears only on Enterprise plans. It lists any custom roles that already include the Claude Science capability. Built-in roles get access automatically. To change which custom roles have access, select Configure in role settings, or continue and adjust roles later.

### Setting up connectors for the organization

Enable the data sources your team will use in Claude Science.

Featured connectors are built by Anthropic and curated for scientific research.\
Local connectors ship with the app and run on each member's computer. Members can turn individual local connectors off in the app.\
Directory connectors are additional life sciences connectors from the Claude connector directory. On Team and Enterprise plans, these appear only after an Owner adds them to the organization's connector allowlist.

This step is shown read-only if your organization has HIPAA compliance enabled. Add connectors from Organization settings > Connectors after enabling.

By continuing, you authorize your team to let Claude use the optional enabled resources on their behalf. These resources and content they reach may be subject to third-party terms (viewable in Settings), and your users are solely responsible for compliance.

## Who gets access after you enable

Turning on the organization toggle controls whether Claude Science is accessible to your organization at all. Adding members or assigning seats doesn't turn it on. Once it's on, roles control which members can use it:

Built-in roles include the Claude Science entitlement, so those members can download and sign in immediately.\
Custom roles (Enterprise plans only) need the Claude Science capability added. Members on a custom role without the capability see the app as unavailable even after you enable it for the organization.\
A custom role whose Capability access setting is All capabilities already includes Claude Science. The All generally available setting excludes beta capabilities such as Claude Science, so for those roles also select the Claude Science capability.

This is the same pattern as other Claude apps you enable per organization.

## What members see

Once Claude Science is enabled and a member's role includes the entitlement, they can download the app from claude.com/product/claude-science and sign in with their claude.ai account.

If the organization toggle is off, claude.ai stops members at sign-in with a message such as "Claude Science has not been enabled for your account. Contact your organization administrator." On Enterprise plans, members whose custom role doesn't include the capability are stopped the same way.

Members who belong to more than one organization on claude.ai, such as a personal account alongside yours, need to choose your organization when claude.ai asks which one to connect. Before they select Authorize, they can also select Switch organization on the authorization screen to change that choice. A member who connects a Free personal account instead sees "Claude Science requires a Pro or Max subscription." and can select Switch account to sign in again and choose your organization.

## HIPAA organizations

Organizations with HIPAA compliance enabled can turn on Claude Science during the beta, but usage isn't covered under your BAA. The setup wizard shows this notice on step 1, and the connectors step is read-only because the wizard's quick-enable path doesn't include the per-connector HIPAA attestation. Add connectors from Organization settings > Connectors instead, where the attestation is required.

## Turn off Claude Science

Go to Organization settings > Claude Science and turn off the Enable for your organization toggle. Members can no longer sign in to the app. Data already on members' computers stays there; see [How Claude Science works with your data](/docs/claude-science/how-claude-science-works-with-your-data) for details.
