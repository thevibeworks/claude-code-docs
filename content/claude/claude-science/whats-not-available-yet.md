> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# What's not available yet

> Claude Science is in beta, and some admin controls you use with other Claude products don't govern it yet.

Claude Science is in beta, and some admin controls you use with other Claude products don't govern it yet. The setup wizard lists some of these when you enable the product; this page has the full detail. See [Admin controls](/docs/claude-science/admin-controls) for the complete per-setting table.

## Audit and compliance

Audit log: no Claude Science events are written to the organization audit log yet. This is on the roadmap.\
Compliance API: admins can't export or delete Claude Science data through the Compliance API. Because conversations live on members' computers, there's no Anthropic-side data for the API to reach; see [Manage on devices](/docs/claude-science/manage-on-devices) for endpoint-level options.\
Org data export: the organization export doesn't include data stored on members' computers.

## Data retention

Custom Data Retention: your auto-delete window applies to conversations, projects, and artifacts stored on Anthropic's servers. Claude Science doesn't store that data on Anthropic's servers, so the setting has nothing to act on.\
Local deletion signal: when a member deletes local Claude Science data, Anthropic isn't notified to drop the matching server-side model-traffic log early. The log still expires under Anthropic's standard retention.

## Connector and domain allowlists

Your organization's connector and domain allowlists apply to Directory connectors you publish, but don't restrict connectors a member adds locally (running on their own computer or pointing at a custom URL). Adding admin control over local and custom connectors is on the roadmap. Skills allowlists work the same way: org-published skills are visible; there's no admin control over which featured skills members can enable.

## Session duration

Your session-duration setting limits the browser sign-in step only. After a member signs in, the app holds its own token and stays signed in beyond that window.

## Offboarding

Removing a member from your organization revokes their ability to sign in, but doesn't wipe Claude Science data already on their computer. Use your device management software to handle local data on offboarding.
