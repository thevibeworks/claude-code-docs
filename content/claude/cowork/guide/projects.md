> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Organize work with projects

> Group folders, instructions, and context into a Cowork project so Claude starts each session with the right setup.

A Cowork project collects everything Claude needs for a recurring area of work: the local folders to read and write, standing instructions, useful links, and a dedicated memory store. When you start a session inside a project, Claude is already set up with that context.

Projects live on your computer. They aren't synced to the cloud or shared with other people.

## What a project holds

Each project bundles the following, and you can change any of it after creation.

| Item               | Purpose                                                                               |
| ------------------ | ------------------------------------------------------------------------------------- |
| Description        | What the project is for; Dispatch reads it when choosing a project for a task         |
| Folders            | One or more local folders Claude can read and write inside this project's sessions    |
| Instructions       | Standing guidance applied to every session in the project                             |
| Links              | Reference URLs (documents, dashboards, repositories) Claude can consult               |
| Projects from Chat | Projects you made in Chat (claude.ai) whose knowledge this Cowork project can draw on |
| Memory             | A project-scoped memory store that persists across sessions                           |

## Create a project

Open **Projects** in the left navigation and choose the **+** button to start. You're offered three starting points.

<Steps>
  <Step title="Choose a starting point">
    Select **Start from scratch** to create an empty project with a new folder,
    **Import a project** to bring an existing claude.ai project into Cowork, or
    **Use an existing folder** to point at a folder you already work from.
  </Step>

  <Step title="Name and describe it">
    Give the project a name and a short description so you can tell it apart in
    the sidebar.
  </Step>

  <Step title="Add folders and instructions">
    Attach the local folders Claude should have access to, and write any
    standing instructions you want applied to every session.
  </Step>
</Steps>

You can attach more folders, links, or projects from Chat at any time from the project's settings.

## Work inside a project

Select a project in the sidebar to start a new Cowork session with that project's folders mounted and instructions applied. Files Claude creates land in the project's folders; what Claude learns during the session is saved to the project's memory for next time.

[Dispatch](/docs/cowork/guide/dispatch) can also route background tasks into a project, so long-running work picks up the same folders, instructions, and memory.

When you drag files or folders into a project, individual files are copied into the project's first folder and folders are mounted as additional project folders. Claude reads individual files up to 50 MB.

## Cowork projects and claude.ai projects

A Cowork project is not the same thing as a project on claude.ai. They're stored separately and have different capabilities.

|                          | Cowork project        | claude.ai project           |
| ------------------------ | --------------------- | --------------------------- |
| Lives                    | On your computer only | In your Claude account      |
| Holds local folders      | Yes                   | No                          |
| Shareable with teammates | No                    | Yes, on Team and Enterprise |

You can link a claude.ai project into a Cowork project so Cowork sessions can draw on its knowledge. Linking doesn't merge them; the claude.ai project stays where it is.

## Archive a project

Archiving removes the project from your list and deletes its metadata (name, instructions, links, memory). It does not touch the local folders you attached; your files stay exactly where they are on disk.

To archive, open the project's menu in the sidebar and choose **Archive**.

## Related

* [Run tasks in the background with Dispatch](/docs/cowork/guide/dispatch) to run work inside a project without watching each step
* [Install plugins](/docs/cowork/guide/plugins) to extend what Claude can do in a project's sessions
* [Cowork overview](/docs/cowork/overview) for how projects relate to sessions and Dispatch
