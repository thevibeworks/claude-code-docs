> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Artifacts

> An artifact is a file Claude saves into the project: a figure, processed dataset, report, notebook, or other output.

An artifact is a file Claude saves into the project: a figure, processed dataset, report, notebook, or other output. Artifacts are stored on your computer in the app's data folder and persist until you delete them. Other files Claude writes during a session are temporary and are cleared a few hours after the session ends; ask Claude to save a scratch file if you want to keep it.

## Working with artifacts

Click a linked file in the conversation to open it in a tab beside the chat. HTML artifacts have zoom controls, including fit to width; images zoom up to their native resolution. Open **Files** in the sidebar for a searchable grid of every artifact in the project. From an artifact's menu you can: Open, Open beside session, **View in context**, **Provenance**, Versions, **Copy link**, **Star**, **Rename**, **Download**, or **Delete**. Renaming doesn't break links. **Delete** removes all versions permanently.

Files you attach or drop into the composer are listed under **Your uploads**.

To copy artifacts outside the app, use **Download** for a single file, or open the project's folder under \~/.claude-science and copy the files directly.

## Versions

When Claude saves the same filename again in the same session, the artifact gains a new version. You can also edit text-based artifacts (Markdown, code, plain text) directly: click **Edit content**, make changes, and **Save** to create a new version. Images, PDFs, HTML, and tables can't be edited in place.

When an artifact file is open, a version stepper and a diff toggle appear. In diff mode, you can choose which earlier version to compare against; the previous version is the default. Older versions are read-only; to restore one, ask Claude to save it again. Links Claude puts in the conversation point to the specific version that existed at the time.

## Provenance

Every artifact version records how it was made. Open **Provenance** from an artifact's menu to see five tabs:

* **Messages**: the conversation around the save.
* **Code**: a reproducible script, downloadable as a script or notebook.
* **Execution Log**: every command that ran.
* **Environment**: the environment name, language version, and every installed package with its version.
* **Review**: findings from [the reviewer](/docs/claude-science/the-reviewer).

The **Execution Log** is the authoritative record of what ran. If the **Code** tab and the log disagree, trust the log.

## Deleting artifacts

Deleting a session keeps its artifacts and their provenance. Deleting a project deletes all of its sessions, artifacts, and project-scoped memory.
