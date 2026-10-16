> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Science in its own window on macOS

> Keep working when Claude Science switches to its own window on a Mac: open, quit, and update it, and turn macOS permissions back on.

On a Mac, Claude Science can now run as its own app, in its own window, rather than in the browser. If yours opens in a browser tab, installing an update from inside Claude Science, such as with **Restart to update**, can switch it over. Installing an update doesn't switch a copy that another account on your Mac installed, such as one that your organization's device management installed. To check whether yours has switched, open Claude Science from your **Applications** folder after the update. If it still opens in a browser tab, it hasn't switched, and you keep using it as before.

<Note>
  To manage Claude Science on your organization's Macs, see [Manage Claude Science on devices](/docs/claude-science/manage-on-devices#macs-where-claude-science-opens-in-its-own-window).
</Note>

## What changes when Claude Science switches to its own window

After the update that switches it over, Claude Science opens in its own window. If it doesn't, open it from your **Applications** folder. Close any old browser tab, even one that still says Claude Science is restarting or that the restart failed.

Your projects, conversations, artifacts, and Python and R environments are all there, and you stay signed in. If a setting such as the theme, the default model, or your pinned projects looks different, set it again.

macOS asks again for some [permissions](#macos-permissions-for-claude-science), and you turn others, such as Full Disk Access, back on yourself.

## Use Claude Science in its own window

* **Opening and quitting**: open Claude Science from your **Applications** folder. Closing the window keeps Claude Science and any sessions running. To quit, press Command-Q, which stops running sessions unless you started Claude Science from Terminal with `claude-science serve`.
* **Updates**: Claude Science downloads updates by itself and installs them the next time you quit. To check for an update right away, choose **Claude Science > Check for App Updates…** in the menu bar.

## macOS permissions for Claude Science

macOS treats Claude Science in its own window as a different app from the browser version, so macOS asks again for some permissions, such as access to your Documents or Desktop folder. Dictation needs microphone access. If dictation doesn't work, see [Dictation](/docs/claude-science/troubleshooting#dictation) in Troubleshoot Claude Science.

Access you turned on yourself, such as Full Disk Access, doesn't carry over from the browser version. To turn it on again, go to **System Settings > Privacy & Security**, choose the kind of access, and turn on the **Claude Science** toggle. If **Claude Science** isn't listed, click the add button (+) and choose **Claude Science** in the **Applications** folder. Do the same if a **Claude Science** entry is already on but Claude Science still can't reach your files, because that entry can be the browser version's.
