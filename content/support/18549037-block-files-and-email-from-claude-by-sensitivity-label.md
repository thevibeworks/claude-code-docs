# Block files and email from Claude by sensitivity label

Owners and Primary Owners can choose Microsoft Purview sensitivity labels to block in Claude. Claude then doesn't work with content that has those labels in the Microsoft 365 connector and in Claude for Excel, PowerPoint, Word, and Outlook.

You connect your Microsoft Entra tenant to Claude, then pick labels from a list. You can connect one tenant to each Claude organization.

Sensitivity label blocking is in beta for Enterprise plans. Label blocking isn't available to organizations that have enabled HIPAA, to hybrid deployments, or in government and national clouds. It also isn't available to organizations with FERPA or zero data retention terms.

**Important:** When enabled, Claude is restricted from reaching files with specific Purview labels, even if the user has access to them normally. Not all files or surfaces are covered, so this setting shouldn't replace your organization's own access controls. See **[What label blocking doesn't cover](#h_5d523d6ae7)**.

## How label blocking works

Label blocking uses the sensitivity labels on your Microsoft 365 content. It limits what Claude can work with, and doesn't change the permissions people have in Microsoft 365. It applies differently in each product:

- **Microsoft 365 connector:** labels are blocked for everyone who uses Anthropic's Microsoft 365 connector with a work or school account from your tenant, including people outside your Claude organization.

  - If another Claude organization connects to the same tenant, the connector blocks the labels that either organization chose.

- **Claude for Excel, PowerPoint, Word, and Outlook:** labels are blocked for members who are signed in to the add-in with an account in your Claude organization. Add-ins that use a third-party platform, such as Amazon Bedrock or a gateway, have their own settings. See “Local connector and third-party platforms.”

### In the Microsoft 365 connector

| **When Claude tries to**                                                                                                        | **What happens**                                                                                                                                   |
| ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Open or download a file with a blocked label, or one whose label can't be determined, such as a password-protected file         | Claude gets a notice instead of the content.                                                                                                       |
| Rename, move, copy, or delete a file with a blocked label, or one whose label can't be determined                               | Refused.                                                                                                                                           |
| Replace the content of a labeled file                                                                                           | Refused when Microsoft reports any label on the file, because replacing the content could remove the label.                                        |
| Search SharePoint and OneDrive, or a whole mailbox                                                                              | Files and emails with a blocked label are left out when Microsoft's search index holds the label.                                                  |
| List a SharePoint or OneDrive folder                                                                                            | Files with a blocked label are listed by name. Claude can't open them.                                                                             |
| Open an email with a blocked label, or one of its attachments                                                                   | Claude gets a notice instead of the content.                                                                                                       |
| List or search a mail folder, or search a shared mailbox                                                                        | Emails with a blocked label, and emails whose label can't be determined, are left out.                                                             |
| Reply to, forward, move, change, send, or delete an email or draft with a blocked label, or one whose label can't be determined | Refused. If the action covers a thread or several emails, one blocked email refuses the whole action.                                              |
| Open a Word, Excel, PowerPoint, or PDF attachment with a blocked label                                                          | Refused, even when the email itself isn't blocked. Password-protected PDFs and encrypted Office attachments are refused regardless of their label. |

The connector checks Word, Excel, and PowerPoint files, PDFs, and MP4 videos. While your list has at least one label, it also refuses OneNote, Loop, and Whiteboard items, regardless of their label.

### In Claude for Excel, PowerPoint, Word, and Outlook

Claude doesn't work with an open document, email, or draft that has a blocked label, or whose label it can't check. The pane shows a message instead. If an add-in can't load your organization's list, Claude may read and work with content that has a blocked label until the list loads.

For what each message means, how to check that it works, and what isn’t covered in the add-ins, see **[Block documents and email by sensitivity label](https://claude.com/docs/office-agents/sensitivity-labels)**.

## Before you start

### In Claude

You need to be an Owner or Primary Owner on an Enterprise plan. A custom role with Owner access works too. The Admin role, and a custom role with only the Privacy permission, can't manage labels.

### In Microsoft Entra

The Microsoft account you sign in with needs one of these roles:

- Global Administrator

- Privileged Role Administrator

- Compliance Administrator

- Compliance Data Administrator

- Security Administrator

- Azure Information Protection Administrator

The first time, Microsoft may also ask for an admin's approval. A Global Administrator or Privileged Role Administrator can approve while connecting. Otherwise, ask one of them to approve, then connect again. If your organization uses Privileged Identity Management, activate your role before you sign in.

### In SharePoint and Purview

The connector can only block a label that Microsoft reports. Ask your Microsoft 365 admin to check these settings:

- **Files:** turn on **[co-authoring for files with sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels-coauthoring)** and **[PDF support](https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-onedrive-files#adding-support-for-pdf)**, plus **[video support](https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-onedrive-files#video-support-mp4-files)** if you label videos. Otherwise SharePoint may report no label for a file, and Claude can read it.

- **Email:** in Purview, include emails in the scope of each label you want to block on email.

- **Multi-Geo tenants:** run `Set-SPOTenant -EnableAIPIntegration $true` in each geo location.

## Connect your tenant

1. Navigate to **[Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls)** in your web browser.

2. Open “Blocked sensitivity labels.”

3. Click “Connect tenant.”

4. Sign in with the Microsoft account that has one of the Microsoft Entra roles in “Before you start”. A Global Administrator or Privileged Role Administrator can select “Consent on behalf of your organization,” if Microsoft asks.

5. Check the name and tenant ID, then click “Connect tenant” to confirm. Do this soon, because your Microsoft sign-in expires after a short time.

Claude uses this sign-in to check the role and read your list of labels. It doesn't read files or email with it.

## Choose labels to block

To choose labels to block:

1. Navigate to **[Organization settings > Data and privacy](https://claude.ai/admin-settings/data-privacy-controls)**.

2. Open “Blocked sensitivity labels.”

3. Click “Add labels.”

4. Search for and select each label you want to block, then click the button that adds them.

When you choose labels, keep these rules in mind:

- **Sublabels are separate.** Blocking a parent label doesn't block its sublabels, so select them too. Sublabels added later aren't blocked automatically.

- **A new label can take time to appear.** If a label is missing, sign in to Microsoft again to refresh the list.

- **Only your own tenant's labels work.** Content labeled by another Microsoft Entra tenant has that tenant's labels, so your list doesn't match it.

- **You can block up to 48 labels in each tenant,** counted across every Claude organization that's connected to it.

Changes to your label blocklist usually reach the Microsoft 365 connector within 30 minutes. People may need to reload or reopen an add-in. See **[Set up label blocking](https://claude.com/docs/office-agents/sensitivity-labels#set-up-label-blocking)**.

Once a change takes effect, Claude can't open newly blocked content. Content Claude already read stays in existing chats.

## Check that blocking works

Use a OneDrive or SharePoint file with a blocked label that doesn't apply encryption, and an email with a blocked label sent from another account. Allow a few minutes after you label them, and 30 minutes after you change your list.

Ask Claude to open the file and the email with the connector. Claude should respond with a message explaining that it can't show their content, or say that it can't find them.

To check the add-ins, see **[Check that blocking works](https://claude.com/docs/office-agents/sensitivity-labels#check-that-blocking-works)**.

## Remove a label or disconnect

To stop blocking a label, open “Blocked sensitivity labels,” then remove it.

To stop blocking all of your organization's labels, disconnect the tenant. If another Claude organization is connected to your tenant, the labels it blocks stay blocked in the Microsoft 365 connector. The approval you gave Claude in Microsoft Entra stays until you remove it in Microsoft Entra.

If your organization moves off the Enterprise plan or enables HIPAA, label blocking isn't available anymore. You can't add labels, and the ones on your list may not be blocked. You can still remove the labels from your list.

## What label blocking doesn't cover

Claude compares your list with the label that Microsoft reports, or the label stored in the document or email attachment. Content that is unlabeled or mislabeled, or whose label Microsoft hasn't recorded yet, may not be blocked.

**Names and details can still appear.** Claude can still see some information about blocked content:

- SharePoint and OneDrive folder listings show a blocked file's name, size, modified time, and link.

- Until Microsoft's search index holds the label, a search can return a blocked file's name, or a blocked email's subject, sender, recipients, and date. Labeled email in Sent Items and Drafts might still appear in a search of the whole mailbox.

- An email that isn't blocked lists its attachments by name, type, and size, including a blocked attachment.

**Some content isn't checked:**

- **Other file types:** for example text files, images, archives, and email messages saved as files.

- **Files inside a folder:** when Claude moves, copies, or deletes a folder, the files inside aren't checked.

- **Other attachments:** images, text files, attached emails, and cloud links are covered only by the email's own label.

- **Other Microsoft 365 content:** calendar events, Teams messages, meeting transcripts, and SharePoint pages and lists. A blocked meeting invitation can still be read as a calendar event.

- **Files given to Claude directly, outside of the connector:** files attached in chat, projects, or Cowork, and local files in Cowork.

- **People outside your tenant:** labels aren't blocked for someone who connects with another tenant's account or a personal Microsoft account, even for a file you shared with them.

- **Pasted, typed, or quoted text:** for example, text copied from a blocked document, or an unlabeled reply, forward, or draft that quotes a blocked email.

- **Linked or embedded content in documents:** only the document's own label is checked.

- **Content Claude creates:** new files and emails.

- **The add-ins:** see **[What is not covered](https://claude.com/docs/office-agents/sensitivity-labels#what-is-not-covered)**.

**Labels that encrypt content:** add each one you want blocked to your list. Don't rely on the encryption alone to keep the content from Claude.

**A newly applied label** **can take time to register.** Microsoft records labels on its own schedule, including labels from auto-labeling policies and library defaults. Until it does, Claude can read the content.

## Local connector and third-party platforms

The list in Organization settings doesn't apply to these setups, which have their own settings:

- **The local Microsoft 365 connector in Claude Desktop:** see **[Block content by sensitivity label](https://claude.com/docs/third-party/claude-desktop/connectors-m365#block-content-by-sensitivity-label)**.

- **Add-ins that use a third-party platform,** for example through Amazon Bedrock, Google Cloud Vertex AI, Azure AI Foundry, an API key, or a gateway: see **[Use Claude for M365 with third-party platforms](https://claude.com/docs/office-agents/third-party-platforms#admin-feature-controls)**.

## Troubleshooting

### A file or email without a blocked label is refused

Claude blocks content when it can't determine the label. For files, check whether the file is encrypted, password-protected, or damaged, and whether the settings under “Before you start” are on. OneNote, Loop, and Whiteboard items are always refused while your list has a label. Claude also can't replace the content of a file when Microsoft reports any label on it.

### A labeled file or email wasn't blocked

- Check that the exact label or sublabel is on your list.

- If you just applied the label, wait a few minutes and try again. If you just changed the list, wait 30 minutes.

- Check the settings under “Before you start.” If Microsoft doesn't report a label, the connector can't block it.

## Frequently asked questions

### Does label blocking work with Microsoft Purview data loss prevention?

Label blocking doesn't evaluate your data loss prevention policies, or policies you set for Microsoft Copilot. It only compares labels with your list.

### Can I see which files or emails were blocked?

Claude's audit logs don't include an event for each blocked item. Connecting or disconnecting a tenant, and adding or removing a label, are recorded in your organization's **[audit logs](https://support.claude.com/en/articles/9970975-access-audit-logs)**.

### Does label blocking change people's access in Microsoft 365?

No. People can still open the content in Microsoft 365.