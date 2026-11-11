# Get started with Claude Sheets

Claude Sheets is a spreadsheet built into Claude. Ask for a tracker, budget, or model, and Claude builds a working sheet that you, your team, and Claude can edit together. This guide covers creating a sheet, working in it with Claude, importing and exporting data, and sharing it.

Claude Sheets is available in beta on Pro, Max, Ultra, Team, and Enterprise plans. It’s on by default on Team plans. On Enterprise plans, it’s off by default until it’s turned on in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**.

## How Claude Sheets works

A sheet is an artifact that you and Claude edit in the same cells. Claude can add tabs, write formulas that work across tabs, apply formatting and conditional formatting, and add dropdowns, checkboxes, and charts. Formulas stay in the cells, so you can see and check how each number was calculated.

When Claude changes a sheet, each edit is outlined as it lands, so you can see what changed. When other people are in the sheet, you all work in the same cells at the same time.

Every sheet you create is saved in the **Artifacts** tab. Learn more about **[artifacts and how to use them](https://support.claude.com/en/articles/17153992)**.

## How Claude Sheets differs from Claude for Excel

Claude Sheets puts a spreadsheet inside Claude. Claude for Excel and Claude for Google Workspace bring Claude to the files you already keep in those apps.

Use Claude Sheets for a light, shared sheet that you build with Claude. When your file already lives in Excel or Google Sheets, or you need the full set of features in those apps, use Claude for Excel or Claude for Google Workspace, or export your sheet.

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

- **Edit directly:** Type in cells, write formulas, and format your data yourself. Claude Sheets includes 144 functions.

- **Comment:** Add comments on cells for your team.

## Undo Claude’s changes

Version history shows earlier versions of a sheet and can restore an earlier version, which also removes edits made after it.

## Import and export

To bring data into a sheet, you can:

- Import a CSV file

- Import from Google Sheets

- Import from Excel

- Start from a blank sheet

Pasting from Excel or Google Sheets is also available. To download a sheet, export it as an .xlsx or CSV file. To continue working in another tool, use “Send to” for a variety of partner apps.

## Share a sheet

Sheets start private to you. To share one, open it and click “Share.” The people you share it with can work on it alongside you and Claude. Learn more about **[sharing artifacts](https://support.claude.com/en/articles/9547008)**.

## Usage

Claude Sheets counts toward your plan’s usage limits, like the rest of your work with Claude. Learn more about **[how usage and length limits work](https://support.claude.com/en/articles/11647753)**.

## Turn on Claude Sheets for your organization

This section is for Owners and Primary Owners on Team and Enterprise plans.

Turn Claude Sheets on or off in **[Organization settings > Artifacts](https://claude.ai/admin-settings/artifacts)**, in the Artifact templates section. It’s on by default on Team plans and off by default on Enterprise plans. Artifacts must also be on for your organization. Support for custom roles is also available, so admins can turn on Claude Sheets for a sub-set of their organization. Learn more in the **[Artifacts admin guide for Team and Enterprise plans](https://support.claude.com/en/articles/16994751)**.

## Current limitations

Claude Sheets is in beta and covers common spreadsheet work. We’re adding more over time. At launch:

- **Size:** A sheet can hold up to 100,000 cells.

- **Charts:** Bar, line, and pie charts are available, as well as a wide range of other chart types Claude can generate.

- **Features not available yet:** Pivot tables, protected ranges, find and replace, multi-column sort, filter views, multi-select dropdowns, and PDF export.

- **Excel features not supported:** Macros, VBA, Power Query, DAX, and print layout.

- **Live data:** Sheets can’t pull live data from connected apps, and docs, decks, and dashboards can’t use a sheet as a data source.

- **Platforms:** web and desktop are supported, with basic read-only access on mobile

- **Data controls:** Claude Sheets is a beta product, so HIPAA, CMEK, and ZDR are not yet supported.