---
title: Connect to a Managed Agents session from your terminal
url: https://platform.claude.com/docs/en/cli-sdks-libraries/cli/sessions-connect
description: Attach the ant CLI to a Claude Managed Agents session to follow its transcript live, send messages, allow or deny tool calls, or open the session viewer in your browser.
---

`ant beta:sessions connect` attaches your terminal to an existing Claude Managed Agents [session](https://platform.claude.com/docs/en/managed-agents/sessions). It loads the session's transcript and follows it live as the agent works. You can also step in: send a message, interrupt the agent, or allow or deny a tool call that is waiting for approval. With `--web`, it opens the session in the Claude Console's session viewer in your browser instead.

The command requires version 1.32.0 or later of the CLI. To install or update the CLI and authenticate, see the [CLI quickstart](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/quickstart).

## Connect to a session

Pass the ID of a session in your workspace. You can copy it from the create response, from `ant beta:sessions list`, or from the Console.

```bash CLI
ant beta:sessions connect sesn_011CZkZAtmR3yMPDzynEDxu7
```

Without `--web`, the command needs an interactive terminal. In scripts, use `ant beta:sessions:events stream` and `ant beta:sessions:events send` instead. See [CLI scripting and automation](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/scripting).

Press Ctrl+C to detach. The session keeps running, and connecting again loads its full history.

## Follow and steer the session

The terminal view shows the conversation live: messages and tool calls, with each call's duration and outcome. A status bar shows whether the session is running, idle, or waiting for your approval. In [multiagent](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration) sessions, the view follows the session's primary thread, which includes the messages the coordinator exchanges with the agents it delegates to.

| Key                | Action                                                                                                                     |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Enter              | Send your input as a `user.message` event. Alt+Enter or Ctrl+J starts a new line.                                          |
| Esc                | Interrupt the agent while it's running (`user.interrupt`).                                                                 |
| Ctrl+O             | Show or hide detail: tool inputs and results, token usage, and status events. `--verbose` (`-v`) starts with detail shown. |
| Page Up, Page Down | Scroll through the transcript. Scrolling up pauses following; End resumes it.                                              |
| Ctrl+C             | Detach. Ctrl+D on an empty input line also detaches.                                                                       |

When a tool call is waiting for your approval, the input line changes to **Allow tool call?** This happens under an `always_ask` policy, or under `auto` when the server reaches no determination. Choose **Yes**, **No**, or **No, and tell the agent why**. The CLI sends your choice as a [`user.tool_confirmation`](https://platform.claude.com/docs/en/managed-agents/permission-policies#respond-to-confirmation-requests) event, with any reason you type as its `deny_message`.

If the session is `terminated` or deleted, the view is read-only.

## Open the session viewer in your browser

```bash CLI
ant beta:sessions connect sesn_011CZkZAtmR3yMPDzynEDxu7 --web
```

`--web` serves the Console's session viewer from a local server on `127.0.0.1`, prints its URL, and opens it in your browser. Add `--no-browser` to skip opening the browser. You can also send messages, interrupt the agent, and allow or deny a tool call from the browser. Unlike the terminal view, the browser viewer follows every thread of a multiagent session.

The URL can be opened once, within two minutes of being printed. Reloading that tab works, but to open the viewer anywhere else, run the command again. Your credentials never leave the CLI: the page sends requests only to the local `ant` process, which makes the API requests. The server runs until you press Ctrl+C.
