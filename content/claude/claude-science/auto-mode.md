> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Auto mode

> Auto mode lets Claude Science run code and call connectors without stopping to ask about every step.

Auto mode lets Claude Science run code and call connectors without stopping to ask about every step. Instead, Claude Science reviews these actions for safety (such as checking for data exfiltration or [prompt injection](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)) and automatically blocks anything it determines to be unsafe. When an action is blocked, Claude Science pauses and asks you directly. If Claude Science keeps running into blocks, it switches back to asking your permission for each step.

> [!WARNING]
>
> No defense is perfect and no mode replaces your judgment. For work with real consequences, such as handling important files, stay close and review what Claude Science does, or consider turning auto mode off.

## Turn auto mode on or off

Where available, auto mode is enabled by default for Pro, Max, Ultra, and Team plans and off by default for Enterprise plans. Once an Enterprise admin enables auto mode, it will automatically become the default for all employees in the org.

* **You can adjust the default for new sessions** by going to **Settings > Permissions** and toggling **Auto mode on for new sessions** to your preferred setting.
* **You can adjust the default for the current session**, by opening the session settings menu in the message box and toggling **Auto mode** to your preferred setting.

The **Auto mode on for new sessions** toggle also turns auto mode on and off in your older sessions, from before you had auto mode. A session with its own setting keeps it until you change the Auto mode row in that session's settings menu.

## What auto mode needs in Claude Science

Auto mode in Claude Science is available only when all of these requirements are met:

* **Sandbox**: the [sandbox](https://claude.com/docs/claude-science/core-concepts.md#sandbox) is on. With the sandbox off, auto mode approves nothing.
* **Organization**: on Team and Enterprise plans, your organization's admin allows it (see [Auto mode in Admin controls](https://claude.com/docs/claude-science/admin-controls.md#auto-mode)). If your role is set to **Custom**, one of your custom roles must also include it.
* **Availability**: Anthropic has made auto mode available to you in Claude Science.

If the toggle is missing or grayed out, one of these requirements is unmet.

## What auto mode checks

Auto mode in Claude Science checks:

* Code that runs in the sandbox (Python, R, shell, and PowerShell cells)
* Code you've already allowed
* Calls to remote and directory connectors that would otherwise ask you

In auto mode, Claude can save most source code to your **Read & write** folders without asking, and auto mode doesn't check it. Claude Science can still ask about some files.

Even when auto mode is on, Claude Science still asks permission for:

* Network access
* Folder access you haven't granted, except [what sandbox rules let code read or write](https://claude.com/docs/claude-science/core-concepts.md#sandbox)
* Saving some file types, such as shell scripts and archives, to your folders
* Deleting files in your folders
* Remote compute
* Claude Science's package and environment tools
* Any tool you set to **Ask each time**

When auto mode is off but [available to you](#what-auto-mode-needs-in-claude-science), Claude Science still checks already-allowed code that uses a saved credential, such as an API key, and asks on a card when unsure. If you don't answer and spend 10 straight minutes in another session, window, or app, or with the session off screen, Claude skips that code. Until you allow one of these cards, later such code in that session can be skipped too. These checks count toward your [usage](https://claude.com/docs/claude-science/overview.md#plans-and-usage).
