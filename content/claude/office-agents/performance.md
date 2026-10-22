> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Performance and limits

> How Claude for M365 works with a busy Office app, the size limits to know, and what to do when Office slows down or stops responding.

Claude for M365 does its work inside your Office app. When a file has very
large ranges, many shapes, or heavy formulas, the app can slow down or stop
responding.<sup id="cite-ref-1-a">[\[1\]](#cite-note-1)</sup> This happens with any heavy task in Office, with
or without Claude.

## Office runs one step at a time

Claude sends each step to Office and waits for Office to finish it. While
Office is busy, other actions can stall too.<sup id="cite-ref-1-b">[\[1\]](#cite-note-1)</sup>

![Claude sends a step and waits. Office runs the step, for example a recalculation, a large read, or a big slide edit. At the wait limit, Claude reports a timeout, but Office is still running the step. The wait limit is 90 seconds for steps where Claude runs code, 5 minutes for other steps, and 2 minutes on the web. Stop and a timeout end Claude's wait, not the step Office already started.](https://mintcdn.com/claude-ai/_Xjykq_jOPUQ7vjH/images/office-agents/performance/perf-one-step.png?fit=max\&auto=format\&n=_Xjykq_jOPUQ7vjH\&q=85\&s=86e807e77450672873ddcbd4e16578d3)

Four habits reduce slowdowns.

* **Let each step finish**: do not click, type, edit, run macros, or start a
  data refresh while Claude works. If a refresh is already running, wait for
  it or stop it with Esc or Stop Refresh.<sup id="cite-ref-2">[\[2\]](#cite-note-2)</sup> If Office asks whether to
  keep running the add-in, continue.<sup id="cite-ref-3-a">[\[3\]](#cite-note-3)</sup>
* **Give Claude only what the task needs**: name the sheet and range, or
  copy the sheets you need into a new workbook.
* **Ask for large changes one step at a time**: split a big job into
  smaller requests.
* **Wait after a timeout**: let Office respond, save, then ask for a
  smaller step.

## Limits to know

These limits come from Claude for M365 and from Office itself.

| Limit | Value | What it means for you |
| - | - | - |
| Wait for a step where Claude runs code | 90 seconds | A heavy step can time out |
| Wait for other steps, such as writing cells | 5 minutes on the desktop, 2 minutes on the web | A heavy step can time out |
| Wait for a Word text edit | 30 seconds | A heavy edit can time out |
| Cells returned by one Claude read in Excel | 2,000 cells with data | Claude reads a large sheet in several steps |
| Cells Office reads from one range | 5,000,000<sup id="cite-ref-3-b">[\[3\]](#cite-note-3)</sup> | A larger read can fail |
| One request in Excel on the web | 5 MB<sup id="cite-ref-3-c">[\[3\]](#cite-note-3)</sup> | Large reads and writes can fail on the web |
| Command batches waiting in Office | 50<sup id="cite-ref-4-a">[\[4\]](#cite-note-4)</sup> | More batches cause errors |
| Workbook opened in a browser | Up to 100 MB, depending on your subscription<sup id="cite-ref-5">[\[5\]](#cite-note-5)</sup> | Open larger files in Excel on the desktop |
| Memory for 32-bit Excel | Up to 4 GB on 64-bit Windows<sup id="cite-ref-6">[\[6\]](#cite-note-6)</sup> | Use 64-bit Office for large workbooks |

## File size and risk

Sessions with larger files more often end with a step that never finished.
This is how Claude for M365 detects an Office crash, a force quit, or a
reload. Larger files also mean longer sessions. The chart is directional,
based on what Claude for M365 usage shows.

![Directional chart of risk by file size. In Excel, measured by total used cells across all sheets, risk is lowest under 1 million cells, higher from 1 to 5 million, and highest over 5 million. In PowerPoint, measured by slides, risk is lowest under 100 slides, higher from 100 to 199, and highest at 200 or more. The chart shows direction, not measured values.](https://mintcdn.com/claude-ai/_Xjykq_jOPUQ7vjH/images/office-agents/performance/perf-risk.png?fit=max\&auto=format\&n=_Xjykq_jOPUQ7vjH\&q=85\&s=c018954e584a7b8fe3712b69b226f106)

The risk rises steadily, without a sharp threshold. Treat the bands as guides.

| File | Works well | Higher risk, so narrow your requests | Use at your own risk |
| - | - | - | - |
| Excel, total used cells across all sheets | Under 1 million | 1 to 5 million | Over 5 million |
| PowerPoint, slides | Under 100 | 100 to 199 | 200 or more |

To estimate the total for a workbook, go to each sheet and press Ctrl+End to
move to its last cell.<sup id="cite-ref-7-a">[\[7\]](#cite-note-7)</sup> Multiply the number of the last row by the
number of the last column, then add the results for all sheets. A last cell
of Z100000 is column 26 and row 100,000, about 2.6 million cells. Formatting
on empty cells moves the last cell, so a sheet can count as larger than its
data.<sup id="cite-ref-7-b">[\[7\]](#cite-note-7)</sup>

A single sheet above 5 million cells also passes the limit for one Office
read.<sup id="cite-ref-3-d">[\[3\]](#cite-note-3)</sup>

## Limit what is open at once

Workbooks that you open in the same instance of Excel share one Excel
process, and each workbook has its own Claude pane.<sup id="cite-ref-8-a">[\[8\]](#cite-note-8)</sup> Every pane
sends its commands to that process. Office queues the command batches it
receives, up to 50 at a time.<sup id="cite-ref-4-b">[\[4\]](#cite-note-4)</sup> When the computer is short of CPU
or memory, the wait grows, and Excel can stall or crash.

![One Excel process contains three workbooks, each with its own Claude pane. The commands from all three panes go into a single command queue in the same process. The process runs on a computer with limited CPU and memory. When CPU and memory run short, waits grow and Excel can stall or crash. Keep only the files you need open.](https://mintcdn.com/claude-ai/_Xjykq_jOPUQ7vjH/images/office-agents/performance/perf-shared-process.png?fit=max\&auto=format\&n=_Xjykq_jOPUQ7vjH\&q=85\&s=524e1317ae5b08f66fe51b4dcf8373ae)

Other Office apps run in their own processes, but they share the same CPU and
memory. Office starts to monitor add-in memory when the device passes 80%
memory use.<sup id="cite-ref-3-e">[\[3\]](#cite-note-3)</sup>

* Close the files you are not working in.
* For large files, work in one file at a time.
* When Claude works across Office apps, ask it to finish in one app before it
  moves to the next. See [Work across M365 apps](/docs/office-agents/work-across-apps.md).
* If Excel runs out of memory with several workbooks open, open Excel in a new
  instance.<sup id="cite-ref-8-b">[\[8\]](#cite-note-8)</sup>

## Lighter files respond faster

A smaller used range and lighter formulas shorten the time Office needs for
each step.

### Make large workbooks lighter

Excel has built-in tools that show what makes a workbook heavy.

| Task | Where in Excel |
| - | - |
| See counts of cells, formulas, and objects | Review, Workbook Statistics<sup id="cite-ref-9">[\[9\]](#cite-note-9)</sup> |
| Remove formatting from empty cells | Review, Check Performance<sup id="cite-ref-10-a">[\[10\]](#cite-note-10)</sup> |
| Find hidden shapes and pictures | Home, Find & Select, Selection Pane<sup id="cite-ref-11-a">[\[11\]](#cite-note-11)</sup> |

Save a copy of the workbook before you run Check Performance. It removes
formatting from cells that look empty, including cells used for pixel
art.<sup id="cite-ref-10-b">[\[10\]](#cite-note-10)</sup>

If the workbook is still too large, copy the sheets you need into a new
workbook.<sup id="cite-ref-11-b">[\[11\]](#cite-note-11)</sup>

### Ask for formulas that calculate fast

Some formulas make Excel recalculate far more cells than others. Ask Claude
for these forms.

* **Conditional sums and counts**: SUMIFS, COUNTIFS, and AVERAGEIFS. They
  calculate much faster than array formulas.<sup id="cite-ref-12">[\[12\]](#cite-note-12)</sup>
* **Today's date**: TODAY in one cell, with other cells that refer to
  it.<sup id="cite-ref-11-c">[\[11\]](#cite-note-11)</sup>
* **Direct references**: cell references in place of OFFSET and INDIRECT,
  which recalculate at each recalculation.<sup id="cite-ref-13">[\[13\]](#cite-note-13)</sup>

### Pause calculation during large changes

Excel recalculates dependent formulas after every change. For large formula
changes, pause recalculation until Claude is done.

**1. Set calculation to manual**

On the Formulas tab, select Calculation Options, Manual.<sup id="cite-ref-14-a">[\[14\]](#cite-note-14)</sup>
The option Automatic except for Data Tables skips only data tables.
Ordinary formulas still recalculate after every change.

**2. Ask Claude for the changes**

Claude writes the formulas without a recalculation after each one.

**3. Recalculate**

Press F9 when Claude is done. In Manual mode, formula results stay out of
date until you press F9.

**4. Check the results**

Ask Claude to verify the formulas after the recalculation.

**5. Turn automatic calculation back on**

Select Calculation Options, Automatic.

> [!NOTE]
>
> Manual calculation applies to every open workbook in Excel on the desktop.<sup id="cite-ref-15">[\[15\]](#cite-note-15)</sup>
> In Excel on the web it applies only to the current workbook. In Manual mode,
> saving can recalculate the workbook.<sup id="cite-ref-14-b">[\[14\]](#cite-note-14)</sup>

### Make large presentations lighter

Large pictures and media make a presentation larger.<sup id="cite-ref-16-a">[\[16\]](#cite-note-16)</sup> Compress them
before you ask Claude for large changes.

| Task | Where in PowerPoint |
| - | - |
| Compress pictures | Picture Format, Compress Pictures, with "Apply only to this picture" cleared<sup id="cite-ref-16-b">[\[16\]](#cite-note-16)</sup> |
| Compress audio and video | File, Info, Compress Media, in PowerPoint on Windows<sup id="cite-ref-17">[\[17\]](#cite-note-17)</sup> |

Save a copy of the presentation before you compress. Deleting cropped picture
areas and discarding editing data cannot be undone.<sup id="cite-ref-16-c">[\[16\]](#cite-note-16)</sup>

Ask Claude to change a few slides at a time.

## When Office stops responding

Use this table when Office stops responding during a request.

| Situation | What to do |
| - | - |
| Claude waits on a step | Wait. Do not click repeatedly. |
| Claude reports a timeout | Wait until Office responds, save, then ask for a smaller step. The step can still be running in Office. |
| Office closes | Reopen the file and look for the Document Recovery pane.<sup id="cite-ref-18-a">[\[18\]](#cite-note-18)</sup> Start a new chat with a smaller request. |
| It happens often | Send your IT admin the transcript and the time of the problem. |

When something goes wrong, keep your work and the chat for your admin.

**1. Recover your work**

Reopen the app and look for the Document Recovery pane.<sup id="cite-ref-18-b">[\[18\]](#cite-note-18)</sup>
In Excel, you can also go to File, Info, Manage Document, Recover Unsaved
Workbooks.<sup id="cite-ref-19">[\[19\]](#cite-note-19)</sup>

**2. Download the chat**

In the Claude pane, select More options, then Download Transcript.

**3. Send it to IT**

Send the file and the time of the problem through your usual support
channel. The file contains your chat.

## Investigate a crash or hang

Windows, Office, and Claude each keep a record of what happened. Start with
the time of the problem, then check the records below in order. The Windows
and Office records exist on Windows only.

![Four sources of records, in order. First, the user: the time of the problem, which is the key to every record, and the transcript of what Claude was doing. Second, Windows only: Reliability Monitor with a daily crash and hang timeline, Event Viewer with event 1000 for a crash and 1002 for a hang, and Windows Error Reporting files for crashes and hangs. Third, Office: the Telemetry Log with add-in CPU and error events, which stays off until an admin enables it. Fourth, your collector: an OpenTelemetry trace for every user turn.](https://mintcdn.com/claude-ai/_Xjykq_jOPUQ7vjH/images/office-agents/performance/perf-where-to-look.png?fit=max\&auto=format\&n=_Xjykq_jOPUQ7vjH\&q=85\&s=d62ef0be87cdd199fb375df256ef2642)

### Collect the user's report

The time of the problem is the key to every other record. Ask the user for
the time, the Office app, and whether Office closed or stopped responding.

Then ask the user to select More options in the Claude pane, then Download
Transcript. The transcript shows what Claude was doing when the problem
started.

### Check Reliability Monitor

Reliability Monitor shows a daily timeline of app crashes and hangs. Use it
to confirm that the problem happened and to see how often it repeats.
Press Windows+R and run this command.<sup id="cite-ref-20">[\[20\]](#cite-note-20)</sup>

```text theme={null}
perfmon /rel
```

### Read Event Viewer

Event Viewer separates a crash from a hang. Open Event Viewer, select
Windows Logs, then Application. Look for events from `EXCEL.EXE`,
`POWERPNT.EXE`, `WINWORD.EXE`, or `OUTLOOK.EXE` near the time of the
problem.

* **Event 1000**: a crash. The event names the faulting module.<sup id="cite-ref-21">[\[21\]](#cite-note-21)</sup>
* **Event 1002**: a hang.<sup id="cite-ref-22">[\[22\]](#cite-note-22)</sup>

### Find Windows Error Reporting files

Windows Error Reporting keeps a report for each crash or hang. The reports
are in one of two folders.<sup id="cite-ref-23">[\[23\]](#cite-note-23)</sup>

The folder for the signed-in user:

```text theme={null}
%LOCALAPPDATA%\Microsoft\Windows\WER\ReportArchive
```

The folder for the whole machine:

```text theme={null}
C:\ProgramData\Microsoft\Windows\WER\ReportArchive
```

### Check the Office Telemetry Log

The Office Telemetry Log can list add-in CPU and runtime error
events.<sup id="cite-ref-24">[\[24\]](#cite-note-24)</sup> It records events only after you turn on the
`EnableLogging` policy.<sup id="cite-ref-25">[\[25\]](#cite-note-25)</sup> Microsoft no longer supports the
Office Telemetry Dashboard but keeps the log.<sup id="cite-ref-26">[\[26\]](#cite-note-26)</sup>

After you turn on the policy, open this folder:

```text theme={null}
%LOCALAPPDATA%\Microsoft\Office\16.0\Telemetry
```

### Search your OpenTelemetry collector

Claude sends one trace for every user turn, including steps that failed.
Search your collector for traces at the time of the problem. See
[Configure a custom OpenTelemetry collector](/docs/office-agents/opentelemetry.md).

## References

Microsoft documentation for the limits, steps, and file locations on this page.

<ol>
  <li id="cite-note-1">↑ [a](#cite-ref-1-a) [b](#cite-ref-1-b) “[Excel not responding, hangs, freezes or stops working](https://support.microsoft.com/en-us/excel/excel-not-responding-hangs-freezes-or-stops-working)”. *Microsoft Support*. “If you try to perform other actions while Excel is in use, Excel may not respond.” The page also lists whole-column references, many hidden objects, excessive styles, and large numbers of shapes as causes of slowness.</li>
  <li id="cite-note-2">[↑](#cite-ref-2) “[Refresh an external data connection in Excel](https://support.microsoft.com/en-us/office/refresh-an-external-data-connection-in-excel-1524175f-777a-48fc-8fc7-c8514b984440)”. *Microsoft Support*.</li>
  <li id="cite-note-3">↑ [a](#cite-ref-3-a) [b](#cite-ref-3-b) [c](#cite-ref-3-c) [d](#cite-ref-3-d) [e](#cite-ref-3-e) “[Resource limits and performance optimization for Office Add-ins](https://learn.microsoft.com/en-us/office/dev/add-ins/concepts/resource-limits-and-performance-optimization)”. *Microsoft Learn*.</li>
  <li id="cite-note-4">↑ [a](#cite-ref-4-a) [b](#cite-ref-4-b) “[Avoid using the context.sync method in loops](https://learn.microsoft.com/en-us/office/dev/add-ins/concepts/correlated-objects-pattern)”. *Microsoft Learn*. “Office supports no more than 50 batch jobs in the queue. Any more triggers errors.”</li>
  <li id="cite-note-5">[↑](#cite-ref-5) “[File size limits for workbooks in SharePoint](https://support.microsoft.com/en-us/office/file-size-limits-for-workbooks-in-sharepoint-9e5bc6f8-018f-415a-b890-5452687b325e)”. *Microsoft Support*.</li>
  <li id="cite-note-6">[↑](#cite-ref-6) “[Large Address Aware capability change for Excel](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/excel/laa-capability-change)”. *Microsoft Learn*.</li>
  <li id="cite-note-7">↑ [a](#cite-ref-7-a) [b](#cite-ref-7-b) “[Locate and reset the last cell on a worksheet](https://support.microsoft.com/en-us/excel/locate-and-reset-the-last-cell-on-a-worksheet)”. *Microsoft Support*.</li>
  <li id="cite-note-8">↑ [a](#cite-ref-8-a) [b](#cite-ref-8-b) “[Tips for improving Excel's performance](https://support.microsoft.com/en-us/excel/tips-for-improving-excel-s-performance)”. *Microsoft Support*. The page advises opening Excel in a new instance when several workbooks in one instance run out of memory.</li>
  <li id="cite-note-9">[↑](#cite-ref-9) “[Check Workbook Statistics](https://support.microsoft.com/en-us/office/check-workbook-statistics-afa12d4b-9584-4826-99a8-33228467e006)”. *Microsoft Support*.</li>
  <li id="cite-note-10">↑ [a](#cite-ref-10-a) [b](#cite-ref-10-b) “[Cleanup cells in your workbook](https://support.microsoft.com/en-us/office/cleanup-cells-in-your-workbook-edcc579f-b82f-495b-8d31-e786cd11717b)”. *Microsoft Support*.</li>
  <li id="cite-note-11">↑ [a](#cite-ref-11-a) [b](#cite-ref-11-b) [c](#cite-ref-11-c) “[Clean up an Excel workbook so that it uses less memory](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/excel/clean-workbook-less-memory)”. *Microsoft Learn*.</li>
  <li id="cite-note-12">[↑](#cite-ref-12) “[Excel performance: Tips for optimizing performance obstructions](https://learn.microsoft.com/en-us/office/vba/excel/concepts/excel-performance/excel-tips-for-optimizing-performance-obstructions)”. *Microsoft Learn*. “You should always use the SUMIFS, COUNTIFS, and AVERAGEIFS functions instead of array formulas where you can because they are much faster to calculate.”</li>
  <li id="cite-note-13">[↑](#cite-ref-13) “[Excel performance: Improving calculation performance](https://learn.microsoft.com/en-us/office/vba/excel/concepts/excel-performance/excel-improving-calculation-performance)”. *Microsoft Learn*. “A volatile function is always recalculated at each recalculation even if it does not seem to have any changed precedents.”</li>
  <li id="cite-note-14">↑ [a](#cite-ref-14-a) [b](#cite-ref-14-b) “[Change formula recalculation, iteration, or precision in Excel](https://support.microsoft.com/en-us/office/change-formula-recalculation-iteration-or-precision-in-excel-73fc7dac-91cf-4d36-86e8-67124f6bcce4)”. *Microsoft Support*. The page covers the Manual and Automatic except for Data Tables options, the desktop and web scope, and the "Recalculate workbook before saving" setting that Manual turns on.</li>
  <li id="cite-note-15">[↑](#cite-ref-15) “[How Excel determines the current mode of calculation](https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/excel/current-mode-of-calculation)”. *Microsoft Learn*. “Changing the calculation mode of one open document changes the mode for all open documents.”</li>
  <li id="cite-note-16">↑ [a](#cite-ref-16-a) [b](#cite-ref-16-b) [c](#cite-ref-16-c) “[Reduce the file size of your PowerPoint presentations](https://support.microsoft.com/en-us/powerpoint/reduce-the-file-size-of-your-powerpoint-presentations)”. *Microsoft Support*. “if you delete the cropped picture data, you won't be able to restore it.” Discarding editing data also cannot be restored.</li>
  <li id="cite-note-17">[↑](#cite-ref-17) “[Compress your media files](https://support.microsoft.com/en-us/powerpoint/compress-your-media-files)”. *Microsoft Support*.</li>
  <li id="cite-note-18">↑ [a](#cite-ref-18-a) [b](#cite-ref-18-b) “[Help protect your files in case of a crash](https://support.microsoft.com/en-us/office/collab-files/help-protect-your-files-in-case-of-a-crash)”. *Microsoft Support*.</li>
  <li id="cite-note-19">[↑](#cite-ref-19) “[Recover an earlier version of an Office file](https://support.microsoft.com/en-us/office/collab-files/recover-an-earlier-version-of-an-office-file)”. *Microsoft Support*.</li>
  <li id="cite-note-20">[↑](#cite-ref-20) “[perfmon](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/perfmon)”. *Microsoft Learn*. “/rel | Starts the Reliability Monitor.”</li>
  <li id="cite-note-21">[↑](#cite-ref-21) “[Troubleshoot application or service crashing behavior](https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/troubleshoot-application-service-crashing-behavior)”. *Microsoft Learn*. “The Event ID 1000 with the Error level is the actual application crashing event.”</li>
  <li id="cite-note-22">[↑](#cite-ref-22) “[Excel freeze: Application Hang error](https://learn.microsoft.com/en-us/answers/questions/5132051/excel-freeze-application-hang-error)”. *Microsoft Q\&A*. This is a community answer. Microsoft has no official page that names event 1002.</li>
  <li id="cite-note-23">[↑](#cite-ref-23) “[Troubleshooting a failover cluster using Windows Error Reporting](https://learn.microsoft.com/en-us/windows-server/failover-clustering/troubleshooting-using-wer-reports)”. *Microsoft Learn*. “Windows Error Reporting Reports are stored in %ProgramData%\Microsoft\Windows\WER”. The per-user folder comes from “[Windows Error Reporting (WER) for developers](https://learn.microsoft.com/en-us/archive/blogs/oanapl/windows-error-reporting-wer-for-developers)”. *Microsoft Learn, archived*. “The reports are usually saved at %localAppData%\Microsoft\Windows\WER”.</li>
  <li id="cite-note-24">[↑](#cite-ref-24) “[Troubleshooting Office files and custom solutions with the telemetry log](https://learn.microsoft.com/en-us/office/client-developer/shared/troubleshooting-office-files-and-custom-solutions-with-the-telemetry-log)”. *Microsoft Learn*. , which lists the add-in events "Add-in used too much CPU" and "Add-in encountered runtime error".</li>
  <li id="cite-note-25">[↑](#cite-ref-25) “[Deploy Office Telemetry Dashboard](https://learn.microsoft.com/en-us/office/compatibility/deploy-telemetry-dashboard)”. *Microsoft Learn*. “By default, data collection is disabled in Office.” The page gives the `%localappdata%\Microsoft\Office\16.0\Telemetry` path and the `EnableLogging` setting.</li>
  <li id="cite-note-26">[↑](#cite-ref-26) “[Removal of Office Telemetry Dashboard from Microsoft 365 Apps for enterprise](https://learn.microsoft.com/en-us/office/compatibility/telemetry-dashboard-removal)”. *Microsoft Learn*. “Office Telemetry Log isn't being removed and is still available on client devices running Windows.”</li>
</ol>
