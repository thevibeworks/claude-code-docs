> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Desktop and filesystem access

> How Claude Desktop on 3P reads and writes files on the user's machine, and how to constrain it

Like [Cowork](https://claude.com/docs/cowork/overview.md) in standard Claude Desktop, Claude Desktop on third-party (3P) works directly with files on the user's computer. Users attach one or more **workspace folders** to a session; the agent can then read, create, and modify files anywhere inside those folders, and run code against them inside the sandbox VM.

## Workspace folder allowlist

Set [`allowedWorkspaceFolders`](https://claude.com/docs/third-party/claude-desktop/configuration#allowedworkspacefolders) in the managed configuration to restrict which paths users may attach as workspace folders. The [Configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration.md) covers where the managed configuration lives on each platform and how to deploy it.

| Value | Behavior |
| - | - |
| Unset | Unrestricted. Users can attach any folder they have OS-level access to, matching standard Claude Desktop. |
| `["~/Documents/Claude", "/Volumes/Shared/Projects"]` | Users may attach only folders **inside** one of the listed roots. |
| `[]` | No folders may be attached. The agent can still create files in its own sandbox scratch space, but cannot read or write the user's filesystem. |

A leading `~` expands to the user's home directory, so a single profile can express per-user roots like `~/Documents/Claude` across the fleet. A path may also reference one of a fixed set of environment-variable tokens, such as `%OneDrive%` or `%USERNAME%`, listed in the [configuration reference](https://claude.com/docs/third-party/claude-desktop/configuration.md#allowedworkspacefolders). An entry that references any other `%VAR%`, or a variable that is unset on the device, adds no folder.

Each entry is either a plain path string or an object with these fields:

| Field | Description |
| - | - |
| `path` | The folder path (required). Subfolders are included. |
| `mode` | `rw` (the default) or `ro`. The agent can view and search a read-only folder but cannot modify it in Cowork. In Code sessions other than SSH remote sessions, read-only applies to Claude's file tools only, and isn't enforced for shell commands. For SSH remote sessions, see [Read-only folders on the remote host](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md#read-only-folders-on-the-remote-host). |
| `isDefaultSelected` | When `true`, the folder appears already selected on the new-task page and skips the trust prompt. Users can remove it. |

For example, `[{"path": "~/Documents/Claude"}, {"path": "/Volumes/Shared/Reference", "mode": "ro"}]` lets users work in their own folder and consult the shared reference folder without changing it.

> [!WARNING]
>
> List the folders that users work in, such as `~/Documents/Claude`, rather than the home folder or a folder that contains it, such as `/Users`. The home folder holds SSH keys and shell startup files, and Claude can read every listed folder, whatever `mode` the entry sets. Setting `mode` to `ro` on a home folder keeps Claude from changing it in Cowork, but not in Code sessions.

The check is enforced against the **resolved** path, so symlinks and `..` traversal can't be used to escape an allowed root.

> [!NOTE]
>
> The allowlist controls what users can **attach**. Within an attached read/write folder, the agent can read and write every file the user's OS account can reach. Data outside the allowed roots can't be attached in Cowork. In Code sessions, Claude's file tools can't open it, apart from [plugin files](https://claude.com/docs/third-party/claude-desktop/code.md#plugin-files-under-allowedworkspacefolders) and, in a local session, Claude Code's own plan files.
>
> A Code session's shell commands are confined only by the sandbox described under [Code](https://claude.com/docs/third-party/claude-desktop/code.md#applied-as-managed-policy). Where it applies, they can change files only inside the roots and temporary locations but can still read outside them, except the locations that [`blockReadsOutsideWorkingDirectories`](https://claude.com/docs/third-party/claude-desktop/configuration#blockreadsoutsideworkingdirectories) hides if you set it. Where it does not apply (Windows devices, hosts without the sandbox dependencies), the allowlist does not confine them. There, `blockReadsOutsideWorkingDirectories` can only ask the user to approve shell commands that Claude Code recognizes as reading outside the working directories, or whose command lines it can't analyze.
>
> To let the agent read data in Cowork without changing it, list the folder with `mode` set to `ro`.

## Network drives on Windows

Users can attach a mapped network drive (for example, `Z:\`) as a workspace folder through the folder picker. Raw UNC paths (`\\server\share`) are not supported; map the share to a drive letter first.

What the agent can do on the network drive depends on whether the drive was mapped and reachable when the sandbox started:

* **Mapped and reachable at sandbox start:** the sandbox mounts the attached folder alongside local folders. File tools and shell commands both work.
* **Mapped later, or unreachable at sandbox start:** file tools still work, but shell commands cannot reach the drive. Copy the relevant files to a local folder before running a script or build against them.

The sandbox can stay running between sessions. A drive the user maps while the sandbox is already up falls into the second case until the sandbox next restarts. For an attached folder below a DFS link, file tools still work but shell commands can't reach the folder, even if the drive was mapped before the sandbox started. Copy the relevant files to a local folder before running a script or build against them.

The agent cannot attach a network-drive path on its own; only the user can, through the folder picker. This is a security boundary.

On macOS, network mounts under `/Volumes/` are treated as local folders.

## Removable drives on Windows

Users can attach a folder on a removable drive, such as a USB stick or an SD card, and file tools work there. The sandbox does not mount removable drives, so shell commands cannot reach them. Copy the relevant files to a local folder before running a script or build against them.

## WSL

You do not need Windows Subsystem for Linux (WSL) to run Claude Desktop or Cowork. On Windows, Cowork's sandbox runs on the operating system's built-in virtualization, which the [readiness check](https://claude.com/docs/third-party/claude-desktop/installation.md#check-device-readiness) verifies. There is no installation path inside WSL, so run the Windows app and work with WSL files from the Windows app.

Windows exposes a WSL distribution's filesystem as a UNC path (`\\wsl$\<distro>` or `\\wsl.localhost\<distro>`). Like any other raw UNC path, these cannot be attached as workspace folders directly. To attach files that live inside WSL as a workspace folder, map the share to a drive letter and attach the mapped drive, or copy the files to a local Windows folder. [Network drives on Windows](#network-drives-on-windows) describes what the agent can do on a mapped drive.
