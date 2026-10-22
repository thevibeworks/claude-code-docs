> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Auto mode

> Auto mode in Claude Science lets a safety check approve code and connector calls.

Auto mode in Claude Science lets Claude run code and call connectors without routine [permission cards](/docs/claude-science/core-concepts.md#permission-cards). A separate safety check reviews code, and the connector calls that would otherwise ask you, before they run. It approves the ones that look safe and holds anything that escalates beyond your request, is destructive or hard to undo, or appears driven by hostile content Claude read. Anything the check holds or can't check still shows you the card. Allow or deny the request as you would with auto mode off.

> [!WARNING]
>
> Auto mode in Claude Science reduces permission cards but does not guarantee safety. Use it for tasks where you trust the general direction, not as a replacement for review on sensitive operations.

## Turn auto mode on or off

Where auto mode is available to you, it starts on.

* **For new sessions**: go to **Settings > Permissions** and turn the **Auto mode on for new sessions** toggle off or on.
* **For the current session**: open the session settings menu in the message box and turn the **Auto mode** row on or off.

The **Auto mode on for new sessions** toggle also decides for sessions that don't have their own auto mode setting, such as sessions you started before Anthropic made auto mode available to you. A session with its own setting keeps it when you change the toggle, so turn auto mode off in that session from the session settings menu in the message box.

## What auto mode needs in Claude Science

Auto mode in Claude Science is available only when all of these requirements are met:

* **Sandbox**: the [sandbox](/docs/claude-science/core-concepts.md#sandbox) is on. With the sandbox off, auto mode approves nothing.
* **Organization**: on Team and Enterprise plans, your organization's admin allows it (see [Auto mode in Admin controls](/docs/claude-science/admin-controls.md#auto-mode)).
* **Availability**: Anthropic has made auto mode available to you in Claude Science.

If the toggle is missing or grayed out, one of these requirements is unmet.

## What auto mode checks

Auto mode in Claude Science checks code that Claude runs in the sandbox (Python, R, shell, and PowerShell cells) and calls to remote and directory connectors. A permission you saved for code cells doesn't skip the check while auto mode is on.

Everything else asks as it does with auto mode off. That includes network access, access to files outside the session's workspace folder, remote compute, Claude's package and environment tools, and any tool you set to **Ask each time**.

## What each check sends to Anthropic

Each check in Claude Science is a separate request to a Claude model at Anthropic and counts toward your usage. It includes the pending action in full and these parts of the conversation so far: your messages, Claude's questions with your answers, and each action Claude took. Each action still in the conversation is sent in full, such as the code Claude ran, the text it wrote to a file, a short message it sent you while it worked, or the instructions it wrote when it delegated part of the work. Claude's other replies and the output of those actions are left out, except where a summary of older parts of a long conversation restates them. When code runs anywhere but the top level of the Claude Science session's workspace folder, the request includes the full path of the folder the code runs in, which can include your computer's user name.
