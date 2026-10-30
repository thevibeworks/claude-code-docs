> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Show a status line

> Show a status line above the message box in Claude Desktop on 3P: one line of your organization's own text, such as budget used, from a program you install

The status line is one line of your organization's own text, such as budget used or a data-handling label, above the message box in Cowork, Chat, and Code sessions. [Claude Desktop on third-party (3P)](https://claude.com/docs/third-party/claude-desktop/overview.md) runs a program that you install on the user's device and shows the first line the program prints.

![The Claude Desktop message box. Above it, right-aligned in small gray text, a ten-square bar and the words 82% of \$500 used this month. The first eight squares and the 82% are colored.](https://mintcdn.com/claude-ai/_XP3pgAHpW92TgGc/images/third-party/status-line-budget.png?fit=max\&auto=format\&n=_XP3pgAHpW92TgGc\&q=85\&s=1b85b3f879c80bb9cd03b7c192bf92fd)

A status line that shows budget use, with made-up data.

> [!NOTE]
>
> These cases are covered on other pages:
>
> * **A notice across the top of the app window, with no program to install**: set the [`banner`](https://claude.com/docs/third-party/claude-desktop/configuration#banner) key
> * **Your own message when your gateway blocks a user at a spend limit**: see [Block requests at a spend limit](https://claude.com/docs/third-party/claude-desktop/gateway.md#block-requests-at-a-spend-limit)

## Turn on the status line

The status line requires Claude Desktop 4.4212.0 or later and is off until you set the [`sessionStatusLine`](https://claude.com/docs/third-party/claude-desktop/configuration#sessionstatusline) key.

**1. Install the program**

Put the program where users can't change it. Claude Desktop runs it only from a location that meets these rules:

* **macOS and Linux**: root owns the file and every parent folder, with no write access for group or others
* **Windows**: the file is under `Program Files` or `Program Files (x86)` on the drive where Windows is installed

To try the [macOS and Linux sample](#sample-status-line-programs) on a test device, save it as `status-line` and run these commands in your terminal:

```bash theme={null}
sudo mkdir -p /opt/example/bin
sudo cp status-line /opt/example/bin/status-line
echo "410 500" | sudo tee /opt/example/budget.txt
sudo chown -R 0:0 /opt/example
sudo chmod 755 /opt/example /opt/example/bin /opt/example/bin/status-line
sudo chmod 644 /opt/example/budget.txt
```

**2. Set the key**

Set the key's `command` field to the program's full path, with no arguments or shell syntax:

```json theme={null}
{ "sessionStatusLine": { "command": "/opt/example/bin/status-line" } }
```

In JSON, double each backslash in a Windows path:

```json theme={null}
{ "sessionStatusLine": { "command": "C:\\Program Files\\Example\\status-line.ps1" } }
```

Add the key to the same [configuration source](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#which-configuration-source-applies-on-a-device) as your other keys.

* **macOS profile or Windows registry**: write the value as a [JSON string](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#value-types-in-a-profile-or-registry-policy)
* **Bootstrap server**: the key applies after the user approves it in a dialog, unless the device [trusts the server's values without prompting](https://claude.com/docs/third-party/claude-desktop/bootstrap.md#keys-that-require-user-consent)

**3. Restart Claude Desktop and check the line**

Quit and reopen Claude Desktop, then open an existing session, or start a new one and send a message. The line appears above the message box.

## Write the status line program

Claude Desktop starts the status line program with no arguments and no window, as the user who runs Claude Desktop.

* **File type**: on macOS and Linux, an executable file, such as a compiled program or a script that starts with `#!`. On Windows, an `.exe` file or a `.ps1`, `.cmd`, or `.bat` script. A `.ps1` script runs in Windows PowerShell, not PowerShell 7.

* **Input**: one line of JSON on standard input, with the session ID and the model. A field with no value is left out, so handle a missing `model`.

  ```json theme={null}
  {"session_id":"local_1f0c2a9e-7b3d-4c58-9a16-5e2d8b40c7f3","model":{"id":"claude-sonnet-4-5","display_name":"Claude Sonnet 4.5"}}
  ```

* **Output**: the first non-empty line of standard output, up to 200 characters. Markup and links show as plain text. A line wider than the message box ends in "…" and shows in full on hover.

* **Colors**: text is gray by default. ANSI codes `31` to `36` and `91` to `96` show red, green, yellow, blue, magenta, and cyan, in shades that fit the light or dark theme, and `0` or `39` returns to gray. Other colors show gray, and codes such as bold have no effect.

* **Paths**: the working directory is `/` (`System32` on Windows). `PATH` is `/usr/bin:/bin:/usr/sbin:/sbin`, or the System32, Windows, and Windows PowerShell folders on Windows, so call other tools by their full path.

* **Environment**: the app's variables, minus `ANTHROPIC_*`, `CLAUDE_*`, `ELECTRON_*`, and variables that make an interpreter load code, such as `PYTHONPATH`.

* **Time limit**: 10 seconds, after which Claude Desktop stops the program and anything it started. On Windows, the time PowerShell takes to start counts toward the limit.

### Sample status line programs

Both samples print a budget line, `■■■■■■■■□□ 82% of $500 used this month`. The macOS and Linux sample reads its numbers from a file that your own scheduled job keeps up to date. The Windows sample prints fixed numbers and shows how a PowerShell script prints UTF-8, reads the input, and writes the escape character.

**macOS and Linux**

```sh theme={null}
#!/bin/sh
# Prints, for example: ■■■■■■■■□□ 82% of $500 used this month
# Your own scheduled job keeps this file up to date. It holds dollars used and
# the limit as two whole numbers, for example: 410 500
BUDGET_FILE=/opt/example/budget.txt

# Unless the file holds two whole numbers, print nothing so no line shows.
[ -r "$BUDGET_FILE" ] || exit 0
read -r used limit < "$BUDGET_FILE"
case "$used" in ''|0?*|*[!0-9]*) exit 0 ;; esac
case "$limit" in ''|0*|*[!0-9]*) exit 0 ;; esac

percent=$((used * 100 / limit))
if [ "$percent" -ge 90 ]; then color=31      # red
elif [ "$percent" -ge 70 ]; then color=33    # yellow
else color=32                                # green
fi

full="" empty=""
for step in 10 20 30 40 50 60 70 80 90 100; do
  if [ "$percent" -ge "$step" ]; then full="${full}■"; else empty="${empty}□"; fi
done

printf '\033[%sm%s\033[0m%s \033[%sm%s%%\033[0m of $%s used this month\n' \
  "$color" "$full" "$empty" "$color" "$percent" "$limit"
```

**Windows**

```powershell theme={null}
# Print UTF-8, so that characters outside ASCII show correctly.
[Console]::OutputEncoding = New-Object Text.UTF8Encoding $false

# Read the session data, one line of JSON. Use fields such as $session.model.display_name.
$line = [Console]::In.ReadLine()
$session = $line | ConvertFrom-Json

# Fixed numbers keep the sample short. Replace them with your own budget data.
$esc = [char]27
$yellow = $esc + '[33m'
$reset = $esc + '[0m'
$full = ([string][char]0x25A0) * 8
$empty = ([string][char]0x25A1) * 2
$bar = $yellow + $full + $reset + $empty
Write-Output ($bar + ' ' + $yellow + '82%' + $reset + ' of $500 used this month')
```

## When the status line updates

Claude Desktop runs the status line program at these moments:

* A session opens
* Claude finishes a turn
* The user picks another model
* The app regains focus

There's no timer, so new data shows the next time one of these happens.

If the program fails, prints nothing, or takes longer than 10 seconds, the line disappears and the user sees no error. The next successful run brings the line back.

## Troubleshoot a missing status line

Search `main.log` in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) on the user's device for `sessionStatusLine`. One entry can stand for many failures of the same kind, and the entries don't include the program's output.

* **`was not run`**: fix the cause the entry gives, such as a folder that users can write to or a Windows path outside `Program Files`
* **`ended with exit code 127`**: a command that the script runs wasn't found, so call each tool by its full path
* **`was stopped after 10 seconds`**: the program hit the [time limit](#write-the-status-line-program). On Windows, a `.ps1` script can be slow to start in the first minutes after Claude Desktop first launches. If the line appears after a later turn ends or the app regains focus, nothing needs fixing.
* **No entry**: the program printed nothing, which isn't logged, or the key hasn't reached the app. Restart Claude Desktop and check [which configuration source applies](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#which-configuration-source-applies-on-a-device).
