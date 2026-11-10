> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Download files from your MCP App

> Save a file from your MCP App to the user's device with app.downloadFile. Handle the result, fix rejected requests, and avoid refused file types.

You can save a file, such as a CSV file or an image, from your [MCP App](https://claude.com/docs/connectors/building/mcp-apps/getting-started.md) to the user's device. For example, in a shopping list app, a user clicks an export button to save the list as a CSV file. Claude asks the user to confirm before the download starts.

Your app's UI runs in Claude in a sandboxed frame, where no download starts from an `<a download>` link, a `blob:` URL, or a `data:` URL. Send each export through [`app.downloadFile`](https://modelcontextprotocol.github.io/ext-apps/api/classes/app.App.html#downloadfile) instead.

> [!NOTE]
>
> This page is for developers whose MCP App already renders in Claude. If you don't have an MCP App yet, start with [Add an interactive UI to your MCP server](https://claude.com/docs/connectors/building/mcp-apps/quickstart.md).

## Send a file from a view

A view is one rendered instance of your app's UI in Claude.

To save a file, call `app.downloadFile` with the file's contents in the view's script. The user sees the **Download file** dialog, or **Download files** for several files. The dialog lists the files in your request, and the user clicks **Download** to start the download.

`app.downloadFile` requires `@modelcontextprotocol/ext-apps` 1.1.2 or later.

### Check whether Claude offers downloads

Claude doesn't offer downloads everywhere that your view can appear, so check each time a view starts. After `app.connect()` resolves, read `app.getHostCapabilities()?.downloadFile` in the view's script:

* **If `downloadFile` is set**: show your export control
* **If `downloadFile` isn't set**: offer the content another way, such as text that the user can copy

### Add an export button to a view

Send the download request when the user clicks a control in the view, while the view is on screen, so that the user expects the dialog.

To run this sample, add `<button id="export">` and an element with `id="status"` to the view's HTML. Clicks have no effect while a request is pending, and the user sees no button where Claude doesn't offer downloads:

```ts theme={null}
import { App } from "@modelcontextprotocol/ext-apps";

const app = new App({ name: "Shopping list", version: "1.0.0" });
await app.connect();

const button = document.querySelector("#export");
const status = document.querySelector("#status");

if (app.getHostCapabilities()?.downloadFile) {
  let waiting = false;
  button?.addEventListener("click", async () => {
    if (waiting) {
      return;
    }
    waiting = true;
    let message = "Download started.";
    try {
      const { isError } = await app.downloadFile(
        {
          contents: [
            {
              type: "resource",
              resource: {
                uri: "file:///shopping-list.csv",
                mimeType: "text/csv",
                text: "item,quantity\nmilk,2\n"
              }
            }
          ]
        },
        { timeout: 600_000 }
      );
      if (isError) {
        message = "The download didn't finish.";
      }
    } catch {
      message = "The download couldn't be confirmed.";
    }
    waiting = false;
    if (status) {
      status.textContent = message;
    }
  });
} else {
  button?.remove();
}
```

Open the view in Claude and click the button. The **Download file** dialog appears and lists `shopping-list.csv`.

### Build the `contents` of a download request

Put each file's data and name inside the request's `contents`, and don't include links:

* **File data**: use the `text` field for text and the `blob` field for binary data. Encode `blob` as standard base64 with no `data:` prefix.
* **Links**: omit `resource_link` items, because Claude doesn't fetch them for the view. If you send only `resource_link` items, Claude refuses the request. If you mix them with files, Claude can also refuse the request.
* **File name**: end `uri` with a name and an extension, such as `file:///report.csv`. The last path segment becomes the saved file's name.
* **Characters in the file name**: write a literal space instead of `%20`. Percent-encoding isn't decoded.
  * Characters such as `%`, `:`, `"`, `*`, `<`, `>`, `|`, `~`, and `\` become `_`.
* **Several files**: you can send several files in one request

### Send one download request at a time

Wait for the result of one request before you send the next. If you send a second request from the same view while the **Download file** dialog is open, one of the two requests [ends with `isError: true`](#handle-the-result-of-a-download-request).

## Handle the result of a download request

Read `isError` in the result of `app.downloadFile`:

* **`false`**: Claude started the download
* **`true`**: tell the user that the download didn't finish

You can't tell from the result which of these cases occurred:

* Claude refused the request
* The user canceled
* Claude closed the **Download file** dialog
* Claude couldn't start the download

If no dialog appeared, check the [file types that Claude refuses](#file-types-that-claude-refuses). If the promise rejects and you receive no result, catch the error and [find its cause](#troubleshoot-a-rejected-download-request).

## File types that Claude refuses

If you send a file whose name ends in an extension on Claude's blocked list, Claude refuses the file.

* **Blocked**: the list includes programs, installers, shortcuts, and some script types. Blocked extensions include `.exe`, `.bat`, `.js`, `.jar`, `.dmg`, and `.lnk`.
* **Saved after the user confirms the download**: other script types, such as `.py` and `.sh`

If Claude refuses one file in a request, it refuses the whole request. No dialog appears, and the result has `isError: true`.

## Troubleshoot a rejected download request

For failures outside [the `isError` cases](#handle-the-result-of-a-download-request), the promise from `app.downloadFile` rejects. Read the error's message and `code`.

### `Invalid params for ui/download-file`

The error's message includes this text when you send a malformed request. Causes include a `blob` that isn't [standard base64](#build-the-contents-of-a-download-request) and an item that has no `uri`.

### `Request timed out`

The error's message includes this text when the [MCP Apps SDK](https://modelcontextprotocol.github.io/ext-apps/api/index.html) stops waiting for a result, after 60 seconds by default. Claude sets no time limit on the **Download file** dialog. To wait longer, pass `timeout` in milliseconds in the second argument to `app.downloadFile`, such as `{ timeout: 600_000 }`.

After a timeout, the dialog can remain open with a working **Download** button. Don't tell the user that nothing was saved.

### Code `-32601`, `Method not found`

Claude doesn't offer downloads where this view appears. [Check `app.getHostCapabilities()?.downloadFile`](#check-whether-claude-offers-downloads) before you send the request.

## Next steps

* [Open external links from MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/external-links.md): take the user to a URL outside Claude
* [Design guidelines](https://claude.com/docs/connectors/building/mcp-apps/design-guidelines.md#interaction-patterns): decide which interactions belong in the app and which in the conversation
* [Troubleshoot MCP Apps](https://claude.com/docs/connectors/building/mcp-apps/troubleshooting.md): open developer tools to inspect the view's requests
