# Invite people outside your organization to an artifact

You can invite specific people by email to access an artifact. They sign in to Claude with that email address and can then open the artifact with the access you give them. Unlike sharing with "Anyone with the link," an invitation works only for the person you invite.

Inviting people by email is in beta and available on Pro, Max, Team, and Enterprise plans.

## Before you invite someone

- The artifact’s owner can invite people. On Team and Enterprise plans, anyone in your organization who can edit the artifact can also invite people after the owner sets a **Shared version**. The owner gets an email when someone else sends an invitation.

- This feature is on by default for Team plans and off by default for Enterprise plans. Owners can adjust this setting in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)** to control whether you can invite people outside your organization.

- The person needs a Claude account with the email address you invite. If they don't have one, they need to create one with that address before they can open it. Claude doesn't tell you whether they have an account.

- Some artifacts can’t be shared with people outside your organization, and the “Share” menu tells you when this applies. For example:

  - Documents made with Claude Docs

  - Artifacts that haven’t been published yet

  - Artifacts that connect to outside websites

  - Artifacts with an uploaded file that’s still being checked or didn’t pass the check

## Invite someone

1. Open the artifact and click “Share.”

2. In the field at the top of the **Share** menu (**Add people**, or **Invite people by email** on Pro and Max plans), type the person’s email address.

3. Select the **Invite** option that shows their address.

4. Under **Their access**, choose “Can view,” “Commenter,” or “Can edit.”

5. If you’re asked to choose a **Version they’ll see**, pick the version you want to share.

6. Click “Invite.”

On Team and Enterprise plans, if you type the email address of someone in your organization, they’re added to the artifact directly instead of getting an invitation.

## Access levels

| **Access**    | **What they can do**                                                                                           |
| ------------- | -------------------------------------------------------------------------------------------------------------- |
| **Can view**  | Open the version of the artifact you shared and read its comments.                                             |
| **Commenter** | Everything in **Can view**, plus add comments and download any files the artifact offers. This is the default. |
| **Can edit**  | Everything in **Commenter**, plus see the latest version, make changes, and publish new versions.              |

At every level, people outside your organization can’t invite others or change sharing settings. Parts of the artifact that use Claude or your connectors don’t work for them. People with **Can edit** access can’t delete the artifact, and they can upload only images and videos to it.

People you invite with **Commenter** or **Can edit** access can comment. They can’t mention people or ask Claude in a comment, and they don’t get email notifications about comments. They can’t comment on an artifact that’s also shared with "Anyone with the link."

If the artifact is also shared with "Anyone with the link," the people you invited have the same access as anyone with the link, whatever level you gave them.

## What invited people see

1. They get an email from Claude (<no-reply-claude@mail.anthropic.com>) that shows the email address of the person who invited them and what access they’ll have.

2. They click “View invitation” and sign in to Claude in a web browser with the email address you invited.

3. They click “Accept and open” to open the artifact.

To come back to the artifact later, they can open the link in the invitation email again or bookmark the artifact.

## Manage people you’ve invited

In the artifact’s **Share** menu, people you’ve invited appear under **Invited from outside your organization**. Pending invitations show when they expire. From there, you can change someone’s access or remove them. Removing someone takes away their access right away.

If someone didn’t get an invitation email because they didn’t have a Claude account yet, ask them to create one with that address. Then remove the invitation and invite them again.

## When access changes

- **Pending invitations expire after 30 days.** Accepted invitations don’t expire.

- **If you change who can open the artifact to “Only you”:** On Team and Enterprise plans, everyone you invited from outside your organization loses access and their invitations are removed. On Pro and Max plans, people you invited keep their access.

- **If you delete the artifact:** Everyone you invited loses access.

- **If the person who sent an invitation leaves your organization or loses edit access:** Their pending invitations stop working. People who already accepted keep access until someone removes them.

- **If an owner turns off email invitations:** Invited people can’t open the artifact until the setting is turned back on. Accepted invitations aren’t deleted, and pending ones still expire 30 days after they were sent.

## Limits

- You can invite up to 50 people outside your organization per artifact. This includes pending and accepted invitations.

- Invitation emails are in English.

## If you got an invitation you didn’t expect

Click “Report this invitation” in the email, or “Didn’t expect this? Report this invitation” on the invitation page. Reporting declines the invitation, and the person who sent it isn’t notified. After you report an invitation, that person can’t invite you by email again.

## For Team and Enterprise plans

This section applies to Team and Enterprise plans.

When email invitations are on, anyone in your organization who can edit an artifact can invite people outside your organization to it, once the owner sets a **Shared version**. Invited people can't share the artifact further or use your connectors through it.

### Turn email invitations on or off

1. Navigate to **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

2. Turn **Email invitations outside your organization** on or off.

This setting requires **Artifacts** to be on. It’s separate from **External sharing**, which controls sharing with "Anyone with the link."

### Defaults

- **Team:** On by default.

- **Enterprise:** Off by default.

Email invitations aren’t available for some organizations, including education and K-12 organizations, and organizations using customer-managed encryption keys (CMEK), zero data retention, or a HIPAA-ready configuration.

### See and remove outside access

1. Navigate to **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

2. Under **Published artifacts**, find an artifact marked **Shared outside**.

3. Open the artifact’s menu and select “Manage outside access.”

4. Select the remove button next to the person, then confirm with “Remove access” or “Remove invitation.”

Admins can remove people here but can’t change their access level.