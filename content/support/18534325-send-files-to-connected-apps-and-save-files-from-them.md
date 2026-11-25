# Send files to connected apps and save files from them

Claude can send a file to an app you've connected, and it can save a file that the app offers. For example, Claude can upload a presentation it just made to your cloud storage, or pull in a contract so you can review it together. This article explains where file transfers work, how to use them, and how your files are handled.

File transfers with connectors are in beta. They're rolling out gradually on Pro, Max, and Ultra plans, and off on Team and Enterprise plans until an owner turns them on. The Free plan will follow. They work in Claude on the web, Claude Desktop, Claude for iOS, Claude for Android, and Claude Code.

---

## Where file transfers work

File transfers work in:

- Chats in the new Claude experience on the web, Claude Desktop, and Claude for iOS and Android

- Claude Code in your terminal, in VS Code, and on the web

File transfers don't work in:

- Incognito chats

- Scheduled tasks

- Claude Code sessions started with Remote Control

### Which apps you can use

The app needs to be in the **[connectors directory](https://claude.ai/directory)**, and its developer needs to have added file support. Custom connectors and MCP servers you add yourself don't work with file transfers.

---

## Send a file to an app

To send a file:

1. Connect the app from the **[connectors directory](https://claude.ai/directory)**.

2. Drag in or attach a file, or tell Claude which file to send. It can be a file Claude made.

3. Tell Claude where the file goes. For example, "Put this in my Receipts folder."

4. If Claude asks for approval, check the file and the app before you allow it.

### When Claude asks before sending

Claude asks before it sends the first file to each app, even in Auto mode or if the connector's tool is set to "Always allow." After that, Claude may send files without asking, depending on your permission settings.

---

## Save a file from an app

To save a file, ask Claude for it. For example, "Get the Q3 report from my Finance folder." Saving follows the permission you set for that connector tool.

### Files you save in a chat

The file is saved to that chat, where Claude can open it. You can open or download it from the chat.

### Files you save in Claude Code on your computer

The file is saved in a connector-downloads folder under ~/.claude/projects, and Claude Code shows the path. To use the file in your project, ask Claude to copy it there.

By default, Claude Code deletes saved files after 30 days, so copy anything you want to keep. Nothing is saved in plan mode.

---

## File limits

### Files you send

- **Claude Code on your computer:** You can send files up to 500 MB each and up to eight files at a time.

- **Chats and Claude Code on the web:** You can send up to 10 files at a time, up to 500 MB in total. Files you attach can be up to 400 MB each.

If several files are too large together, ask Claude to send them one at a time. Claude can send files but not folders. A photo you attach may be sent as a smaller copy.

### Files you save

You can save files up to 500 MB each and up to 10 files at a time. Most files have five minutes to download.

Claude Code adds .bin or .txt to some file types, such as .html. To open the file, rename it.

### Limits set by the app

An app can set a lower size limit or accept only some file types.

### Files Claude Code checks before sending

- **Files named like credentials:** Claude Code refuses most of these files, such as .env or .pem, unless you attached them yourself.

- **Files outside your working folders:** Claude Code asks before it sends one, even in Auto mode or if the tool is set to Always allow, unless you bypass permissions. To send a file from outside your home or temporary folder, add its folder with `/add-dir` first.

---

## How your files are handled

Files you attach or save in a chat or cloud session stay with that chat or session. They’re retained and deleted according to our data retention practices for **[consumer plans](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)** or **[Team and Enterprise plans](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)**. Files that Claude Code saves to your computer are stored on your computer.

Remember, photos and videos may include other metadata, such as the location where they were taken. The connected app handles the file under its own terms and privacy policy, or under your organization’s agreement with the app. Deleting your chat or session from Claude doesn’t delete the file from the connected app.

Files pass through Anthropic’s servers, and we keep a temporary encrypted copy of files you send. We may also keep a temporary copy of some images and videos for safety scanning. Deleting your chat or session doesn’t delete the scanning copy, which is typically deleted within two weeks unless we need to keep it longer for safety or legal reasons.

**Important:** A file from an app can contain text written to mislead Claude. Connect only apps you trust.

---

## Troubleshooting file transfers

### Claude can't send or save files

- Update Claude Code or the Claude app to the latest version, then start a new session or chat. Some chats, including many older ones, can't send or save files.

- In Claude Code, sign in with your Claude account. File transfers don't work with an API key or through a cloud provider.

- In Claude Code, check that `DISABLE_TELEMETRY`, `DO_NOT_TRACK`, and `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` aren't set. Each one turns off file transfers in Claude Code.

### Claude says the connector is custom or can't be confirmed

Remove the connector and add it again from the **[connectors directory](https://claude.ai/directory)**, or ask an Owner or Primary Owner in your organization to.

### A send fails or you stop it

Check the app before you try again. The file may have arrived.

### A file doesn't finish uploading from your phone

Until the file has finished uploading, keep Claude open on your screen and don't let the screen turn off.

---

## Manage file transfers on Team and Enterprise plans

### Turn on file transfers

Sending and saving files are both off by default. Owners and Primary Owners can turn on one or both:

1. Navigate to **Organization settings > Connectors**.

2. Under **File transfers**, turn on **File uploads to connectors**, **File downloads from connectors**, or both.

3. Ask users to start a new chat or Claude Code session.

Each setting applies to the whole organization. Connector tools you've blocked stay blocked. In chats, members also need Chat and Cowork unified, in **Organization settings > Capabilities**.

## Compliance records

On Enterprise plans with the Compliance API enabled, sent files are usually recorded in its activity feed. Saved files may not be recorded. Learn more about **[accessing the Compliance API](https://support.claude.com/en/articles/13015708-access-the-compliance-api)**.

### Organizations that can't use file transfers

Some organizations can't use file transfers, including:

- Organizations that use HIPAA settings, zero data retention, customer-managed encryption keys, Access Transparency, or an IP allowlist

- Organizations whose default workspace keeps data outside the US

- Organizations set up for FERPA, and Claude for Teachers accounts

Sending files isn't available to organizations that allow inference hooks.

### What happens if a connector can't receive files

Remove the connector and add it again from the **[connectors directory](https://claude.ai/directory)**. Check who has access to it afterward, because removing it can reset that.