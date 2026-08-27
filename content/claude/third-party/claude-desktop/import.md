> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Import history from claude.ai

> Bring conversations, projects, and local Cowork and Code sessions into Claude Desktop on 3P from a claude.ai workspace or an earlier install

Import brings a copy of your claude.ai conversations and projects into Claude Desktop on third-party (3P), along with any Cowork and Claude Code sessions already on this machine from an earlier install. Everything lands in the local session store described in [User identity and local data](/docs/third-party/claude-desktop/data-storage), so you can pick up work you started on claude.ai and continue it against your organization's own inference provider.

Each import is a one-time copy. New activity on claude.ai after you import does not appear in Claude Desktop unless you import again, and re-running the import does not create duplicates.

## Before you start

* Your administrator has turned import on by setting [`claudeAiImport`](/docs/third-party/claude-desktop/configuration#claudeaiimport) with `enabled` set to `true` in the managed configuration. Import is off by default; until then, **Settings → Import & export** reports that import isn't enabled for this deployment.
* Claude Desktop is installed and running in third-party mode. See [Installation and setup](/docs/third-party/claude-desktop/installation).
* To bring history over from a claude.ai Team or Enterprise workspace, an owner of that workspace has enabled member data export (next section). Personal claude.ai accounts can always export.

## Enable member data export (admins)

On Team and Enterprise workspaces, member data export is off by default. A workspace owner enables it on claude.ai under **Settings → Organization → Data and privacy → Allow members to export their own data**.

<Frame caption="The member data export toggle in claude.ai organization settings. Only workspace owners see this control.">
  <img src="https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-admin-toggle.png?fit=max&auto=format&n=HpR2FaaZXZXkiUcV&q=85&s=f1f4696a2124cd36ee9a7366cb1c4772" alt="claude.ai organization settings, Data and privacy page, with the Allow members to export their own data toggle turned on and a confirmation toast reading Member data export enabled." width="1800" height="1125" data-path="images/third-party/import/import-admin-toggle.png" />
</Frame>

Members of the workspace can then export their own conversations. The toggle does not expose one member's data to another; each member can download only their own history.

## Open the import wizard

In Claude Desktop, go to **Settings → Import & export** and click **Import…** to open the **Import from Claude** wizard.

<Frame caption="Step 1 of the import wizard, before a source is chosen.">
  <img src="https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-wizard-start.png?fit=max&auto=format&n=HpR2FaaZXZXkiUcV&q=85&s=526562f1c9c0abd66e9b56d0328808db" alt="Claude Desktop settings with Import and export selected and the Import from Claude wizard open on step 1, showing Sign in to claude.ai and Choose file buttons." width="1920" height="1440" data-path="images/third-party/import/import-wizard-start.png" />
</Frame>

The wizard has three steps: **Chats** (your claude.ai export), **Cowork & Code** (local sessions on this machine), and **Review**. Skip any step you don't need.

## Step 1: claude.ai chats and projects

You can pull your claude.ai history straight into the wizard by signing in, or download it from claude.ai yourself and choose the file.

<Tabs>
  <Tab title="Sign in to claude.ai (recommended)">
    Click **Sign in to claude.ai…**. Your browser opens to claude.ai; sign in if prompted, choose your organization if you belong to more than one, and click **Authorize**.

    <Frame caption="The organization selector, shown if your claude.ai account belongs to more than one workspace.">
      <img src="https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-consent-org.png?fit=max&auto=format&n=HpR2FaaZXZXkiUcV&q=85&s=1657a03028a7ceb3d173e71ba27f591d" alt="claude.ai organization selector titled Select organization, listing one organization." width="1600" height="720" data-path="images/third-party/import/import-consent-org.png" />
    </Frame>

    <Frame caption="The authorization prompt. The only permission granted is a one-time export of your own data.">
      <img src="https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-consent-authorize.png?fit=max&auto=format&n=HpR2FaaZXZXkiUcV&q=85&s=55be3501d41c9e61b49154db66b71d5b" alt="claude.ai authorization card reading Claude Desktop Import would like to connect to your Claude chat account, with an Authorize button." width="1400" height="1300" data-path="images/third-party/import/import-consent-authorize.png" />
    </Frame>

    Back in Claude Desktop, click **Fetch export**. The wizard requests an export from claude.ai, downloads it, and shows what it found.

    <Frame caption="The wizard after the export finishes downloading.">
      <img src="https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-signed-in.png?fit=max&auto=format&n=HpR2FaaZXZXkiUcV&q=85&s=dafc4cbfffd685321442cbd72fd73993" alt="Import from Claude wizard step 1 showing a claude.ai export row with the account email and a summary of 7 chats and 1 project." width="1920" height="1440" data-path="images/third-party/import/import-signed-in.png" />
    </Frame>
  </Tab>

  <Tab title="Choose a downloaded file">
    On claude.ai, go to **Settings → Privacy → Export data** and click **Export**. If you don't see **Export data**, ask a workspace owner to [enable member data export](#enable-member-data-export-admins).

    <Frame caption="The Export data page in claude.ai personal settings.">
      <img src="https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-web-export.png?fit=max&auto=format&n=HpR2FaaZXZXkiUcV&q=85&s=1ed4aa5a08469420020d3ff83579c0de" alt="claude.ai settings Privacy page with the Export data subpage open, showing an Export button and a note that a download link will be sent by email." width="1800" height="1125" data-path="images/third-party/import/import-web-export.png" />
    </Frame>

    claude.ai emails you a download link when the export is ready. The link expires after 24 hours.

    <Frame caption="The export-ready email.">
      <img src="https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-email.png?fit=max&auto=format&n=HpR2FaaZXZXkiUcV&q=85&s=cf883e9c401401686568c77cb6ac45c1" alt="Email from Claude titled Your data is ready for download with a Download data button." width="1800" height="1125" data-path="images/third-party/import/import-email.png" />
    </Frame>

    Download the `.zip`, then in the import wizard click **Choose file…** and select it.

    <Frame caption="Step 1 with a downloaded export selected.">
      <img src="https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-choose-file.png?fit=max&auto=format&n=HpR2FaaZXZXkiUcV&q=85&s=5cb868969ebed88801296f696796d0f1" alt="Import from Claude wizard step 1 showing a selected member-data zip file with a summary of 7 chats and 1 project." width="1920" height="1440" data-path="images/third-party/import/import-choose-file.png" />
    </Frame>
  </Tab>
</Tabs>

Click **Continue**, or **Skip this step** if you only want to bring in local sessions.

## Step 2: local Cowork and Code sessions

The wizard scans this machine for Cowork and Claude Code sessions from an earlier Claude Desktop install and lists what it finds. Choose how far back to include, and add any other folder that holds sessions (for example, a backup or a folder copied from another machine).

<Frame caption="Local sessions found on this machine.">
  <img src="https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-local-sessions.png?fit=max&auto=format&n=HpR2FaaZXZXkiUcV&q=85&s=e17511922a814b0355cb540688a5c949" alt="Import from Claude wizard step 2, Cowork and Code, listing 5 local sessions with a time-range selector and an option to add another location." width="1920" height="1440" data-path="images/third-party/import/import-local-sessions.png" />
</Frame>

Sessions are copied, not moved. Your original history stays where it is.

## Step 3: review and import

The **Review** step summarizes what will be added. Click **Import** to copy everything into your local session store.

<Frame caption="The review summary before import.">
  <img src="https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-review.png?fit=max&auto=format&n=HpR2FaaZXZXkiUcV&q=85&s=c7939485c7185afbf1ef7518a94db2d6" alt="Import from Claude wizard step 3 showing a claude.ai export summary of 7 chats and 1 project alongside 5 local Cowork and Code sessions, with an Import button." width="1920" height="1440" data-path="images/third-party/import/import-review.png" />
</Frame>

<Frame caption="Import complete. Imported chats appear in the sidebar and imported projects appear as Spaces.">
  <img src="https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-success.png?fit=max&auto=format&n=HpR2FaaZXZXkiUcV&q=85&s=c878c70886ff9a0fd2b3d046bf916375" alt="Import from Claude wizard success screen reading Imported 12 sessions and 1 Space, with a note that re-running import will not create duplicates." width="1920" height="1440" data-path="images/third-party/import/import-success.png" />
</Frame>

## Continue an imported conversation

Open any imported conversation from the sidebar and keep chatting. The first time you send a message in an imported session, Claude Desktop shows a **Resume imported session?** prompt. Click **Trust and resume** to continue; the reply comes from your configured inference provider, not from claude.ai.

<Frame caption="The trust prompt shown the first time you resume an imported session.">
  <img src="https://mintcdn.com/claude-ai/HpR2FaaZXZXkiUcV/images/third-party/import/import-trust-resume.png?fit=max&auto=format&n=HpR2FaaZXZXkiUcV&q=85&s=806d0d2018d7fc0f10afb71035b1f807" alt="An imported conversation open in Cowork with a yellow Resume imported session card offering Go back and Trust and resume buttons." width="1800" height="688" data-path="images/third-party/import/import-trust-resume.png" />
</Frame>

## Export sessions to move them to another device

When your administrator also sets `exportEnabled` to `true` under `claudeAiImport`, **Settings → Import & export** offers **Export…**, which writes this computer's chats, Cowork tasks, and Code sessions (not terminal Claude Code sessions) to a zip file. On the other device, open the import wizard and select that zip with **Choose file…**; the wizard lists its sessions in the [Cowork & Code step](#step-2-local-cowork-and-code-sessions). The export is a one-time snapshot, not a sync, and the zip contains full conversation content, so handle it as sensitive data.

## What is and isn't included

* **Your data only.** An export contains your own conversations, projects, and memory. Other workspace members' content is not included.
* **Chats and projects come over.** Each imported project becomes a Space. If the project has custom instructions, Claude Desktop shows them in the Space for you to review and accept before they take effect.
* **Project knowledge files and conversation attachments do not.** A member's own export never includes the contents of files uploaded to a project's knowledge or attached to a conversation. This is a security policy on claude.ai, and it applies to both the **Sign in to claude.ai** and **Choose a downloaded file** paths. Imported chats keep the messages that referenced an attachment, but not the file itself. The only export that includes file contents is an organization-level export, which only a workspace owner can request.
* **One-time copy.** Imported history does not stay in sync with claude.ai. Run the import again to pick up newer conversations; existing imports are matched and skipped, so you won't get duplicates.
* **Download links expire.** The email link from claude.ai is valid for 24 hours. Request a new export if it lapses.
