# What are artifacts and how do I use them?

An **[artifact](https://claude.com/features/artifacts)** is anything Claude makes for you that you'd put in front of someone: a design, a deck, a document, a dashboard, or a small interactive tool. It opens beside your conversation, and you can edit it, come back to it, and share it with others. Ask for one in any conversation with Claude, including in Claude Code, or start from a template in the “Artifacts” tab.

Artifacts are available on Free, Pro, Max, Team, and Enterprise plans, and in Claude Code on every plan that includes Claude Code. The Docs, Slides, and Design templates are available on all plans and are on by default. On Enterprise plans, they turn on by default on October 15, 2026, and owners can turn them on before then.

The Dashboards template is in beta on Pro, Max, Team, and Enterprise plans. On Enterprise plans, it's off by default until an owner turns it on. The Motion template is in beta on Team and Enterprise plans. It's on by default on Team plans and off on Enterprise plans until an owner turns it on.

| **Feature**                                   | **Free** | **Pro** | **Max** | **Team** | **Enterprise** |
| --------------------------------------------- | -------- | ------- | ------- | -------- | -------------- |
| Create artifacts in a chat                    | ✅        | ✅       | ✅       | ✅        | ✅              |
| Start from a Docs, Slides, or Design template | ✅        | ✅       | ✅       | ✅        | ✅              |
| Start from a Dashboards template (beta)       |          | ✅       | ✅       | ✅        | ✅              |
| Start from a Claude Motion template (beta)    |          |         |         | ✅        | ✅              |
| Connect your apps to an artifact              |          | ✅       | ✅       | ✅        | ✅              |
| Store data in an artifact                     |          | ✅       | ✅       | ✅        | ✅              |

**Important:** Artifacts require **Cloud code execution and file creation** to be turned on in **[Settings > Capabilities](https://claude.ai/settings/capabilities)** (Free, Pro, Max) or **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)** (Team, Enterprise).

---

## What is an artifact?

**Note:** Legacy artifacts are artifacts made in a chat before September 16, 2026. They keep working, and you can still publish and share them, but you can't make new ones.

Claude creates an artifact when the content it's sharing meets these criteria:

- It's significant and self-contained, typically over 15 lines.

- It's something you're likely to want to edit, iterate on, or reuse outside the conversation.

- It stands on its own without needing extra context from the conversation.

- It's content you're likely to refer back to or use later.

Claude can make an artifact out of almost anything, including documents, code snippets, single-page websites, images, diagrams and flowcharts, dashboards, and small interactive tools.

## Where you can use artifacts

- **Claude on the web and Claude Desktop:** Create, edit, and share artifacts, and start from a template.

- **Claude Code:** Publish session output as an artifact, or make designs and docs. See **[Artifacts in Claude Code](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them#h_dca5623bec)** below.

- **Claude for iOS and Claude for Android:** Ask for a design, deck, or doc in any chat, view the result in the **Artifacts** tab, and edit the artifact. To change sharing settings, use Claude on the web or Claude Desktop.

## Start from a template

Templates are starting points for work you'll share with others. Ask for one in any chat, select "Output" in the message box and choose a template, or pick one in the **Artifacts** tab.

- **Docs:** Living documents you write with Claude and your team in real time. Learn more in **[Get started with Claude Docs](https://support.claude.com/en/articles/16923645)**.

- **Slides:** Presentations built from your notes, reports, or the work already in your chat. Edit any slide directly, present without leaving Claude, and export to PowerPoint or PDF. To edit and present with a keyboard or screen reader, see **[Use Claude Slides with a keyboard](#h_11975db891)** below.

- **Design:** Visuals, mockups, prototypes, one-pagers, and landing pages, built with your design system. Learn more in **[Get started with Claude Design](https://support.claude.com/en/articles/14604416)**.

- **Dashboards (beta):** Dashboards built from your data platforms or connected apps, like Salesforce. Claude writes the queries, and each chart shows its query and when it was last refreshed. Learn more in **Get started with Claude Dashboards**.

- **Motion (beta):** Animated explainers, charts, and walkthroughs built from your content. Ask Claude to change any detail, like a word, a number, or the timing, and the rest stays as it was. Export the result as an MP4 video. Available on Team and Enterprise plans. Learn more in **Get started with Claude Motion**.

Whichever template you start from, the artifact works the same way: edit it by talking to Claude or directly in the artifact, and it updates live as you work. When it's ready, share it or export it.

Designs and decks can use a design system, so new work picks up your colors, fonts, and components. Learn more about **[setting up your design system](https://support.claude.com/en/articles/14604397)**.

## Find your artifacts

Everything you make is saved to the **[Artifacts](https://claude.ai/artifacts)** tab in your Claude sidebar, so you can find it again from any conversation. From there you can view all your artifacts in one place, start a new one from a template, and organize what you've made.

## Work with artifacts

An artifact opens in its own window beside your conversation. Artifacts made from a template open on a canvas or page you can work in directly.

## Edit and iterate

- Ask Claude to change the artifact.

- In an artifact made from a template, edit directly: type in a doc, edit a slide, or move elements on a design canvas.

- In a doc or Markdown document, highlight the text you want changed, click "Edit with Claude," and type your request. Claude makes the edit where you marked it, so you don't have to describe which section you mean.

- Edit an earlier message to create a different version of the chat, with its own artifacts, so you can explore another direction without losing previous work.

**Note:** When Claude drafts content across multiple Markdown files, such as a skill or plugin, you can leave edit requests in several files before submitting. Each request is added to your next message, and the file list shows how many are waiting in each file. Send the message and Claude applies the whole batch in one pass.

## View and export

- **Artifacts made from a template:** Click "Export." Docs export to Word, PDF, Markdown, and Google Docs. Decks export to PowerPoint and PDF, or go straight to Google Slides as editable files. Designs export as a .zip, PDF, PowerPoint, or standalone HTML, or go straight to another tool. Animations export as MP4 video.

- **Legacy artifacts:** Use the controls at the top of the artifact panel to view the code, copy the content, or download it.

## Build on a published artifact

Available on Free, Pro, and Max plans, for legacy artifacts published from a chat.

If someone publishes an artifact you like, you can use it as a starting point for your own version. Your version is separate, so nothing you do affects the original.

**Important:** Only do this with artifacts from people you trust. You're bringing someone else's code and content into your own chat, so treat it the way you'd treat a file from an unknown sender.

1. Open the published artifact and click "Copy" to copy its code.

2. Start a new chat, paste the code, and describe the changes you want. For example: "Here's the code for a quiz game. Change the questions to be about movies and add a timer."

3. Refine the new artifact the same way you would any artifact you made yourself.

## Fix errors

If an artifact generates an error, look for the "Try fixing with Claude" button near the error message. Click it to copy the error details into a new message, then send it to Claude to diagnose the issue and suggest a fix. Claude will attempt to fix the error, but success isn't guaranteed. Some errors need more troubleshooting.

---

## Use Claude Slides with a keyboard

To get into and out of the artifact panel, and to comment from the panel's header, see **[Use artifacts with a keyboard or screen reader](https://support.claude.com/en/articles/17457950)**. That article also explains what focus means, what to do on a Mac laptop or in Safari, and how the tables show keys.

The editor is divided into areas: the toolbar at the top, the slide you're editing, a formatting toolbar that floats over whatever is selected, the list of slide thumbnails, and the properties panel.

### Move between the editor's areas

Press F6 to move to the next area and Shift+F6 to move to the previous one. Cmd+F6 (Ctrl+F6 on Windows) works in place of F6, with or without Shift. Each area remembers where you last were in it. F6 is paused while a menu, pop-up, or dialog is open, and while you're presenting.

### Edit a slide

The slide is a single stop when you press Tab. The objects on it are inside the slide: you go into the slide to reach them, and a group has its own objects inside it in the same way.

1. Press Tab until you reach the slide.

2. Press Return to go into the slide.

3. Press Tab or Shift+Tab to move between the objects on the slide. Tab doesn't leave the slide.

4. Press Return on a text box to start editing it. The cursor starts at the end of the text. On a group, Return moves inside the group.

5. Type your changes.

6. Press Escape or Tab to finish editing. Your change is kept.

7. Press Escape again to go back out to the slide. From inside a group, Shift+Return goes up one level instead.

In a table, Tab and Return move between cells. Press Escape or Cmd+Return (Ctrl+Enter on Windows) to finish.

With a free-standing object selected, the arrow keys move it (an object that's part of the slide's layout stays where the layout puts it), and F6 takes you to its formatting toolbar. With a screen reader, the slide and each object tell you which key goes in and which comes back.

### Move between slides

With nothing selected on the slide, press the Left arrow or Right arrow key, or Page Up or Page Down, to change slides. With a screen reader, you hear the new slide's number and title. If an object is selected, the arrow keys move the object instead, so press Escape first.

You can also press F6 until you reach the list of thumbnails. There, the Left arrow and Right arrow keys move between slides, showing each one in the editor as you go, and Return moves you onto that slide.

**Important:** Delete or Backspace on a thumbnail deletes that slide right away. Cmd+Z (Ctrl+Z on Windows) brings it back.

### Present a deck

1. Press Tab until you reach "Present" in the toolbar.

2. Press Return to open its menu.

3. Press Return on "Present" to start.

While you're presenting, press the Right arrow key or Space for the next slide, the Left arrow key for the previous one, and Escape to end. With a screen reader, you hear each slide's number and title as it appears. When you end the presentation, focus returns to "Present."

### Comment on a slide

To comment on a slide or on something on it, see "Comment on a deck or a design" in **[Use artifacts with a keyboard or screen reader](https://support.claude.com/en/articles/17457950)**.

### Get an overview of a deck

The "Canvas" view, which shows every slide at once, doesn't give a screen reader anything to read. Use the list of thumbnails instead.

### Claude Slides keyboard shortcuts

| **Action**                                                                 | **Mac**                                         | **Windows**                                     |
| -------------------------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- |
| Next area                                                                  | F6 or Cmd+F6                                    | F6 or Ctrl+F6                                   |
| Previous area                                                              | Shift+F6 or Cmd+Shift+F6                        | Shift+F6 or Ctrl+Shift+F6                       |
| Go into the slide, a group, or a text box                                  | Return                                          | Enter                                           |
| Next object, previous object                                               | Tab, Shift+Tab                                  | Tab, Shift+Tab                                  |
| First object, last object                                                  | Home, End                                       | Home, End                                       |
| Up one level                                                               | Shift+Return                                    | Shift+Enter                                     |
| Back out to the slide                                                      | Escape                                          | Escape                                          |
| Finish editing text                                                        | Escape or Tab                                   | Escape or Tab                                   |
| Next cell (while editing a table)                                          | Tab or Return                                   | Tab or Enter                                    |
| Finish editing a table                                                     | Escape or Cmd+Return                            | Escape or Ctrl+Enter                            |
| Move the selected object (free-standing objects only)                      | Arrow keys (Shift for smaller steps)            | Arrow keys (Shift for smaller steps)            |
| Bring to front, send to back (free-standing objects only)                  | ], [                                            | ], [| | Duplicate the object, or the slide when focus is in the list of thumbnails | Cmd+D | Ctrl+D | | Delete | Delete or Backspace | Delete or Backspace | | Bold, italic, underline (on a text box) | Cmd+B, Cmd+I, Cmd+U | Ctrl+B, Ctrl+I, Ctrl+U | | Undo, redo | Cmd+Z, Cmd+Shift+Z | Ctrl+Z, Ctrl+Shift+Z or Ctrl+Y | | Add a text box | T | T | | Add a rectangle, rounded rectangle, oval, or diamond | R, Shift+R, O, D | R, Shift+R, O, D | | Add a line or a connector | L, Shift+L | L, Shift+L | | Previous slide, next slide (nothing selected) | Left arrow or Page Up, Right arrow or Page Down | Left arrow or Page Up, Right arrow or Page Down | | Zoom in, zoom out, fit to the window | Cmd+Plus, Cmd+Minus, Cmd+0 | Ctrl+Plus, Ctrl+Minus, Ctrl+0 | If the arrow keys don't move an object, it's part of the slide's layout, which positions it for you. Ask Claude to move it. The single-letter shortcuts work when you're not typing and focus isn't on the formatting toolbar or in the properties panel. The new object appears on the slide, selected, and a new text box opens for typing. Cmd+Z (Ctrl+Z on Windows) removes it. For a new text box, press Escape first to finish typing. In the formatting toolbar: the Left arrow and Right arrow keys move between buttons, Home and End move to the first and last, Return or Space uses a button, and Tab or Escape goes back to the object. In the list of thumbnails (the Menu key is the key some Windows keyboards have between the right Alt and Ctrl keys; it opens the menu you'd get with a right-click): | **Action** | **Mac** | **Windows** | | ---------------------------------------------------------- | ----------------------- | ------------------------- | | Previous slide, next slide (the editor shows it as you go) | Left arrow, Right arrow | Left arrow, Right arrow | | First slide, last slide | Home, End | Home, End | | Move onto that slide in the editor | Return | Enter | | Open the slide's menu | Shift+F10 | Shift+F10 or the Menu key | | Delete the slide (a deck keeps at least one) | Delete or Backspace | Delete or Backspace | The slide's menu includes "Duplicate slide," "Add slide after," "Move left," "Move right," "Skip slide," and "Delete slide." "Move left" and "Move right" are how you reorder slides from the keyboard. While presenting: | **Action** | **Key** | | --------------------------------------------- | -------------------------------------------- | | Next slide | Right arrow, Down arrow, Page Down, or Space | | Previous slide | Left arrow, Up arrow, or Page Up | | First or last slide | Home or End | | Jump to that slide, if the deck has that many | 1 to 9 | | Full screen on or off | F | | End the presentation | Escape | **Note:** In Chrome versions 150 to 152, and in Claude Desktop, VoiceOver doesn't read text as you type or move through it in a text box on a slide. Use Chrome 153 or later. --- ## Artifacts that use Claude You can build artifacts that call Claude directly, turning them into small apps. People using your artifact can ask questions, generate content, get coaching, play games, and solve problems, with Claude adapting to what they enter. Describe what you want, Claude writes the code, and the app runs on Anthropic's infrastructure. People using it sign in with their Claude account and interact with their own instance. No API keys are required, and there's no cost to you. Whether your artifact helps 10 people or 10,000, sharing is free, and usage counts against each person's own plan limits rather than yours. On Team and Enterprise plans, people in your organization can use what you share without adding cost for you. For legacy artifacts, you can turn this off with the **AI-powered artifacts** setting in **[Settings > Capabilities](https://claude.ai/settings/capabilities)**. New artifacts ask you for permission the first time they want to use Claude.

---

## Connect your apps to an artifact

Available on Pro, Max, Team, and Enterprise plans, on Claude on web and desktop.

Artifacts can connect to the apps you've connected to Claude, so they can read from and write to tools like Asana, Google Calendar, and Slack. They can also connect to any **[custom connectors](https://support.claude.com/en/articles/11175166)** you've set up.

The first time an artifact needs a connected app, Claude shows which apps and tools it will use and asks you to approve them. You can turn individual tools off, and your choice carries over to later uses of that artifact. Connector tools that need approval for each action aren't available to artifacts.

**Important:** Everyone connects their own apps, even when using a shared or published artifact. On Team and Enterprise plans, an owner can turn this off for your whole organization. Learn more in the **[Artifacts admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/16994751)**.

---

## Store data in an artifact

Available on Pro, Max, Team, and Enterprise plans, on Claude on the web and Claude Desktop.

Artifacts can store data between sessions, so you can build things like journals, trackers, and collaborative tools. Storage is either personal or shared:

- **Personal storage:** Everyone keeps their own private data. In a journal artifact, your entries stay visible only to you.

- **Shared storage:** Everyone sees and works with the same data. In a game leaderboard, everyone sees the same scores.

The first time you use an artifact with shared storage, Claude shows a confirmation explaining that your data will be visible to others using it.

**Note:** In legacy artifacts, storage works only after you publish. While you're building and testing, storage operations won't succeed until you publish. New artifacts don't need to be published to store data.

Storage has a 20 MB limit per artifact and accepts text only, no images, files, or binary data. Personal and shared storage are kept separate, and unpublishing a legacy artifact permanently deletes all its stored data.

**Warning:** Whoever builds an artifact decides which data uses personal storage and which uses shared. Before entering anything sensitive, check whether the artifact uses shared storage.

---

## Artifacts in Claude Code

Artifacts are available in Claude Code on every plan that includes Claude Code.

Claude Code can publish its session output as an artifact, a live interactive page at a private URL. The page updates in place as your session continues, and you can share it. An artifact might be a pull-request walkthrough with annotated diffs, a dashboard built from session data, or an investigation timeline that fills in as Claude works.

You can also make designs and docs from Claude Code. Use /design for Claude Design, or ask for a doc. On desktop, the doc opens in the side panel. In the terminal, Claude gives you a link to open it on the web.

To learn how to create, update, and share artifacts in Claude Code, see the **[artifacts documentation on Claude Code Docs](https://code.claude.com/docs/en/artifacts)**.

---

## Live artifacts from Claude Cowork

Artifacts made in Claude Cowork before August 19, 2026 are live artifacts. They keep working, but you can't edit them in place. Learn more in **[Use live artifacts in Claude Cowork](https://support.claude.com/en/articles/14729249)**.

---

## Share an artifact

Artifacts start private to you. Learn more about **[sharing artifacts](https://support.claude.com/en/articles/9547008)**, including who can open them and what they see.