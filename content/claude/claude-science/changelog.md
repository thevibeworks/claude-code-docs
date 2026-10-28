> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Science changelog

> Release notes for Claude Science, including new features, improvements, and bug fixes by version.

**0.1.71**

October 27, 2026

* If usage credits are turned on at claude.ai while Claude Science is open, it now pauses at your usage limit and asks before it keeps spending them
* When Claude's servers time out before a reply starts, Claude Science now tries again instead of stopping right away with an error
* Fixed custom connectors failing to load behind a proxy with "unexpected end of file" when their server sends an empty reply marked as compressed
* The sandbox now protects `.devcontainer`, `.cursor`, `.codex`, and `.gemini` folders in a folder you've granted. On a Mac, use your own terminal to clone or unpack a project that holds one; on Linux they look empty inside the sandbox, so committing all changes there (for example with `git commit -a`) records their files as deleted
* Mac and Linux: Claude now installs pip packages into [task environments](https://claude.com/docs/claude-science/tools-and-environments.md#task-environments) only as prebuilt packages (wheels), not from a git repository, web address, or local folder or file. A package with no wheel for your computer and Python version won't install there; if an older version has one, pip may install that instead. For other ways to install a package, see [Tools and environments](https://claude.com/docs/claude-science/tools-and-environments.md#python-package-sources-for-starter-and-task-environments)
* Linux: as in 0.1.61, Claude Science again runs bubblewrap and socat only from system folders such as `/usr/bin` and `/usr/local/bin`, not from your PATH. With your distribution's bubblewrap (0.8.0 or later) and socat, nothing changes; Ubuntu 22.04 and earlier, Debian 11 and earlier, RHEL and Rocky 8 and 9, and Amazon Linux 2 ship an older bubblewrap or none
* Linux: if your bubblewrap or socat is your own copy (for example from conda or pixi), [approve it once](https://claude.com/docs/claude-science/run-on-remote-linux-server.md#approve-your-own-copy-of-bubblewrap-or-socat) or ask an administrator to install both. Until then, updating from the app or running the install command again keeps your current version and says what to do
* Linux: with your own copy, don't update by typing `claude-science update`. It can replace your current version, and 0.1.71 then won't start until your copy is approved (see [Troubleshooting](https://claude.com/docs/claude-science/troubleshooting.md#not-approved))
* Bug fixes and reliability improvements

**0.1.70**

October 21, 2026

* Bug fixes and reliability improvements

**0.1.69**

October 21, 2026

* As a precaution following the publicly reported compromise of several emSign (eMudhra) intermediate certificate authority (CA) keys, most of the connections Claude Science makes itself, and many of the package installs it runs itself, no longer trust emSign (eMudhra) root certificates or one other root certificate. Versions 0.1.69 and later include all of these changes; to update, see [Update Claude Science](https://claude.com/docs/claude-science/update-claude-science.md)
* [Auto mode](https://claude.com/docs/claude-science/auto-mode.md) is on by default wherever it's available to you: it lets Claude Science run code and call connectors without stopping to ask about every step. Turn it off for new sessions in **Settings > Permissions**, or for one session in its settings menu in the message box
* Auto mode: if **Auto mode on for new sessions** is off, then in the Windows app, or when Claude Science runs from a terminal or in a browser tab, turning auto mode on for a single session may not take effect until you quit Claude Science fully, reopen it and turn the session on again, usually once for each organization. To quit it fully, see [the steps in Troubleshoot Claude Science](https://claude.com/docs/claude-science/troubleshooting.md#environments-failed)
* Team and Enterprise: auto mode works only where it's allowed for your organization. Where it isn't, the **Auto mode on for new sessions** toggle is grayed out (point at it to see why), and Claude Science asks for approval as it does without auto mode
* A new **Trouble updating?** link opens [Update Claude Science](https://claude.com/docs/claude-science/update-claude-science.md), a help page with other ways to update. It shows in **Settings > General > About**, in the **Update required** box, and on the "Update available" notice while an update downloads or after one fails
* Cloud storage in Settings now works with Google Cloud Storage HMAC keys on computers where no AWS region is set
* Mac: if `config.toml` has `auto_update = false` under `[update]`, Claude Science in its own window no longer checks for updates in the background. You can still check with **Claude Science > Check for App Updates…** in the menu bar
* Linux: fixed updates from 0.1.66 or earlier failing with "restart aborted" when Claude Science was started by typing only `claude-science`
* Linux: if a folder you've granted **Read & write** holds a folder you can enter but not list (such as another person's folder on a shared drive), or a stale network mount, the code and commands Claude runs can now be refused, with a message that says how to fix it
* Bug fixes and reliability improvements

**0.1.68**

October 20, 2026

* **Export session** files now list the approval decisions made in the session from this version on: whether each action was approved, how it was settled, and when
* From this version on, when an update is required while sessions are running, you can stop them and update in one step, and resume them afterwards
* Mac and Linux: the starter Python and R environments, and the environments Claude Science sets up for connectors and compute providers, now keep their own downloaded packages. The first conda install into them after you update downloads packages again, so it needs a network connection and takes longer, and Claude Science can use about 3 GB more disk space
* After an update, the Example project lists the current examples and your own sessions. Examples from earlier versions are no longer listed unless you pinned them, moved them, or added your own messages to them. Nothing is deleted
* Bug fixes and reliability improvements

**0.1.67**

October 19, 2026

* The Example project now holds nine new example sessions from various scientific fields
* If Claude Science opens in its own window, on Windows or on a Mac, you can now search the page you're on with Ctrl+F (Cmd+F on a Mac)
* The Genomes connector's five UCSC Genome Browser tools and the Regulation connector's UniBind region lookup are unavailable for now
* Pictures in Claude's messages that point at another port or path of the address Claude Science is open on (such as localhost:8888) no longer load; save them as files to show them
* Files whose names Windows treats as shortcuts or themes (.url, .website, .lnk, .pif, .library-ms, .searchConnector-ms, .theme, and desktop.ini) are now downloaded and exported with .txt added to the name. If you trust the file, remove .txt from its name to get the shortcut back
* Leaving setup without starting a first task no longer leaves an empty "Getting started" project behind (if the app reloads or restarts during setup, the empty project can still remain)
* Linux: Claude's requests to delete an ordinary file in a folder you've granted are no longer refused while a session is running just because a protected file such as `.env` sits deeper in the same folder
* Bug fixes and reliability improvements

**0.1.66**

October 18, 2026

* Bug fixes and reliability improvements

**0.1.63**

October 14, 2026

* Tabs in the right pane are now all one width, and the tab you're viewing always shows its close button
* Newly saved artifacts now list more of their input files in Provenance when the code that created them read many files
* Linux: Claude Science now detects an NVIDIA GPU only if `nvidia-smi` can run without your `LD_LIBRARY_PATH` and is in `/usr/bin` or one of a few other fixed folders (`/usr/local/bin` isn't one). Otherwise the app finds no GPU, and the **Host GPU** switch in **Settings > Compute** is hidden unless it's already on
* Linux: a uv, conda, mamba, or pixi environment in a folder you've granted is now read-only to Claude when its files are shared with the tool's package cache (the usual case). Claude can still run code from it but can't add, update, or remove packages in it. The rest of the folder usually stays writable
* Various bug fixes and security improvements

**0.1.62**

October 13, 2026

* Linux: if Claude Science won't start after updating to 0.1.61, run `claude-science update` in a terminal to get 0.1.62 or later, then start it again. If it's still running and the "Update available" notice shows "restart aborted", select "Check for updates" in **Settings > General > About** so it finds the newer version, then "Restart to update"
* Linux: Claude Science starts again when bubblewrap or socat comes from conda, Homebrew, or a folder in your home directory. 0.1.61's requirement that both be installed for the whole system is withdrawn for now, though installing them that way is still recommended
* Fixed the app sometimes becoming unresponsive after Claude saves results from an analysis that read large files
* Various bug fixes and security improvements

**0.1.61**

October 13, 2026

* Sessions you start in the Example project now show on the home screen
* A GitHub token you paste in **Settings > Credentials** now stays after a restart, instead of switching back to the token found on your computer; if yours switched back, paste it again
* Linux: fixed Featured connectors that run on your computer sometimes failing to start right after your first sign-in
* Linux: Claude Science now needs bubblewrap and socat installed for the whole system, from your distribution's packages or by an administrator. If yours came from conda, Homebrew, or a folder in your home directory, the app refuses to start and its message says what to do
* Windows: Claude Science is now signed with a renewed certificate from the same publisher, Anthropic, PBC. If your IT team allows the app by certificate thumbprint, add the new SHA-1 thumbprint `60C2D9C51F09822FFF4F194DE9EEDB67451292D1` and keep the previous one, both listed under [Windows signing certificate](https://claude.com/docs/claude-science/manage-on-devices.md#windows-signing-certificate)
* Security hardening of the analysis sandbox on Mac, Windows, and Linux
* Various bug fixes and security improvements

**0.1.60**

October 7, 2026

* Mac: fixed a problem introduced in 0.1.59 where Python, R, and some shell commands could fail to run when Claude Science has access to many folders
* **Settings > Network > Package mirror** now shows a mirror credential file your organization deployed, instead of asking for a token

**0.1.59**

October 6, 2026

* Saved approvals for tools from your organization's plugins are cleared, so Claude asks again; new approvals apply only to the plugin that added the tool
* Skills from plugins your organization's admin uploads now appear under Organization in **Settings > Skills**, instead of under Featured
* Comment boxes on figures, PDFs, reports, and files now grow as you type, and a new comment that fails to save keeps your text and shows an error
* Fixed some files failing to upload when you add hundreds of files to a message at once
* `claude-science --here` now refuses to start on a data folder another install created if it holds organization policy files or folders that Claude Science creates for itself; if the folder is yours, run it once with `--trust-here-data`
* Security hardening of the analysis sandbox on Mac, Windows, and Linux
* Various bug fixes and security improvements

**0.1.56**

October 2, 2026

* When safeguards flag a message for life sciences content, Claude Science can now retry it once on another model automatically, depending on the model; turn this off with **Switch models when a message is flagged** in **Settings > General > Model**
* Excel (.xlsx) previews now show cell colors, bold text, and color-scale heat maps
* Reviewer findings now open in place, with a button to the reviewer's full transcript
* A stalled file upload now stops by itself, and a failed upload says why under the file
* Skills: "Check for updates…" now lists only the imported skills whose files changed
* Claude now asks before it uses a tool from a connector that your organization's plugins add
* Fixed a case where the app could delete a skill from your computer when it started
* Windows: zoom the app window with Ctrl+Plus and Ctrl+Minus, and reset it with Ctrl+0
* Windows: IT teams can now deploy package mirror credentials as a `.netrc` file, as on Mac and Linux
* Mac: the app now applies only a fixed list of variables from the `env` file in the data folder; move a GitHub token to **Settings > Credentials**
* Admins can now turn off Claude's web search tool with `enable_web_search = false` in `config.toml`
* Security hardening of the analysis sandbox on Mac, Windows, and Linux
* Various bug fixes and security improvements

**0.1.55**

September 29, 2026

* New sessions on an organization's default model with more life sciences restrictions now show a notice with a one-click switch to another model
* Fixed an error Claude ran into when outlining an existing multi-panel figure or drafting a paper's brief from its abstract and figure captions

**0.1.54**

September 28, 2026

* Sessions on Claude Sonnet 5.5 now default to Extra high reasoning effort
* Windows: after an update, the app window reopens on the new version by itself
* Pinned artifacts (formerly starred) and pinned projects now show a pushpin instead of a star
* Editing a Markdown table cell now outlines the cell itself instead of opening a box over it
* The app starts much faster with a long list of allowed domains
* Security hardening of the analysis sandbox on Mac, Windows, and Linux
* Various bug fixes and security improvements

**0.1.53**

September 24, 2026

* Paste a list of domains in **Settings > Network** to allow them all at once
* In Markdown files, editing table cells in place now works in files with up to 2,500 table cells, however long their text
* **Settings > Connectors**: a Featured connector that was turned off during setup now shows as off, and turning it back on lets Claude use it again
* Hover over a tab in the right pane to see the file's full name
* Mac: fixed a case where code cells didn't run because Claude wrote the folder's name in a different letter case or accent form than on disk
* Mac: security hardening of the analysis sandbox
* Various bug fixes and security improvements

**0.1.52**

September 22, 2026

* Clicking a figure in Claude's answer now opens it beside the chat; Ctrl/Cmd-click or the new "Open fullscreen" button opens it full screen
* Opening or closing the right pane now keeps your place in a long answer
* Markdown files no longer rotate in Safari after they load
* The reviewer no longer flags working figure links in saved reports as broken
* When Claude sets a Python, R, or shell cell to run in a folder other than the session's workspace, its permission card now shows that folder
* "Download script" and "Download notebook" now give the input and output files in the zip plain names: spaces, brackets, and other special characters become underscores
* Various bug fixes and security improvements

**0.1.51**

September 22, 2026

* Pinned sessions (formerly starred) from across all your projects now appear at the top of the session list; a new switch in **Settings > General > Appearance** lets you limit them to the open project
* In Markdown files, click a plain-text cell in a table to edit it in place
* Tables in Markdown files keep their scroll position when Claude saves another file
* Fixed the BioMart connector's data queries and identifier translation; a data query that filters on more than a few hundred IDs can still fail
* The BioMart connector now reads from Ensembl's June 2026 archive. If your network allowlist lists `www.ensembl.org` by name, add `jun2026.archive.ensembl.org`
* Removed connector tools that failed on every call: the ENCODE and eQTL Catalogue lookups and ZINC's random-sample tool
* "Download script" on an artifact made by a shell command now includes the script itself
* The app stays more responsive while Claude saves files in projects with tens of thousands of files, and zip downloads with thousands of same-named files are prepared much faster
* Mac: security hardening of the analysis sandbox
* Life Sciences Verification Program (beta): fixed a case where your approved use cases could disappear from the app
* Various bug fixes and security improvements

**0.1.50**

September 17, 2026

* Tables in Markdown files now show as a compact grid; a long table keeps its header row in view, and row labels stay in view when you scroll sideways
* Tabs in the right pane can be reordered by dragging, or with Ctrl/Cmd+Shift+Left/Right
* Pasted images are now saved to your uploads, so Claude can keep working with them later in the conversation
* When Claude redraws a figure several times in one turn, the chat keeps only the newest one open; open an earlier step to see its draft
* Closing Settings or Customize by clicking outside it no longer drops an edit you were still typing
* "View in context" on a file version that a different session saved now opens the file's own session instead of an empty screen
* Project settings are now clearer with helper text
* Home screen: project rows now show running sessions in gray like the session cards

**0.1.49**

September 16, 2026

* If your organization is in Anthropic's Life Sciences Verification Program (beta), you can now [choose a use case](https://claude.com/docs/claude-science/safeguards.md#choose-a-use-case) for your sessions
* Saved credentials now reach Claude's code only when it asks for them and you approve. They're no longer present in every cell
* Access Claude Science work saved on your computer from other sign-ins, from Home or Settings. Admins control it on Team and Enterprise plans
* Claude can send you a short message, such as a link to a file, while it keeps working on a task
* Mac: Apple silicon Macs with the Intel version installed can now update, and then run natively
* Mac: if Claude's tools can't start after an Xcode update, the error now says how to accept the Xcode license
* You can comment on and bookmark the short summaries of Claude's progress notes
* Sessions moved to a model with a smaller context window keep going instead of failing
* Turning Auto-review off now applies to agents that are already running; turning it back on resumes their reviews
* Settings > Connectors shows "Not set" for tools without a permission, and saves "Ask each time"
* Windows: `claude-science install` now reports the step that failed instead of reporting success
* Faster search of a long session's history; clearer wording in model settings

**0.1.48**

September 14, 2026

* On Windows, environment setup now handles user folders with accented or non-Latin names, tries again if Windows briefly refuses to start the environment installer, and no longer needs the Microsoft Visual C++ Redistributable
* The app now warns you a few days before your sign-in expires and offers a "Sign in again" button
* Various bug fixes and security improvements

**0.1.47**

September 10, 2026

* Claude Science is now available for Windows: download it from [claude.com/product/claude-science](https://claude.com/product/claude-science), and see [Get started](https://claude.com/docs/claude-science/get-started.md) for setup
* Various bug fixes and improvements

**0.1.43**

August 31, 2026

* On Linux, commands, notebook cells, and local connectors work again on systems with bubblewrap's recent security update
* Cloud storage in Settings (Amazon S3, S3-compatible services, and Google Cloud Storage with HMAC keys) now works behind a TLS-inspecting proxy such as Zscaler or Netskope, trusting the same corporate root certificate as sign-in and the Claude API
* Various bug fixes and security improvements

**0.1.41**

August 27, 2026

* Messages now show when they were sent: hover one of your messages to see the time, and Claude's replies show it next to their copy and feedback buttons
* Reviewer findings now appear as cards directly under the message they refer to, instead of a single summary card; click a card to open the reviewer's reasoning
* When a connector's sign-in expires mid-session, Claude now tells you which connector to reconnect, and Settings > Connectors shows "Sign-in expired" with a Reconnect button
* Choosing a model whose safeguards block most life sciences research now shows a short warning first, with a one-click switch to an alternative model
* Sessions on Claude Opus 5 now stay focused on what you asked for, with fewer unrequested analyses, figures, and sub-agents
* On macOS behind a TLS-inspecting proxy (such as Zscaler or Netskope), Python, pip, curl, and git inside a session now trust the same corporate root certificate that environment builds already use
* Tab-separated (.tsv) files open as tables, and the 3D structure viewer follows dark mode and opens small-molecule files (SDF, MOL2, XYZ, and similar) in stick view
* First-time setup now includes a memory step, with memory on unless you switch it off there; existing installs keep their current setting (change it anytime under Settings > Memory)
* Security hardening across the analysis sandbox and credential handling on macOS and Linux
* Lots of other miscellaneous improvements and fixes

**0.1.27**

August 7, 2026

* On macOS, installs that showed an environment setup error in their first session now repair themselves automatically after updating; the Featured connectors become available once the repair finishes, which can take a few minutes
* Star a session from its menu to keep it in a Starred section at the top of your project's session list
* Get notified when any of your sessions finishes or needs your input, even while you work in another project. In-app notifications are on by default; sound and desktop notifications are under Settings > General > Notifications
* Set reasoning effort for a single session from the session options next to the message box; the value in Settings stays the default for new sessions
* On Pro and Max plans, see your credit balance and monthly spend limit and turn usage credits on or off under Settings > Usage
* When you ask for a plan, Claude now waits for your approval before running code or marking steps done
* Lots of other miscellaneous improvements and fixes

**0.1.21**

July 21, 2026

**New**

* **Improved context preservation.** On Max, Team, and Enterprise plans, sessions go much further before older messages are summarized.
* **Works on corporate networks.** Sign in and install packages on networks with corporate proxies, TLS inspection, or authenticated package mirrors. Mirror credentials go in Settings. No config files needed.
* **Search your memories.** Find anything Claude remembers from the memory screen. Results are highlighted and jump to where they live. The screen also loads faster now.
* **Archive projects.** Tidy your project list without deleting anything; archived projects keep all their data and can be brought back anytime.
* **Password sign-in for SSH machines.** Adding a remote machine that asks for a password instead of a key is now supported. You're prompted when it's needed, and the password is never saved to disk.
* **Compute monitor.** See every running kernel with its memory and CPU use from the new Compute tab. Kernels can be stopped if needed with optional feedback sent to the agent such as "redo this analysis using less memory".

**Improvements and fixes**

* **Richer artifact previews.** HTML files show rendered thumbnails, Word documents show text previews, large CSVs show their structure, and PDFs show their first page.
* **Parquet files open as tables.** See a parquet file's columns and first rows right in the app, even for very large files.
* **Memories stay in their project.** Notes from one project no longer surface in another.
* **Annotations travel with your message.** Annotations you've added appear above the message box and carry over when you open a side chat.
* **Less disk space for huge files.** When Claude saves the same very large file over and over, it can now keep just the latest version instead of every copy.
* **The conversation view holds still.** Images no longer shove the page as they load, "View in context" lands on the right message, and mentioning a file always attaches the right one.
* **Edit messages with attachments.** Editing an earlier message now supports file mentions, attachments, and uploads.
* **Many other miscellaneous fixes and improvements.**

**0.1.18**

July 9, 2026

**Features**

* Sessions now pause and ask for your confirmation before spending extra usage. Billed usage credits are never drawn on a dismissible warning alone.
* Claude can now monitor how much memory and processing power its computations are using, and plan its work accordingly.
* Search from inside a project: the project view now has a search button that opens the same search as Cmd+K.
* Download any artifact from any surface: every artifact menu now includes a download option.
* Starred artifacts now pin to a new Starred section at the top of the Library, with a star badge.

**Fixes**

* Fixed a crash that could prevent very large sessions from loading.
* Fixed several ways a running session could stall or stop early, including long thinking pauses being cut off mid-run and sessions resuming incorrectly after a crash.
* Fixed the app sometimes becoming unresponsive after an automatic update.
* Code blocks now switch correctly when your system switches between light and dark mode.
* Lots of other miscellaneous improvements and fixes.

**0.1.17**

July 8, 2026

* **Fixed a bug where idle sessions were consuming usage.**
* Lots of other miscellaneous improvements and fixes.

**0.1.16**

July 7, 2026

**Features**

* Auto-review is now available on the Pro plan: turn it on from the session settings, and it stays off until you do.
* Artifact previews: zoom HTML artifacts (including fit to width), zoom images to native resolution, and choose which version an artifact diff compares against
* Import skills from private GitHub repositories using your own GitHub credentials
* LaTeX previews now resolve cross-references — \ref, \eqref, and section numbering render the way your document intended
* Dashboard upgrades: a project switcher with live per-project status, project names on the "Now" cards, a visible search button, and ⌘K search now matches project descriptions too
* Annotate artifacts faster: drag image annotation pins to reposition them, and use @/# mentions in annotation comments

**Fixes**

* Pasted attachments no longer disappear before their first use, very large text and JSON previews no longer freeze the tab, and a stale usage-limit banner now clears itself once your usage limit resets
* Cloning a repo or unpacking an archive no longer floods the chat with every image it contains
* The Reviewer no longer gets stuck on "Reviewing…" or hides its findings tray
* Flaky read-only connector tool calls now retry once automatically instead of failing your turn, and connector setup errors tell you what's actually wrong
* A corrupt pasted image no longer breaks the transcript
* Upgrading with a very large history database no longer fails partway through
* Fixed a crash when the browser's auto-translate feature modified the page
* Lots of other miscellaneous improvements and fixes

**0.1.15**

July 1, 2026

* Corporate networks: environment builds now work behind TLS-inspecting proxies (such as Zscaler or Netskope). On macOS, corporate root CAs in your keychain are picked up automatically for conda/pip package downloads; on macOS or Linux you can also point at a CA-bundle file under Settings > Network > Package mirror. The mirror card's Check button now verifies TLS trust with the same bundle the builds use. (In-session `pip`/`curl` and the Desktop app's guest-VM builds are not covered)
* Package mirrors: point conda and pip at your organization's internal mirror (Artifactory/Nexus) via Settings > Network > Package mirror. Setting a mirror also drops the public package hosts from the sandbox network allowlist
* OpenAlex now requires a free API key for full-text access. Claude Science resolves access automatically or asks you in the session when a key is needed; you can also add and validate a key anytime under Settings > Credentials
* New Context usage view: see how full a session's context window is and where tokens go, from the + menu in the composer
* Lots of other miscellaneous improvements and fixes

**0.1.14**

June 30, 2026

* Public launch of Claude Science
