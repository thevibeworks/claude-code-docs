> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Block documents and email by sensitivity label

> How Claude for Excel, PowerPoint, Word, and Outlook handle documents and email that have a Microsoft Purview sensitivity label your organization blocks.

Your organization can choose Microsoft Purview sensitivity labels that
Claude for Excel, PowerPoint, Word, and Outlook do not work with. While a
document or email has a blocked label, Claude does not read it, and the
task pane shows a message instead.

> [!NOTE]
>
> Sensitivity label blocking is in beta on Enterprise plans. It applies when
> you sign in with an account in your Claude organization. If your
> organization manages the add-ins from the Enterprise Admin Console, set
> document access policies on the console's Office Agents page instead. See
> [Change settings or turn off sign-in](https://claude.com/docs/office-agents/admin-console.md#change-settings-or-turn-off-sign-in).
> If you connect through Amazon Bedrock, Google Cloud Vertex AI, Azure AI
> Foundry, an API key, or a gateway, use `access_policies` instead. See
> [Admin feature controls](https://claude.com/docs/office-agents/third-party-platforms.md#admin-feature-controls).

## Set up label blocking

Owners and Primary Owners connect their Microsoft Entra tenant and choose
the labels in Claude Organization settings. One list covers the add-ins and
the Microsoft 365 connector. See
[Block files and email from Claude by sensitivity label](https://support.claude.com/en/articles/18549037)
for the steps.

Checking email labels in Outlook also needs a Microsoft 365 admin to
[grant Microsoft Graph consent](https://claude.com/docs/office-agents/outlook.md#grant-microsoft-graph-consent).
Grant it before you block a label. Otherwise, received email shows "Can't
check this email's label".

In the add-ins, labels are blocked for members who are signed in with an
account in that Claude organization. An add-in that was open before your
organization blocked its first label does not check labels until you reopen
it. After later changes, wait 15 minutes, then reload the add-in and reopen
the document if you have it open.

## Check that blocking works

Use a Word, Excel, or PowerPoint file with a blocked label that does not
apply encryption, and an email with a blocked label sent from another
account. Allow a few minutes after you label them, and 15 minutes after you
change the list. Open the file and select the email. The task pane shows
that Claude is unavailable. Attach the file in another document, and it is
not uploaded.

## Excel, PowerPoint, and Word

Claude reads the label from the document on your device.

| You see | What it means | What to do |
| - | - | - |
| "Claude is unavailable for this document" | The document has a blocked label. | Use a different document, or ask your admin. |
| "Can't verify this document" | Claude cannot read the document's label, for example because the document is password-protected. | Select "Try again" if the screen has it. On the web, open the document in the desktop app. Otherwise, use a different document or ask your admin. |
| "Can't check your organization's policy" | Claude could not load your organization's list, and this device already knows that your organization blocks labels. | Check your connection, then select "Try again". |
| "Restricted by your organization's access policy and not uploaded" | The file you attached has a blocked label, or its label cannot be read. | Attach a different file. |

Labels are checked in the document you have open, and in current Office
formats and PDF files you attach. While your organization blocks at least
one label:

* Office 97-2003 files and encrypted files cannot be attached.
* Encrypted documents in Word and Excel for the web are blocked because
  Office for the web does not let Claude read the label. Open them in the
  desktop app.
* A label you apply while the pane is open takes effect when you return to
  the pane or reload it.

## Outlook

Claude reads a received email's label through Microsoft Graph, and a
draft's label from Outlook.

| You see | What it means | What to do |
| - | - | - |
| "Claude is unavailable for this email" | The email or draft has a blocked label. | Select another email, or ask your admin. |
| "Can't check this email's label" | Claude could not read the label, or could not load your organization's list. | Select "Try again" and finish the Microsoft sign-in. If the screen says "This Outlook client doesn't support Microsoft Graph sign-in", update Outlook or use Outlook on the web. Otherwise, ask your admin to check [Microsoft Graph consent](https://claude.com/docs/office-agents/outlook.md#grant-microsoft-graph-consent). |

Lists and searches leave out blocked email, and email whose label cannot be
read. While your organization blocks at least one label:

* Claude cannot forward an email that has any attachment, including inline
  images.
* Claude does not read an attached PDF, or Office file in a current format,
  that has a blocked label or a label Claude cannot read.
* Searches of the whole mailbox leave out Deleted Items and Junk Email, and
  Claude may not be able to list subfolders.
* In some older versions of Outlook, every draft shows "Can't check this
  email's label". Update Outlook or use Outlook on the web.
* Email in a shared or delegated mailbox shows "Can't check this email's
  label". Claude for Outlook does not support these mailboxes.

A label change on a draft normally shows in the pane at once. If it does
not, Claude reads the label again the next time you act in the pane.

## What is not covered

Label blocking does not cover these cases:

* **Text in other places**: text you paste or type, and quoted text in a
  reply, forward, or draft, unless that reply, forward, or draft itself has
  a blocked label.
* **Embedded and linked content**: embedded files, links, formulas or
  fields that point to other files.
* **Subjects when you select several emails**: Claude can see the subjects
  of the emails you select, including blocked ones.
* **Devices without the list**: if the add-in cannot load the list, for
  example the first time you open the add-in on a device, Claude may read
  and work with content that has a blocked label until the list loads.
* **Other attachments and files**: images, text files, archives, attached
  emails, and cloud links have no label check of their own. On an email
  that is not blocked, older `.doc`, `.xls`, and `.ppt` attachments are not
  checked either.
* **Calendar items**: meetings and events are not checked.
* **Deliberate workarounds**: label blocking helps prevent accidental use.
  It does not stop someone who deliberately works around it.

> [!WARNING]
>
> When enabled, Claude is restricted from reaching files with specific Purview
> labels, even if the user has access to them normally. Not all files or
> surfaces are covered, so this setting should not replace your organization's
> own access controls. [Learn more](https://support.claude.com/en/articles/18549037)

## Related

These pages cover the add-ins, security, and storage in more detail:

* [Use Claude for Outlook](https://claude.com/docs/office-agents/outlook.md)
* [Security, admin auditability, and analytics](https://claude.com/docs/office-agents/enterprise-readiness.md)
* [Data storage and retention](https://claude.com/docs/office-agents/data-storage.md)
* [Block files and email from Claude by sensitivity label](https://support.claude.com/en/articles/18549037)
