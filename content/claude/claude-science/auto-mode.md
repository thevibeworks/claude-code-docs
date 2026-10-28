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

Where available, auto mode is enabled by default for Pro, Max, and Team plans and off by default for Enterprise plans unless your organization's admin allows it.

* **To set your default for new sessions**: go to **Settings > Permissions** and turn the **Auto mode on for new sessions** toggle off or on.
* **To turn auto mode on or off for the current session**: open the session settings menu in the message box and turn the **Auto mode** row on or off.

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

Even when auto mode is on, Claude Science still asks permission for:

* Network access
* Access to files outside the session's workspace folder
* Remote compute
* Claude Science's package and environment tools
* Any tool you set to **Ask each time**
