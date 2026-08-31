> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude for Government changelog

> Release notes for Claude for Government

<Update label="2026.08.28.1">
  * Improved screen reader and keyboard support in the Admin Console: actions such as revoking a key or saving seats now announce their result, and keyboard focus returns to the control you used instead of being lost.
  * Changed the main button on the sign-in pages to a dark button with a white label so it is easier to read; the page an emailed sign-in link opens now announces its result to screen readers.
  * Added the "Restart deadline for configuration changes" setting under Config > Compliance and telemetry: it sets how long members can keep working after a settings change before Claude Desktop requires the restart that applies it, and takes effect on Claude Desktop 1.40609.0 or later.
  * Added a search box to the Config page that finds a setting by its name or description and takes you to it.
</Update>

<Update label="2026.08.26.1">
  * Fixed members on the default 24-hour "Session idle timeout" being signed out a day after signing in even when they had kept using Claude; the timeout now counts from a member's last activity.
  * Improved screen reader support in the Admin Console: dialog options, repeated buttons, and usage meters are announced with distinct names, every page has its own browser title, and the setup wizards move keyboard focus to the new step's heading when you change steps.
  * Changed the "Session idle timeout" setting so a tenant admin can set it as high as 96 hours (5,760 minutes), with larger values refused; a value above 24 hours saved earlier, which was ignored until this release, now applies, and the 24-hour default is unchanged.
  * Added connector management to the Group configuration pages: tenant admins and organization owners can add, override, or remove connectors for one directory group instead of only for the whole tenant or organization, and these changes appear as new activity types in the Compliance API feed.
</Update>

<Update label="2026.08.25.2">
  * Fixed adding a plugin or marketplace under Config > Integrations > Plugins failing with "Something went wrong" for all but the smallest zip files.
  * Added text alternatives to the charts on the Admin Console's Analytics page: screen readers announce each chart by name and can read its plotted values as a table.
</Update>

<Update label="2026.08.25.1">
  * Fixed the "By product" table on the Analytics page counting Claude for Microsoft 365 activity as "Unknown".
</Update>

<Update label="2026.08.24.1">
  * Fixed Admin Console pages cutting off setting names, values, and buttons at high browser zoom or in narrow windows; content now wraps instead of scrolling sideways.
  * Added two settings under Config > Compliance and telemetry: "Application event level (Claude Desktop)" chooses how much of Claude Desktop's application event log goes to your telemetry collector, and "Telemetry resource attributes (Claude Desktop)" adds your own labels to every record.
</Update>
