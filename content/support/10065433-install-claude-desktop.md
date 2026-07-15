# Install Claude Desktop

The Claude desktop apps bring Claude's capabilities directly to your computer, allowing for seamless integration with your workflow.

## Availability

Claude Desktop is available on macOS, Windows, and Linux (beta). What you can do depends on your plan:

| **Feature**   | **Free** | **Pro** | **Max** | **Team** | **Enterprise** |
| ------------- | -------- | ------- | ------- | -------- | -------------- |
| Chat          | ✅        | ✅       | ✅       | ✅        | ✅              |
| Claude Code   |          | ✅       | ✅       | ✅        | ✅              |
| Claude Cowork |          | ✅       | ✅       | ✅        | ✅              |

## System Requirements

- macOS: macOS 11 (Big Sur) or higher

- Windows: Windows 10 or higher

- Linux: Ubuntu 22.04 LTS+ or Debian 12 (bookworm)+, on x64 or arm64

## Installation steps for mac OS and Windows

1. Visit the **[Claude downloads page](http://claude.ai/download)**.

2. Select the appropriate version for your operating system:

  - For Mac users, find **macOS** and click "Download."

  - For Windows users, find **Windows** and click "Download."

Once the download is completed:

1. Open the file to complete installation.

2. Launch Claude from your Applications folder (Mac) or Start menu (Windows).

3. Sign in with your account to get started.

## Installation steps for Linux

### Install using apt

On Linux, you can install Claude Desktop from Anthropic’s apt repository rather than as a downloaded .deb file so that updates arrive through your system's normal package updates rather than in-app.

1. On Ubuntu or Debian, open a terminal and run:
​

```
sudo curl -fsSLo /usr/share/keyrings/claude-desktop-archive-keyring.asc https://downloads.claude.ai/claude-desktop/key.asc
echo "deb [signed-by=/usr/share/keyrings/claude-desktop-archive-keyring.asc] https://downloads.claude.ai/claude-desktop/apt/stable stable main" | sudo tee /etc/apt/sources.list.d/claude-desktop.list
sudo apt update && sudo apt install claude-desktop
```

2. Launch Claude from your applications menu, or run `claude-desktop` from a terminal, and sign in.

**Keeping Claude Desktop up to date on Linux**

The app doesn't update itself. Updates arrive with your system's regular package updates (`sudo apt update && sudo apt upgrade`).

### Install using file download

**Note:** Downloading the .deb will not opt you into regular package updates. We highly recommend that you install using apt, or set up the apt repo using the steps above.

If you can’t install Claude Desktop using apt, you can install it by downloading a .deb file instead:

1. Visit the **[Claude downloads page](http://claude.ai/download)**.

2. Find the .deb for your architecture (x64 or arm64) and click "Download."

3. From the folder you downloaded the .deb file, run: `sudo apt install ~/Downloads/claude-desktop_amd64.deb`

4. Launch Claude from your applications menu (or run `claude-desktop`), then sign in.

### Verify the download on Linux (optional)

Verify the signing key fingerprint before trusting it:

1. Run: `gpg --show-keys /usr/share/keyrings/claude-desktop-archive-keyring.asc`

2. Confirm the output matches: `31DD DE24 DDFA B679 F42D 7BD2 BAA9 29FF 1A7E CACE`

### Current limitations when you use Claude Desktop on Linux

- Computer use isn't available.

- Dictation isn't available.

- Quick Entry, the global hotkey, works on X11. On native Wayland, it relies on your desktop's GlobalShortcuts portal.

---

## Desktop extensions

Desktop extensions transform how you connect Claude to your desktop applications and data. Similar to browser extensions, these secure, installable packages let you:

- **Connect Claude to your desktop apps with one click**: Install extensions that integrate with your local files, calendars, emails, and messaging apps.

- **Access a curated directory of extensions**: Browse verified extensions directly within Claude Desktop, including options like filesystem access and iMessage.

- **Enjoy enterprise-ready security**: Extensions use code signing, encrypted storage for sensitive data like API keys, and enterprise policy controls.

To explore desktop extensions, navigate to Settings > Extensions within the Claude Desktop app after installation.

**Note:** We’re building a directory of desktop extensions – if you’re a developer hoping to add an extension you built to the directory, complete our **[desktop extensions interest form](https://docs.google.com/forms/d/14_Dmcig4z8NeRMB_e7TOyrKzuZ88-BLYdLvS6LPhiZU/viewform?edit_requested=true)** to share more information with us.

Read more about desktop extensions in our **[Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)** article.

---

## Claude Cowork

Claude Cowork is available for all paid plans (Pro, Max, Team, Enterprise) using the Claude Desktop app on macOS, Windows, and Linux (beta).

Users on paid Claude plans can access Cowork in Claude Desktop. Cowork brings Claude Code's agentic capabilities to a visual interface, allowing you to hand off complex, multi-step tasks without using a terminal.

With Cowork, Claude can:

- Access your local files directly without manual uploads.

- Work on long-running tasks like research synthesis, file organization, and document generation.

- Coordinate parallel workstreams for complex projects.

- Deliver professional outputs like spreadsheets with working formulas and formatted presentations.

Cowork runs code in an isolated virtual machine on your computer. File reads and writes are limited to folders you connect, and network access follows your egress settings.

To learn more, see **[Get started with Cowork](https://support.claude.com/en/articles/13345190-get-started-with-cowork)**.

**Setup requirements for Claude Cowork on Linux**

Cowork on Linux has its own setup requirements. Cowork runs your tasks in a virtual machine on your computer. Before it can start, your machine needs:

- **Hardware virtualization (KVM).** Most computers support this, but it's sometimes turned off in firmware. If Cowork says virtualization isn't available, enable it in your BIOS or UEFI settings and restart.

- **Permission to use virtualization.** Add yourself to the KVM group, then log out and back in: `sudo usermod -aG kvm $USER`

- **QEMU and supporting packages.** Installing Claude with `apt install` pulls these in automatically.

  - If you installed the .deb file directly on x64, run `sudo apt install qemu-system-x86 ovmf virtiofsd`

  - On arm64, run `qemu-system-arm qemu-efi-aarch64 virtiofsd` instead.

- **About 25 GB of free disk space for the workspace image, and at least 8 GB of RAM.** The workspace uses 4 GB while it's running.