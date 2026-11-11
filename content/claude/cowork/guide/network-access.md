> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Network access for shell commands

> Which hosts the shell commands in a Cowork task can reach, and what works on package registries and GitHub.

When a Cowork task runs on your computer, Claude runs its shell commands in a virtual machine (VM). Your network settings decide which hosts those commands can reach. Some of those hosts are download-only in a task.

## What a task can reach

You'll find the settings in **Settings > Capabilities**. On Team and Enterprise plans, your admin sets them for the whole organization in **Organization settings > Capabilities**.

| Setting | Shell commands can reach |
| - | - |
| **Allow network egress** is off | `anthropic.com` and `claude.com` hosts |
| **Domain allowlist** is **None** | Those hosts, plus the domains under **Additional allowed domains** |
| **Domain allowlist** is **Package managers only** | The same, plus common package registries and `github.com` |
| **Domain allowlist** is **All domains** | Any host, unless your organization applied the [HIPAA configuration](https://claude.com/docs/cowork/hipaa-setup.md#limit-network-access-for-cowork-shell-commands) |

## Download-only hosts

If a task can reach these hosts, it can download from them, but uploads to them are blocked. This doesn't apply when **Domain allowlist** is **All domains**. To publish or push, [use a terminal on your own computer](#push-or-publish-from-your-own-computer).

| Host | Works | Blocked |
| - | - | - |
| `registry.npmjs.org`, `registry.yarnpkg.com`, `crates.io` | Package installs and `npm audit` | Publishing, unpublishing, and account changes |
| `github.com` | `git clone`, `git fetch`, and `git pull` over HTTPS | `git push`, other uploads, Git LFS, and SSH remotes (`git@github.com:`) |

If your organization deploys Claude Desktop with its own model provider, your admin's [list of allowed hosts](https://claude.com/docs/third-party/claude-desktop/web-tools.md#web-fetch) replaces these settings. In that case, Claude Desktop doesn't block uploads to these hosts.

These limits aren't a security boundary. Don't rely on them alone to keep data inside the VM.

## What a blocked command shows

The command fails, and its output usually says why. A `git push` prints this line:

```text theme={null}
remote: Cowork blocked this request: only git clone, git fetch and plain downloads from GitHub work here, not git push, other uploads or Git LFS. To push or upload, use a terminal on your own computer.
```

A publish command gets the message below. npm shows only its short form, `403 Package registry is download-only`.

```text theme={null}
Package registries are download-only inside Cowork: publishing, unpublishing and account changes are blocked. Run those commands in a terminal on your own computer.
```

Two errors don't say why. With an SSH remote, `git` reports a closed connection, for both fetch and push. Git LFS reports an `Authorization error`. To clone or fetch from an SSH remote, use its `https://github.com/` URL instead.

## Push or publish from your own computer

Ask Claude to make the changes in a folder you connected to the task. Then open a terminal on your own computer and go to that folder. Review the changes, then commit and push them or run the publish command yourself.

## Related

These pages cover related topics.

* [Organize work with projects](https://claude.com/docs/cowork/guide/projects.md) for the folders a task can read and write
* [Cowork overview](https://claude.com/docs/cowork/overview.md) for an introduction to Cowork
