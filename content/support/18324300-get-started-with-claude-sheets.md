# Get started with Claude Sheets

Claude Sheets is a spreadsheet built into Claude. Ask for a tracker, budget, or model, and Claude builds a working sheet that you, your team, and Claude can edit together. This guide covers creating a sheet, working in it with Claude, importing and exporting data, and sharing it.

Claude Sheets is available in beta on Pro, Max, Ultra, Team, and Enterprise plans. It’s on by default on Team plans. On Enterprise plans, it’s off by default until it’s turned on in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

## How Claude Sheets works

A sheet is an artifact that you and Claude edit in the same cells. Claude can add tabs, write formulas that work across tabs, apply formatting and conditional formatting, and add dropdowns, checkboxes, and charts. Formulas stay in the cells, so you can see and check how each number was calculated.

When Claude changes a sheet, each edit is outlined as it lands, so you can see what changed. When other people are in the sheet, you all work in the same cells at the same time.

Every sheet you create is saved in the **Artifacts** tab. Learn more about **[artifacts and how to use them](https://support.claude.com/en/articles/17153992)**.

## How Claude Sheets differs from Claude for Excel

Claude Sheets puts a spreadsheet inside Claude. Claude for Excel and Claude for Google Workspace bring Claude to the files you already keep in those apps.

Use Claude Sheets for trackers, budgets, plans, and models that you and your team build and update with Claude. If your file has to stay in Excel or Google Sheets, use Claude for Excel or Claude for Google Workspace there. You can also import the file into Claude Sheets, and export it as .xlsx.

## Create a sheet

### From a chat

Ask Claude for a sheet in any chat. For example:

- “Build a campaign tracker with owners, dates, and status.”

- “Make a hiring budget by team and quarter.”

- “Forecast next quarter from these deals and flag what’s at risk.”

### From the Artifacts tab

1. Go to the **Artifacts** tab.

2. Select the “Sheets” tile.

3. Describe the sheet you want, or start with a blank sheet.

### Tips for better results

Say what the sheet is for and what you want to track. If you already have the numbers, give them to Claude so the sheet is built from your own data.

## Work in your sheet

- **Ask Claude:** Ask for changes, like “Add a column for budget remaining” or “Highlight anything that’s overdue.”

- **Ask about a range:** Select cells and ask Claude about them, like “Why is this total higher than last month?”

- **Edit directly:** Type in cells, write formulas, and format your data yourself. Claude Sheets includes over 250 functions.

- **Comment:** Add comments on cells for your team.

## Edit your sheet yourself

You can do everyday spreadsheet work without asking Claude:

- **Sort:** Right-click a cell and open the sort menu. To sort by several columns, select “Custom sort.” You can sort for yourself or for all users of the sheet.

- **Filter:** Right-click a cell in a table and select “Filter.” You can filter for yourself or for all users of the sheet.

- **Find and replace:** Press Ctrl+H (Cmd+Shift+H on Mac) to find and replace text in the current tab or in the selected cells. Formula results, dropdowns, and checkboxes can’t be changed this way.

- **Charts:** Select cells with numbers, then select “Insert chart” in the toolbar, or right-click and select “Make chart.” Pick a chart type to add it to your sheet.

- **Conditional formatting:** Select cells, then select “Conditional formatting” in the toolbar or the right-click menu to color cells by a rule.

- **People:** On Team and Enterprise plans, type @ in a cell, then select a person from your organization. A cell can hold several people: click the cell to add more.

- **Dropdowns, checkboxes, and dates:** Right-click a cell, select “Insert,” then select “Dropdown,” “Checkbox,” or “Date.” Double-click a date to change it in a date picker, unless a formula calculates it.

- **Rows and columns:** Right-click a row number or column letter to freeze, group, move, or resize it. To merge cells, select them, right-click, and select “Merge cells.”

- **Number formats:** Select “Number format” in the toolbar to show numbers as currency, percentages, dates, and more.

- **Tables:** When Claude Sheets recognizes a block of cells with a header row as a table, it gives the block a table look and keeps the header in view as you scroll.

- **Cell history:** Right-click a cell and select “View history” to see recent edits to that cell or its row, who made them, and when.

- **Keyboard shortcuts:** With a cell selected, press Ctrl+/ (Cmd+/ on Mac) to see the full list.

## Ask Claude from inside the sheet

If you can edit a sheet, you don’t need the chat for every change:

- **Write a formula in plain words:** Type = in a cell and describe what you want, then select “Write this formula.” Select “Keep” or “Discard” when you see the result. For something simple, like “=sum B2 to B5,” the formula may appear right away, and you can select it.

- **Fix an error:** Select a cell that shows an error, then select “Fix with Claude.” Select “Keep” or “Discard” when you see the fix. If you see “Ask Claude to fix” instead, it opens the chat.

- **Describe a chart:** Select your data, select “Insert chart,” describe the chart you want, and select “Make this chart.”

- **Describe a rule:** Select “Conditional formatting,” type a rule like “red if over budget,” and select “Write rules.”

- **Describe a filter:** Right-click a cell in a table, select “Filter,” and type which rows to show, like “overdue” or “top 10 by revenue.”

- **Ask about cells:** Select cells, right-click, and select “Ask Claude.”

- **Send a comment to Claude:** When you write a comment, make sure “Send to Claude” is checked.

**Note:** When Claude does the work, it counts toward usage limits. On Team and Enterprise plans, an admin can turn off Sheets in **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**. Some options, including comments, aren’t available to people from outside your organization.

## Undo Claude’s changes

When Claude finishes, a card says what Claude updated. If it shows “Undo,” select it to take back only that change. The card goes away a few seconds after you’re back in the sheet, or as soon as you work in the cells. After that, use **Version history** to restore an earlier version, which also removes edits made after it.

## Import and export

To bring data into a sheet, you can:

- Import a CSV file

- Import from Google Sheets

- Import from Excel

- Start from a blank sheet

Pasting from Excel or Google Sheets is also available. To download a sheet, export it as an .xlsx or CSV file. To continue working in another tool, use "Send to."

## Share a sheet

Sheets start private to you. To share one, open it and click "Share." People you share it with who have “Can edit” access can work on it alongside you and Claude. People from outside your organization can’t add comments. With “Anyone with the link,” the sheet opens only for people signed in to Claude, who can only view it. Learn more about **[sharing artifacts](https://support.claude.com/en/articles/9547008)**.

## Usage

Claude Sheets counts toward your plan’s usage limits, like the rest of your work with Claude. Learn more about **[how usage and length limits work](https://support.claude.com/en/articles/11647753)**.

## Turn on Claude Sheets for your organization

This section is for Owners and Primary Owners on Team and Enterprise plans.

Turn Claude Sheets on or off in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**, under **Templates**. It’s on by default on Team plans and off by default on Enterprise plans. Artifacts must also be on for your organization. On Enterprise plans, once Claude Sheets is on, custom roles can limit it to specific groups. Learn more in the **[Artifacts admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/16994751)**.

## Current limitations

Claude Sheets is in beta and covers common spreadsheet work. We’re adding more over time.

- **Size:** A sheet can hold over 500,000 filled cells.

- **Charts:** Bar, line, and pie charts are available, as well as a wide range of other chart types Claude can generate.

- **Features not available yet:** Multi-select dropdowns, and PDF export.

- **Excel features not supported:** Macros, VBA, Power Query, DAX, and print layout.

- **Live data:** Sheets can’t pull live data from connected apps, and docs, decks, and dashboards can’t use a sheet as a data source.

- **Platforms:** Web, desktop, Claude for iOS, and Claude for Android.

- **Data controls:** Claude Sheets is a beta product. It isn’t yet available to organizations with HIPAA-ready configurations or with zero data retention for Claude Code. Sheets aren’t covered by zero data retention.