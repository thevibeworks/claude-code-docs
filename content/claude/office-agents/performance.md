> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Performance and limits

> How Claude for M365 works with a busy Office app, the size limits to know, and what to do when Office slows down or stops responding.

Claude for M365 does its work inside your Office app. When a file has very
large ranges, many shapes, or heavy formulas, the app can slow down or stop
responding.<sup id="cite-ref-1-a" className="scroll-mt-24"><a href="#cite-note-1">\[1]</a></sup> This happens with any heavy task in Office, with
or without Claude.

## Office runs one step at a time

Claude sends each step to Office and waits for Office to finish it. While
Office is busy, other actions can stall too.<sup id="cite-ref-1-b" className="scroll-mt-24"><a href="#cite-note-1">\[1]</a></sup>

<img src="https://mintcdn.com/claude-ai/_Xjykq_jOPUQ7vjH/images/office-agents/performance/perf-one-step.png?fit=max&auto=format&n=_Xjykq_jOPUQ7vjH&q=85&s=86e807e77450672873ddcbd4e16578d3" alt="Claude sends a step and waits. Office runs the step, for example a recalculation, a large read, or a big slide edit. At the wait limit, Claude reports a timeout, but Office is still running the step. The wait limit is 90 seconds for steps where Claude runs code, 5 minutes for other steps, and 2 minutes on the web. Stop and a timeout end Claude's wait, not the step Office already started." width="1930" height="792" data-path="images/office-agents/performance/perf-one-step.png" />

Four habits reduce slowdowns.

* **Let each step finish**: do not click, type, edit, run macros, or start a
  data refresh while Claude works. If a refresh is already running, wait for
  it or stop it with Esc or Stop Refresh.<sup id="cite-ref-2" className="scroll-mt-24"><a href="#cite-note-2">\[2]</a></sup> If Office asks whether to
  keep running the add-in, continue.<sup id="cite-ref-3-a" className="scroll-mt-24"><a href="#cite-note-3">\[3]</a></sup>
* **Give Claude only what the task needs**: name the sheet and range, or
  copy the sheets you need into a new workbook.
* **Ask for large changes one step at a time**: split a big job into
  smaller requests.
* **Wait after a timeout**: let Office respond, save, then ask for a
  smaller step.

## Limits to know

These limits come from Claude for M365 and from Office itself.

| Limit                                       | Value                                                                                                                           | What it means for you                       |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| Wait for a step where Claude runs code      | 90 seconds                                                                                                                      | A heavy step can time out                   |
| Wait for other steps, such as writing cells | 5 minutes on the desktop, 2 minutes on the web                                                                                  | A heavy step can time out                   |
| Wait for a Word text edit                   | 30 seconds                                                                                                                      | A heavy edit can time out                   |
| Cells returned by one Claude read in Excel  | 2,000 cells with data                                                                                                           | Claude reads a large sheet in several steps |
| Cells Office reads from one range           | 5,000,000<sup id="cite-ref-3-b" className="scroll-mt-24"><a href="#cite-note-3">\[3]</a></sup>                                  | A larger read can fail                      |
| One request in Excel on the web             | 5 MB<sup id="cite-ref-3-c" className="scroll-mt-24"><a href="#cite-note-3">\[3]</a></sup>                                       | Large reads and writes can fail on the web  |
| Command batches waiting in Office           | 50<sup id="cite-ref-4-a" className="scroll-mt-24"><a href="#cite-note-4">\[4]</a></sup>                                         | More batches cause errors                   |
| Workbook opened in a browser                | Up to 100 MB, depending on your subscription<sup id="cite-ref-5" className="scroll-mt-24"><a href="#cite-note-5">\[5]</a></sup> | Open larger files in Excel on the desktop   |
| Memory for 32-bit Excel                     | Up to 4 GB on 64-bit Windows<sup id="cite-ref-6" className="scroll-mt-24"><a href="#cite-note-6">\[6]</a></sup>                 | Use 64-bit Office for large workbooks       |

## File size and risk

Sessions with larger files more often end with a step that never finished.
This is how Claude for M365 detects an Office crash, a force quit, or a
reload. Larger files also mean longer sessions. The chart is directional,
based on what Claude for M365 usage shows.

<img src="https://mintcdn.com/claude-ai/_Xjykq_jOPUQ7vjH/images/office-agents/performance/perf-risk.png?fit=max&auto=format&n=_Xjykq_jOPUQ7vjH&q=85&s=c018954e584a7b8fe3712b69b226f106" alt="Directional chart of risk by file size. In Excel, measured by total used cells across all sheets, risk is lowest under 1 million cells, higher from 1 to 5 million, and highest over 5 million. In PowerPoint, measured by slides, risk is lowest under 100 slides, higher from 100 to 199, and highest at 200 or more. The chart shows direction, not measured values." width="1890" height="1062" data-path="images/office-agents/performance/perf-risk.png" />

The risk rises steadily, without a sharp threshold. Treat the bands as guides.

| File                                      | Works well      | Higher risk, so narrow your requests | Use at your own risk |
| ----------------------------------------- | --------------- | ------------------------------------ | -------------------- |
| Excel, total used cells across all sheets | Under 1 million | 1 to 5 million                       | Over 5 million       |
| PowerPoint, slides                        | Under 100       | 100 to 199                           | 200 or more          |

To estimate the total for a workbook, go to each sheet and press Ctrl+End to
move to its last cell.<sup id="cite-ref-7-a" className="scroll-mt-24"><a href="#cite-note-7">\[7]</a></sup> Multiply the number of the last row by the
number of the last column, then add the results for all sheets. A last cell
of Z100000 is column 26 and row 100,000, about 2.6 million cells. Formatting
on empty cells moves the last cell, so a sheet can count as larger than its
data.<sup id="cite-ref-7-b" className="scroll-mt-24"><a href="#cite-note-7">\[7]</a></sup>

A single sheet above 5 million cells also passes the limit for one Office
read.<sup id="cite-ref-3-d" className="scroll-mt-24"><a href="#cite-note-3">\[3]</a></sup>

## Limit what is open at once

Workbooks that you open in the same instance of Excel share one Excel
process, and each workbook has its own Claude pane.<sup id="cite-ref-8-a" className="scroll-mt-24"><a href="#cite-note-8">\[8]</a></sup> Every pane
sends its commands to that process. Office queues the command batches it
receives, up to 50 at a time.<sup id="cite-ref-4-b" className="scroll-mt-24"><a href="#cite-note-4">\[4]</a></sup> When the computer is short of CPU
or memory, the wait grows, and Excel can stall or crash.

<img src="https://mintcdn.com/claude-ai/_Xjykq_jOPUQ7vjH/images/office-agents/performance/perf-shared-process.png?fit=max&auto=format&n=_Xjykq_jOPUQ7vjH&q=85&s=524e1317ae5b08f66fe51b4dcf8373ae" alt="One Excel process contains three workbooks, each with its own Claude pane. The commands from all three panes go into a single command queue in the same process. The process runs on a computer with limited CPU and memory. When CPU and memory run short, waits grow and Excel can stall or crash. Keep only the files you need open." width="1890" height="872" data-path="images/office-agents/performance/perf-shared-process.png" />

Other Office apps run in their own processes, but they share the same CPU and
memory. Office starts to monitor add-in memory when the device passes 80%
memory use.<sup id="cite-ref-3-e" className="scroll-mt-24"><a href="#cite-note-3">\[3]</a></sup>

* Close the files you are not working in.
* For large files, work in one file at a time.
* When Claude works across Office apps, ask it to finish in one app before it
  moves to the next. See [Work across M365 apps](/docs/office-agents/work-across-apps).
* If Excel runs out of memory with several workbooks open, open Excel in a new
  instance.<sup id="cite-ref-8-b" className="scroll-mt-24"><a href="#cite-note-8">\[8]</a></sup>

## Lighter files respond faster

A smaller used range and lighter formulas shorten the time Office needs for
each step.

### Make large workbooks lighter

Excel has built-in tools that show what makes a workbook heavy.

| Task                                       | Where in Excel                                                                                                              |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| See counts of cells, formulas, and objects | Review, Workbook Statistics<sup id="cite-ref-9" className="scroll-mt-24"><a href="#cite-note-9">\[9]</a></sup>              |
| Remove formatting from empty cells         | Review, Check Performance<sup id="cite-ref-10-a" className="scroll-mt-24"><a href="#cite-note-10">\[10]</a></sup>           |
| Find hidden shapes and pictures            | Home, Find & Select, Selection Pane<sup id="cite-ref-11-a" className="scroll-mt-24"><a href="#cite-note-11">\[11]</a></sup> |

Save a copy of the workbook before you run Check Performance. It removes
formatting from cells that look empty, including cells used for pixel
art.<sup id="cite-ref-10-b" className="scroll-mt-24"><a href="#cite-note-10">\[10]</a></sup>

If the workbook is still too large, copy the sheets you need into a new
workbook.<sup id="cite-ref-11-b" className="scroll-mt-24"><a href="#cite-note-11">\[11]</a></sup>

### Ask for formulas that calculate fast

Some formulas make Excel recalculate far more cells than others. Ask Claude
for these forms.

* **Conditional sums and counts**: SUMIFS, COUNTIFS, and AVERAGEIFS. They
  calculate much faster than array formulas.<sup id="cite-ref-12" className="scroll-mt-24"><a href="#cite-note-12">\[12]</a></sup>
* **Today's date**: TODAY in one cell, with other cells that refer to
  it.<sup id="cite-ref-11-c" className="scroll-mt-24"><a href="#cite-note-11">\[11]</a></sup>
* **Direct references**: cell references in place of OFFSET and INDIRECT,
  which recalculate at each recalculation.<sup id="cite-ref-13" className="scroll-mt-24"><a href="#cite-note-13">\[13]</a></sup>

### Pause calculation during large changes

Excel recalculates dependent formulas after every change. For large formula
changes, pause recalculation until Claude is done.

<Steps>
  <Step title="Set calculation to manual">
    On the Formulas tab, select Calculation Options, Manual.<sup id="cite-ref-14-a" className="scroll-mt-24"><a href="#cite-note-14">\[14]</a></sup>
    The option Automatic except for Data Tables skips only data tables.
    Ordinary formulas still recalculate after every change.
  </Step>

  <Step title="Ask Claude for the changes">
    Claude writes the formulas without a recalculation after each one.
  </Step>

  <Step title="Recalculate">
    Press F9 when Claude is done. In Manual mode, formula results stay out of
    date until you press F9.
  </Step>

  <Step title="Check the results">
    Ask Claude to verify the formulas after the recalculation.
  </Step>

  <Step title="Turn automatic calculation back on">
    Select Calculation Options, Automatic.
  </Step>
</Steps>

<Note>
  Manual calculation applies to every open workbook in Excel on the desktop.<sup id="cite-ref-15" className="scroll-mt-24"><a href="#cite-note-15">\[15]</a></sup>
  In Excel on the web it applies only to the current workbook. In Manual mode,
  saving can recalculate the workbook.<sup id="cite-ref-14-b" className="scroll-mt-24"><a href="#cite-note-14">\[14]</a></sup>
</Note>

### Make large presentations lighter

Large pictures and media make a presentation larger.<sup id="cite-ref-16-a" className="scroll-mt-24"><a href="#cite-note-16">\[16]</a></sup> Compress them
before you ask Claude for large changes.

| Task                     | Where in PowerPoint                                                                                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compress pictures        | Picture Format, Compress Pictures, with "Apply only to this picture" cleared<sup id="cite-ref-16-b" className="scroll-mt-24"><a href="#cite-note-16">\[16]</a></sup> |
| Compress audio and video | File, Info, Compress Media, in PowerPoint on Windows<sup id="cite-ref-17" className="scroll-mt-24"><a href="#cite-note-17">\[17]</a></sup>                           |

Save a copy of the presentation before you compress. Deleting cropped picture
areas and discarding editing data cannot be undone.<sup id="cite-ref-16-c" className="scroll-mt-24"><a href="#cite-note-16">\[16]</a></sup>

Ask Claude to change a few slides at a time.

## When Office stops responding

Use this table when Office stops responding during a request.

| Situation                | What to do                                                                                                                                                                                |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Claude waits on a step   | Wait. Do not click repeatedly.                                                                                                                                                            |
| Claude reports a timeout | Wait until Office responds, save, then ask for a smaller step. The step can still be running in Office.                                                                                   |
| Office closes            | Reopen the file and look for the Document Recovery pane.<sup id="cite-ref-18-a" className="scroll-mt-24"><a href="#cite-note-18">\[18]</a></sup> Start a new chat with a smaller request. |
| It happens often         | Send your IT admin the transcript and the time of the problem.                                                                                                                            |

When something goes wrong, keep your work and the chat for your admin.

<Steps>
  <Step title="Recover your work">
    Reopen the app and look for the Document Recovery pane.<sup id="cite-ref-18-b" className="scroll-mt-24"><a href="#cite-note-18">\[18]</a></sup>
    In Excel, you can also go to File, Info, Manage Document, Recover Unsaved
    Workbooks.<sup id="cite-ref-19" className="scroll-mt-24"><a href="#cite-note-19">\[19]</a></sup>
  </Step>

  <Step title="Download the chat">
    In the Claude pane, select More options, then Download Transcript.
  </Step>

  <Step title="Send it to IT">
    Send the file and the time of the problem through your usual support
    channel. The file contains your chat.
  </Step>
</Steps>

## Investigate a crash or hang

Windows, Office, and Claude each keep a record of what happened. Start with
the time of the problem, then check the records below in order. The Windows
and Office records exist on Windows only.

<img src="https://mintcdn.com/claude-ai/_Xjykq_jOPUQ7vjH/images/office-agents/performance/perf-where-to-look.png?fit=max&auto=format&n=_Xjykq_jOPUQ7vjH&q=85&s=d62ef0be87cdd199fb375df256ef2642" alt="Four sources of records, in order. First, the user: the time of the problem, which is the key to every record, and the transcript of what Claude was doing. Second, Windows only: Reliability Monitor with a daily crash and hang timeline, Event Viewer with event 1000 for a crash and 1002 for a hang, and Windows Error Reporting files for crashes and hangs. Third, Office: the Telemetry Log with add-in CPU and error events, which stays off until an admin enables it. Fourth, your collector: an OpenTelemetry trace for every user turn." width="1890" height="722" data-path="images/office-agents/performance/perf-where-to-look.png" />

### Collect the user's report

The time of the problem is the key to every other record. Ask the user for
the time, the Office app, and whether Office closed or stopped responding.

Then ask the user to select More options in the Claude pane, then Download
Transcript. The transcript shows what Claude was doing when the problem
started.

### Check Reliability Monitor

Reliability Monitor shows a daily timeline of app crashes and hangs. Use it
to confirm that the problem happened and to see how often it repeats.
Press Windows+R and run this command.<sup id="cite-ref-20" className="scroll-mt-24"><a href="#cite-note-20">\[20]</a></sup>

```text theme={null}
perfmon /rel
```

### Read Event Viewer

Event Viewer separates a crash from a hang. Open Event Viewer, select
Windows Logs, then Application. Look for events from `EXCEL.EXE`,
`POWERPNT.EXE`, `WINWORD.EXE`, or `OUTLOOK.EXE` near the time of the
problem.

* **Event 1000**: a crash. The event names the faulting module.<sup id="cite-ref-21" className="scroll-mt-24"><a href="#cite-note-21">\[21]</a></sup>
* **Event 1002**: a hang.<sup id="cite-ref-22" className="scroll-mt-24"><a href="#cite-note-22">\[22]</a></sup>

### Find Windows Error Reporting files

Windows Error Reporting keeps a report for each crash or hang. The reports
are in one of two folders.<sup id="cite-ref-23" className="scroll-mt-24"><a href="#cite-note-23">\[23]</a></sup>

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
events.<sup id="cite-ref-24" className="scroll-mt-24"><a href="#cite-note-24">\[24]</a></sup> It records events only after you turn on the
`EnableLogging` policy.<sup id="cite-ref-25" className="scroll-mt-24"><a href="#cite-note-25">\[25]</a></sup> Microsoft no longer supports the
Office Telemetry Dashboard but keeps the log.<sup id="cite-ref-26" className="scroll-mt-24"><a href="#cite-note-26">\[26]</a></sup>

After you turn on the policy, open this folder:

```text theme={null}
%LOCALAPPDATA%\Microsoft\Office\16.0\Telemetry
```

### Search your OpenTelemetry collector

Claude sends one trace for every user turn, including steps that failed.
Search your collector for traces at the time of the problem. See
[Configure a custom OpenTelemetry collector](/docs/office-agents/opentelemetry).

## References

Microsoft documentation for the limits, steps, and file locations on this page.

<ol>
  <li id="cite-note-1" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10">↑ <a href="#cite-ref-1-a" className="font-normal">a</a> <a href="#cite-ref-1-b" className="font-normal">b</a> “<a href="https://support.microsoft.com/en-us/excel/excel-not-responding-hangs-freezes-or-stops-working">Excel not responding, hangs, freezes or stops working</a>”. <em>Microsoft Support</em>. “If you try to perform other actions while Excel is in use, Excel may not respond.” The page also lists whole-column references, many hidden objects, excessive styles, and large numbers of shapes as causes of slowness.</li>
  <li id="cite-note-2" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-2" className="font-normal">↑</a> “<a href="https://support.microsoft.com/en-us/office/refresh-an-external-data-connection-in-excel-1524175f-777a-48fc-8fc7-c8514b984440">Refresh an external data connection in Excel</a>”. <em>Microsoft Support</em>.</li>
  <li id="cite-note-3" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10">↑ <a href="#cite-ref-3-a" className="font-normal">a</a> <a href="#cite-ref-3-b" className="font-normal">b</a> <a href="#cite-ref-3-c" className="font-normal">c</a> <a href="#cite-ref-3-d" className="font-normal">d</a> <a href="#cite-ref-3-e" className="font-normal">e</a> “<a href="https://learn.microsoft.com/en-us/office/dev/add-ins/concepts/resource-limits-and-performance-optimization">Resource limits and performance optimization for Office Add-ins</a>”. <em>Microsoft Learn</em>.</li>
  <li id="cite-note-4" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10">↑ <a href="#cite-ref-4-a" className="font-normal">a</a> <a href="#cite-ref-4-b" className="font-normal">b</a> “<a href="https://learn.microsoft.com/en-us/office/dev/add-ins/concepts/correlated-objects-pattern">Avoid using the context.sync method in loops</a>”. <em>Microsoft Learn</em>. “Office supports no more than 50 batch jobs in the queue. Any more triggers errors.”</li>
  <li id="cite-note-5" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-5" className="font-normal">↑</a> “<a href="https://support.microsoft.com/en-us/office/file-size-limits-for-workbooks-in-sharepoint-9e5bc6f8-018f-415a-b890-5452687b325e">File size limits for workbooks in SharePoint</a>”. <em>Microsoft Support</em>.</li>
  <li id="cite-note-6" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-6" className="font-normal">↑</a> “<a href="https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/excel/laa-capability-change">Large Address Aware capability change for Excel</a>”. <em>Microsoft Learn</em>.</li>
  <li id="cite-note-7" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10">↑ <a href="#cite-ref-7-a" className="font-normal">a</a> <a href="#cite-ref-7-b" className="font-normal">b</a> “<a href="https://support.microsoft.com/en-us/excel/locate-and-reset-the-last-cell-on-a-worksheet">Locate and reset the last cell on a worksheet</a>”. <em>Microsoft Support</em>.</li>
  <li id="cite-note-8" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10">↑ <a href="#cite-ref-8-a" className="font-normal">a</a> <a href="#cite-ref-8-b" className="font-normal">b</a> “<a href="https://support.microsoft.com/en-us/excel/tips-for-improving-excel-s-performance">Tips for improving Excel's performance</a>”. <em>Microsoft Support</em>. The page advises opening Excel in a new instance when several workbooks in one instance run out of memory.</li>
  <li id="cite-note-9" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-9" className="font-normal">↑</a> “<a href="https://support.microsoft.com/en-us/office/check-workbook-statistics-afa12d4b-9584-4826-99a8-33228467e006">Check Workbook Statistics</a>”. <em>Microsoft Support</em>.</li>
  <li id="cite-note-10" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10">↑ <a href="#cite-ref-10-a" className="font-normal">a</a> <a href="#cite-ref-10-b" className="font-normal">b</a> “<a href="https://support.microsoft.com/en-us/office/cleanup-cells-in-your-workbook-edcc579f-b82f-495b-8d31-e786cd11717b">Cleanup cells in your workbook</a>”. <em>Microsoft Support</em>.</li>
  <li id="cite-note-11" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10">↑ <a href="#cite-ref-11-a" className="font-normal">a</a> <a href="#cite-ref-11-b" className="font-normal">b</a> <a href="#cite-ref-11-c" className="font-normal">c</a> “<a href="https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/excel/clean-workbook-less-memory">Clean up an Excel workbook so that it uses less memory</a>”. <em>Microsoft Learn</em>.</li>
  <li id="cite-note-12" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-12" className="font-normal">↑</a> “<a href="https://learn.microsoft.com/en-us/office/vba/excel/concepts/excel-performance/excel-tips-for-optimizing-performance-obstructions">Excel performance: Tips for optimizing performance obstructions</a>”. <em>Microsoft Learn</em>. “You should always use the SUMIFS, COUNTIFS, and AVERAGEIFS functions instead of array formulas where you can because they are much faster to calculate.”</li>
  <li id="cite-note-13" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-13" className="font-normal">↑</a> “<a href="https://learn.microsoft.com/en-us/office/vba/excel/concepts/excel-performance/excel-improving-calculation-performance">Excel performance: Improving calculation performance</a>”. <em>Microsoft Learn</em>. “A volatile function is always recalculated at each recalculation even if it does not seem to have any changed precedents.”</li>
  <li id="cite-note-14" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10">↑ <a href="#cite-ref-14-a" className="font-normal">a</a> <a href="#cite-ref-14-b" className="font-normal">b</a> “<a href="https://support.microsoft.com/en-us/office/change-formula-recalculation-iteration-or-precision-in-excel-73fc7dac-91cf-4d36-86e8-67124f6bcce4">Change formula recalculation, iteration, or precision in Excel</a>”. <em>Microsoft Support</em>. The page covers the Manual and Automatic except for Data Tables options, the desktop and web scope, and the "Recalculate workbook before saving" setting that Manual turns on.</li>
  <li id="cite-note-15" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-15" className="font-normal">↑</a> “<a href="https://learn.microsoft.com/en-us/troubleshoot/microsoft-365-apps/excel/current-mode-of-calculation">How Excel determines the current mode of calculation</a>”. <em>Microsoft Learn</em>. “Changing the calculation mode of one open document changes the mode for all open documents.”</li>
  <li id="cite-note-16" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10">↑ <a href="#cite-ref-16-a" className="font-normal">a</a> <a href="#cite-ref-16-b" className="font-normal">b</a> <a href="#cite-ref-16-c" className="font-normal">c</a> “<a href="https://support.microsoft.com/en-us/powerpoint/reduce-the-file-size-of-your-powerpoint-presentations">Reduce the file size of your PowerPoint presentations</a>”. <em>Microsoft Support</em>. “if you delete the cropped picture data, you won't be able to restore it.” Discarding editing data also cannot be restored.</li>
  <li id="cite-note-17" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-17" className="font-normal">↑</a> “<a href="https://support.microsoft.com/en-us/powerpoint/compress-your-media-files">Compress your media files</a>”. <em>Microsoft Support</em>.</li>
  <li id="cite-note-18" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10">↑ <a href="#cite-ref-18-a" className="font-normal">a</a> <a href="#cite-ref-18-b" className="font-normal">b</a> “<a href="https://support.microsoft.com/en-us/office/collab-files/help-protect-your-files-in-case-of-a-crash">Help protect your files in case of a crash</a>”. <em>Microsoft Support</em>.</li>
  <li id="cite-note-19" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-19" className="font-normal">↑</a> “<a href="https://support.microsoft.com/en-us/office/collab-files/recover-an-earlier-version-of-an-office-file">Recover an earlier version of an Office file</a>”. <em>Microsoft Support</em>.</li>
  <li id="cite-note-20" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-20" className="font-normal">↑</a> “<a href="https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/perfmon">perfmon</a>”. <em>Microsoft Learn</em>. “/rel | Starts the Reliability Monitor.”</li>
  <li id="cite-note-21" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-21" className="font-normal">↑</a> “<a href="https://learn.microsoft.com/en-us/troubleshoot/windows-server/performance/troubleshoot-application-service-crashing-behavior">Troubleshoot application or service crashing behavior</a>”. <em>Microsoft Learn</em>. “The Event ID 1000 with the Error level is the actual application crashing event.”</li>
  <li id="cite-note-22" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-22" className="font-normal">↑</a> “<a href="https://learn.microsoft.com/en-us/answers/questions/5132051/excel-freeze-application-hang-error">Excel freeze: Application Hang error</a>”. <em>Microsoft Q\&A</em>. This is a community answer. Microsoft has no official page that names event 1002.</li>
  <li id="cite-note-23" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-23" className="font-normal">↑</a> “<a href="https://learn.microsoft.com/en-us/windows-server/failover-clustering/troubleshooting-using-wer-reports">Troubleshooting a failover cluster using Windows Error Reporting</a>”. <em>Microsoft Learn</em>. “Windows Error Reporting Reports are stored in %ProgramData%\Microsoft\Windows\WER”. The per-user folder comes from “<a href="https://learn.microsoft.com/en-us/archive/blogs/oanapl/windows-error-reporting-wer-for-developers">Windows Error Reporting (WER) for developers</a>”. <em>Microsoft Learn, archived</em>. “The reports are usually saved at %localAppData%\Microsoft\Windows\WER”.</li>
  <li id="cite-note-24" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-24" className="font-normal">↑</a> “<a href="https://learn.microsoft.com/en-us/office/client-developer/shared/troubleshooting-office-files-and-custom-solutions-with-the-telemetry-log">Troubleshooting Office files and custom solutions with the telemetry log</a>”. <em>Microsoft Learn</em>. , which lists the add-in events "Add-in used too much CPU" and "Add-in encountered runtime error".</li>
  <li id="cite-note-25" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-25" className="font-normal">↑</a> “<a href="https://learn.microsoft.com/en-us/office/compatibility/deploy-telemetry-dashboard">Deploy Office Telemetry Dashboard</a>”. <em>Microsoft Learn</em>. “By default, data collection is disabled in Office.” The page gives the <code>%localappdata%\Microsoft\Office\16.0\Telemetry</code> path and the <code>EnableLogging</code> setting.</li>
  <li id="cite-note-26" className="scroll-mt-24 target:bg-amber-100/60 dark:target:bg-amber-400/10"><a href="#cite-ref-26" className="font-normal">↑</a> “<a href="https://learn.microsoft.com/en-us/office/compatibility/telemetry-dashboard-removal">Removal of Office Telemetry Dashboard from Microsoft 365 Apps for enterprise</a>”. <em>Microsoft Learn</em>. “Office Telemetry Log isn't being removed and is still available on client devices running Windows.”</li>
</ol>
