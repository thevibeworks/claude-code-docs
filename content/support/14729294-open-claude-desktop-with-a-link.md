# Open Claude Desktop with a link

Claude for macOS, Windows, and Linux respond to the `claude://` URL scheme, much like a browser responds to the `https://` scheme. You can use these links from a website, a script, or another app to open Claude Desktop and jump straight to a chat, a Cowork session, or a Code session.

This article lists the link formats Claude Desktop supports and the parameters each one accepts.

## How deep links work

When your operating system opens a `claude://` URL, it hands the URL to Claude. If the app isn't running, macOS, Windows, and Linux will launch it first. Claude then reads the path and query parameters and navigates to the right place inside the app.

All parameter values must be URL-encoded. Prompt text passed in `q` is truncated to roughly 14,000 characters.

---

## Start a new chat

```
claude://claude.ai/new
claude://claude.ai/new?q=Summarize%20this%20week%27s%20release%20notes
```

Opens a new chat in Claude Desktop. If you include `q`, the prompt field is prefilled with that text so you can review and send it.

| **Parameter** | **Required** | **Description**                      |
| ------------- | ------------ | ------------------------------------ |
| `q`           | No           | Text to prefill in the prompt field. |

---

## Open an existing chat or project

```
claude://claude.ai/chat/{conversation-id}
claude://claude.ai/project/{project-id}
```

Opens a specific chat or project by its ID. The ID is the UUID you see at the end of the chat or project URL in Claude. If the ID is missing or invalid, Claude opens your recent chats or your projects list instead.

---

## Start a Claude Code session

```
claude://code/new
claude://code/new?q=Fix%20the%20failing%20test&folder=%2FUsers%2Fme%2Frepo
```

Opens Claude Code in Claude Desktop with the composer prefilled. Use this for "Open in Claude Code" buttons in your own tools.

| **Parameter** | **Required** | **Description**                                                                                                                                              |
| ------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `q`           | No           | Text to prefill in the composer. prompt is accepted as an alias.                                                                                             |
| `folder`      | No           | Absolute path to use as the working directory. Claude Desktop asks you to confirm the folder before it's used. Only the first folder value is applied today. |
| `file`        | No           | Absolute path to a file to attach. Accepted but not currently supported.                                                                                     |

**Note:** Any folder supplied through a link is treated as untrusted. Claude Desktop always shows a confirmation dialog before adopting it as the working directory, even if you've trusted that folder before.

---

## Start a Claude Cowork session

```
claude://cowork/new
claude://cowork/new?q=Draft%20the%20Q2%20update&folder=%2FUsers%2Fme%2Fdocs&file=%2FUsers%2Fme
%2Fdocs%2Fnotes.md
```

Opens a new Cowork session with the composer prefilled. Use this for "Open in Claude Cowork" buttons in your own tools.

| **Parameter** | **Required** | **Description**                                                                                                                                     |
| ------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `q`           | No           | Text to prefill in the composer.                                                                                                                    |
| `folder`      | No           | Absolute path to a folder to attach. Repeat the parameter to attach more than one. Claude Desktop asks you to confirm each folder before it's used. |
| `file`        | No           | Absolute path to a file to attach. Repeat the parameter to attach more than one.                                                                    |

**Note:** Any folder supplied through a link is treated as untrusted. Claude Desktop always shows a confirmation dialog before adopting it as the working directory, even if you've trusted that folder before.

---

## Test a deep link

### On macOS

Open Terminal and run:

```
open "claude://claude.ai/new?q=Hello"
```

### On Windows

Open Command Prompt and run:

```
start "" "claude://claude.ai/new?q=Hello"
```

### On Linux

Open a terminal and run:

```
xdg-open "claude://claude.ai/new?q=Hello"
```