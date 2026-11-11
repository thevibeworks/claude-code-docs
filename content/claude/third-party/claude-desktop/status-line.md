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
> * **A message that each user can close, on the start screen or in a dialog**: set the [`organizationAnnouncement`](https://claude.com/docs/third-party/claude-desktop/configuration#organizationannouncement) key
> * **Your own message when your gateway blocks a user at a spend limit**: see [Block requests at a spend limit](https://claude.com/docs/third-party/claude-desktop/gateway.md#block-requests-at-a-spend-limit)

## Turn on the status line

The status line requires Claude Desktop 4.4212.0 or later and is off until you set the [`sessionStatusLine`](https://claude.com/docs/third-party/claude-desktop/configuration#sessionstatusline) key.

**1. Install the program**

Put the program where users can't change it. Claude Desktop runs it only from a location that meets these rules:

* **macOS and Linux**: root owns the file and every parent folder, with no write access for group or others, and the path isn't under `/home`, `/net`, or `/Volumes`
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

If one configuration serves several operating systems, such as a bootstrap server's response, add `platformOverrides` with a `command` under `win32` (Windows), `darwin` (macOS), or `linux`. In a macOS profile, a Windows registry policy, or the [Linux configuration file](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#the-linux-configuration-file), set only `command`. Versions before 4.16336.0 reject the whole key and show no status line, so add `platformOverrides` only after every device has updated. The top-level `command` is required and runs on any system you don't list:

```json theme={null}
{
  "sessionStatusLine": {
    "command": "/opt/example/bin/status-line",
    "platformOverrides": {
      "win32": { "command": "C:\\Program Files\\Example\\status-line.ps1" }
    }
  }
}
```

**3. Restart Claude Desktop and check the line**

Quit and reopen Claude Desktop, then open an existing session, or start a new one and send a message. The line appears above the message box.

On Claude Desktop 4.16336.0 or later, if [`inferenceModelPricingEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencemodelpricingenabled) is also on, the status line replaces the "Session cost (estimate)" line.

## Write the status line program

Claude Desktop starts the status line program with no arguments and no window, as the user who runs Claude Desktop.

* **File type**: on macOS and Linux, an executable file, such as a compiled program or a script that starts with `#!`. Claude Desktop doesn't check the interpreter that a `#!` line names, so install it where users can't change it too. Python also runs code from the user's folders unless you start it with `-I`, for example `#!/usr/bin/python3 -I`. On Windows, an `.exe` file or a `.ps1`, `.cmd`, or `.bat` script.

* **Input**: one line of JSON on standard input, with the session ID, the model, and the [session cost](#session-cost-in-the-status-line-input). A field with no value is left out, so handle a missing `model` or `cost`. Later versions can add fields, so ignore any that the program doesn't use. Don't build a file path from these values.

  ```json theme={null}
  {"session_id":"local_1f0c2a9e-7b3d-4c58-9a16-5e2d8b40c7f3","model":{"id":"claude-sonnet-4-5","display_name":"Claude Sonnet 4.5"},"cost":{"total_cost_usd":1.24}}
  ```

* **Output**: the first non-empty line of standard output, read as UTF-8, up to 200 characters. Markup and links show as plain text. A line wider than the message box ends in "…" and shows in full on hover.

* **Colors**: text is gray by default. ANSI codes `31` to `36` and `91` to `96` show red, green, yellow, blue, magenta, and cyan, and `0` or `39` returns to gray. Other colors show gray, and codes such as bold have no effect.

* **Paths**: the working directory is `/` (`System32` on Windows). `PATH` is `/usr/bin:/bin:/usr/sbin:/sbin`, or the System32, Windows, and Windows PowerShell folders on Windows, so call other tools by their full path.

* **Environment**: the app's variables, minus `ANTHROPIC_*`, `CLAUDE_*`, `ELECTRON_*`, `GIT_*`, and variables that change which code a program loads, such as `PYTHONPATH` or `LD_LIBRARY_PATH`.

* **Time limit**: 10 seconds, after which Claude Desktop stops the program and anything it started.

### Session cost in the status line input

`cost.total_cost_usd` is the session's estimated cost so far. Claude Desktop sends it only while [`inferenceModelPricingEnabled`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencemodelpricingenabled) is on and the session has an estimate. The value is a number in US dollars with up to six decimal places and no exponent. It's for display only and can differ from your provider's bill.

* **Source**: Claude Desktop's own sum for the session, added up on the user's device. It covers Cowork, Chat, and Code sessions, including [Code sessions over SSH](https://claude.com/docs/third-party/claude-desktop/ssh-remote-sessions.md). With no status line set, the built-in "Session cost (estimate)" line above the message box shows the same sum.
* **Models with no price**: a model ID that can't be matched to a Claude model, such as an opaque gateway alias, adds nothing. After you give that ID a rate in [`inferenceModelPricing`](https://claude.com/docs/third-party/claude-desktop/configuration#inferencemodelpricing), only its later usage counts. The input doesn't show that the sum is partial.
* **Missing `cost`**: don't show \$0. Check for each of these causes:
  * `inferenceModelPricingEnabled` is off
  * The session has no priced estimate yet, such as before Claude Desktop records its first turn's cost or when it has used only models with no price
  * Claude Desktop [couldn't read its usage ledger](#troubleshoot-a-missing-status-line), the local record of these estimates
* **Scripts written for Claude Code**: [Claude Code's status line](https://code.claude.com/docs/en/statusline) always sends `cost`, among many other fields. Claude Desktop sends only the fields in the [sample input](#write-the-status-line-program), so check a script that you carry over for other fields and for a fallback to 0. Claude Desktop's sum can also differ from Claude Code's total, for example after `/clear`.

This macOS and Linux script prints the cost. While `cost` is missing it prints nothing, so no line shows:

```sh theme={null}
#!/bin/sh
# Prints, for example: Session cost (estimate): $1.24
LC_ALL=C
export LC_ALL
cost=$(sed -n 's/.*"total_cost_usd":\([0-9.]*\).*/\1/p')
[ -n "$cost" ] || exit 0
printf 'Session cost (estimate): $%.2f\n' "$cost"
```

### Status line scripts on Windows

A `.ps1` script runs in Windows PowerShell, not PowerShell 7.

* **Execution policy**: if Group Policy allows only signed scripts, sign the `.ps1` script with a certificate that each device trusts, and add it to each device's Trusted Publishers store. If Group Policy turns scripts off, use a `.cmd` or `.exe` file.
* **Encoding**: a script must print UTF-8, or characters outside ASCII can show as "�" or "?". In a `.ps1` script, set UTF-8 output in the first statement, as the [Windows sample](#sample-status-line-programs) does, and save the file as UTF-8 with BOM. In a `.cmd` or `.bat` script, put `chcp 65001 >nul` right after `@echo off`, and save the file as UTF-8 without BOM.

### Sample status line programs

Both samples print a budget line, `■■■■■■■■□□ 82% of $500 used this month`.

> [tab] macOS and Linux
>
> ```sh theme={null}
> #!/bin/sh
> # Prints, for example: ■■■■■■■■□□ 82% of $500 used this month
> # Your own scheduled job keeps this file up to date. It holds dollars used and
> # the limit as two whole numbers, for example: 410 500
> BUDGET_FILE=/opt/example/budget.txt
>
> # Unless the file holds two whole numbers, print nothing so no line shows.
> [ -r "$BUDGET_FILE" ] || exit 0
> read -r used limit < "$BUDGET_FILE"
> case "$used" in ''|0?*|*[!0-9]*) exit 0 ;; esac
> case "$limit" in ''|0*|*[!0-9]*) exit 0 ;; esac
>
> percent=$((used * 100 / limit))
> if [ "$percent" -ge 90 ]; then color=31      # red
> elif [ "$percent" -ge 70 ]; then color=33    # yellow
> else color=32                                # green
> fi
>
> full="" empty=""
> for step in 10 20 30 40 50 60 70 80 90 100; do
>   if [ "$percent" -ge "$step" ]; then full="${full}■"; else empty="${empty}□"; fi
> done
>
> printf '\033[%sm%s\033[0m%s \033[%sm%s%%\033[0m of $%s used this month\n' \
>   "$color" "$full" "$empty" "$color" "$percent" "$limit"
> ```

> [tab] Windows
>
> ```powershell theme={null}
> # Print UTF-8, so that characters outside ASCII show correctly.
> [Console]::OutputEncoding = New-Object Text.UTF8Encoding $false
>
> # Read the session data, one line of JSON. Use fields such as $session.model.display_name.
> $line = [Console]::In.ReadLine()
> $session = $line | ConvertFrom-Json
>
> # Fixed numbers keep the sample short. Replace them with your own budget data.
> $esc = [char]27
> $yellow = $esc + '[33m'
> $reset = $esc + '[0m'
> $full = ([string][char]0x25A0) * 8
> $empty = ([string][char]0x25A1) * 2
> $bar = $yellow + $full + $reset + $empty
> Write-Output ($bar + ' ' + $yellow + '82%' + $reset + ' of $500 used this month')
> ```

## When the status line updates

Claude Desktop runs the status line program at these moments:

* A session opens
* Claude finishes a turn
* A turn's result arrives
* The user picks another model
* The app regains focus

There's no timer, so new data shows the next time one of these happens.

A turn's result closes the turn, and Claude Desktop doesn't add the turn to the [session cost](#session-cost-in-the-status-line-input) until the result arrives. That can be seconds after Claude's answer ends, for example when a [Stop hook](https://code.claude.com/docs/en/hooks#stop) runs first. The program can then run twice for the turn, and the first run's `cost` may not include the turn yet.

If the program exits with a code other than 0, prints nothing, or takes longer than 10 seconds, the line disappears and the user sees no error. The next successful run brings the line back.

## Troubleshoot a missing status line

Search `main.log` in the [logs directory](https://claude.com/docs/third-party/claude-desktop/data-storage.md#where-data-lives) on the user's device for `sessionStatusLine`. Claude Desktop doesn't log every failure of the same kind, so restart it after each fix. The entries don't include the program's output.

* **`Failed to parse managed config`** or **`was not applied`**: Claude Desktop rejected the whole key. A `Failed to parse` entry says what is wrong. A version before 4.16336.0 logs `sessionStatusLine.platformOverrides ignored`, so update that device.
* **`was not run`**: fix the cause the entry gives, such as a folder that users can write to or a Windows path outside `Program Files`
* **`ended with exit code`**: any code other than 0 hides the line, even if the program printed one
  * **macOS and Linux**: code 127 means that a command the script runs wasn't found, so call each tool by its full path
  * **Windows**: a `.ps1` script that an [execution policy](#status-line-scripts-on-windows) blocks ends with code 1
* **`was stopped after 10 seconds`**: the program hit the [time limit](#write-the-status-line-program). On Windows, a `.ps1` script can be slow to start for a few minutes after a user first opens Claude Desktop, and a `.cmd` or `.exe` file starts faster. If the line appears after a later turn ends or the app regains focus, nothing needs fixing.
* **`runs without the session's cost`**: Claude Desktop couldn't read its usage ledger, the local record of cost estimates, so the program ran with no `cost` in its input. The entry gives the cause. If `cost` comes back after a later turn ends or the app regains focus, nothing needs fixing.
* **No entry**: the program printed nothing, which isn't logged, or the key hasn't reached the app. Restart Claude Desktop and check [which configuration source applies](https://claude.com/docs/third-party/claude-desktop/configuration-format.md#which-configuration-source-applies-on-a-device).

To see the program's own error messages, run it in a new terminal window with Claude Desktop's working directory and `PATH`:

> [tab] macOS and Linux
>
> ```bash theme={null}
> cd /
> echo '{"session_id":"test","cost":{"total_cost_usd":1.24}}' | env -i HOME="$HOME" PATH=/usr/bin:/bin:/usr/sbin:/sbin /opt/example/bin/status-line
> echo "exit code: $?"
> ```

> [tab] Windows
>
> Paste these lines into PowerShell. They start a `.ps1` script with Claude Desktop's options and module path:
>
> ```powershell theme={null}
> Set-Location "$env:SystemRoot\System32"
> $env:PATH = "$env:SystemRoot\System32;$env:SystemRoot;$env:SystemRoot\System32\WindowsPowerShell\v1.0"
> $env:PSModulePath = "$env:SystemRoot\System32\WindowsPowerShell\v1.0\Modules;$env:SystemRoot\System32\WindowsPowerShell\v1.0\Modules"
> '{"session_id":"test","cost":{"total_cost_usd":1.24}}' | powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "C:\Program Files\Example\status-line.ps1"
> "exit code: $LASTEXITCODE"
> ```
