> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# How Claude Science works with your data

> What Claude Science keeps on your computers, what it sends to Anthropic and how long Anthropic keeps it, who can access it, Anthropic's no-training and ownership commitments, and the controls available to your organization.

Claude Science is client-side software that your organization installs and runs on computers it controls, and Anthropic provides the Claude models the app calls. This page covers what that means for your research data.

## Model training and ownership of your work

On Team and Enterprise plans the [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) apply. Under them Anthropic "may not train models on Customer Content from Services," and, as between the parties and to the extent permitted by applicable law, your organization "retains all rights to its Inputs" and "owns its Outputs," including the analyses, code, and results your researchers produce with Claude Science. Anthropic may use content to improve its models only when a member gives express consent, by providing feedback, which includes a copy of that conversation, or when your organization otherwise expressly chooses to allow it (see [Is my data used for model training?](https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training)). To turn off the ability for your researchers to provide feedback, an Owner can turn off the **Rate chats** toggle under **Organization settings** > **Data and privacy**.

On Pro and Max plans the [Consumer Terms of Service](https://www.anthropic.com/legal/consumer-terms), [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy), and your Claude privacy settings in the Settings panel apply (see [Legal and compliance](/docs/claude-science/legal-and-compliance)).

## Where Claude Science data lives

| Where                                         | What                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| The computer running Claude Science           | Conversation history, project files and artifacts, saved memory, settings, and stored credentials, in a local folder Anthropic doesn't host or sync (see [Manage Claude Science on devices](/docs/claude-science/manage-on-devices))                                                                                                                                                                |
| Anthropic                                     | The items listed under [What Anthropic receives](#what-anthropic-receives)                                                                                                                                                                                                                                                                                                                     |
| Services your organization or members connect | Jobs, files, and queries sent to your SSH hosts, your Modal account, scientific model endpoints, cloud storage, and the external services that local (Featured and custom) connectors, sandboxed code, and remote jobs call, directly from the computer or your own compute and without passing through Anthropic (see [Admin controls](/docs/claude-science/admin-controls#organization-settings)) |

Sign-in tokens and the credentials members store for compute and cloud storage are encrypted on the computer, and the rest of the local folder relies on operating-system permissions, so apply your full-disk encryption and device management policies to it.

## What Anthropic receives

The app sends the following to Anthropic, over TLS and signed in with the member's Claude account (see [Network requirements](/docs/claude-science/network-requirements#app-connections) for the domains):

* **Requests to Claude** every time Claude responds, carrying the conversation so far, including the member's prompts, the contents of files Claude has read (PDFs included), code and command output, connector results, images Claude is shown, and recalled memory facts. Anthropic keeps these as model-call logs (see [What Anthropic keeps and for how long](#what-anthropic-keeps-and-for-how-long)).
* **Web search queries**, run by Anthropic's web search service through a third-party search provider listed among [Anthropic's subprocessors](https://www.anthropic.com/subprocessors).
* **Dictation audio**, streamed to Anthropic's speech-to-text service only while a member dictates. If the app can't use that service while Claude Science is open in a browser such as Chrome or Edge, it falls back to the browser's built-in speech recognition, and that browser's vendor then processes the audio.
* **Feedback**, only when a member sends it, consisting of the rating, the comment, and a copy of that conversation (members are reminded before submission) with known credential formats and email addresses redacted. Not accepted from organizations with HIPAA compliance or customer-managed encryption keys.
* **Custom skills a member publishes**, stored with the member's claude.ai skills.
* **Usage telemetry and error reports**, which carry app, device, and timing data, plus account and organization identifiers on telemetry events, but no conversation content, file contents, or file names (see [Telemetry](/docs/claude-science/manage-on-devices#telemetry) for the device setting that turns them, and feedback, off).
* **Calls to connectors Anthropic hosts** from your claude.ai connector directory, which pass through Anthropic's connector service as in claude.ai, plus routine account, settings, and update traffic.

## What Anthropic keeps and for how long

For Team and Enterprise organizations, Anthropic processes this data under the [Data Processing Addendum](https://www.anthropic.com/legal/data-processing-addendum), encrypted at rest and in transit. Model-call logs follow Anthropic's [commercial data retention policy](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data), including its longer retention for content flagged by automated trust and safety systems or required by law.

Requests to models designated [Covered Models](https://support.claude.com/en/articles/15425695-covered-models) are retained for 30 days to support Anthropic's safety work, as [Data retention practices for Covered Models](https://support.claude.com/en/articles/15425996-data-retention-practices-for-covered-models) describes. Feedback submissions are kept under the feedback terms in the same policy.

## Who at Anthropic can access retained content

Human review of model-call logs, published skills, or Compliance API transcripts requires a specific reason, such as reviewing content that automated safety systems flagged, responding to a security incident, or meeting a legal obligation, through a controlled path where access is restricted to personnel whose role requires it and logged as the [Data Processing Addendum](https://www.anthropic.com/legal/data-processing-addendum) describes, and content reviewed this way isn't used to train Claude models. Feedback a member chooses to send is handled separately, as [Model training and ownership of your work](#model-training-and-ownership-of-your-work) describes. [Access Transparency](https://platform.claude.com/docs/en/manage-claude/access-transparency) records don't cover the Claude apps, including Claude Science.

## Controls available to your organization

* **Organization settings** for connectors, skills, the sandbox network allowlist, SSH hosts, Modal, model endpoints, memory, and access to previously saved Claude Science work (see [Admin controls](/docs/claude-science/admin-controls)). There is no organization setting for web search, dictation, or telemetry.
* **US-only inference** (usage-based Enterprise plans) runs model inference for Claude Science requests in the United States, as for your other Claude apps (see [Enable US-only inference](https://support.claude.com/en/articles/15422948-enable-us-only-inference-for-your-organization)).
* **Device configuration** turns off telemetry, error reports, and feedback and relocates the local data folder (see [Manage Claude Science on devices](/docs/claude-science/manage-on-devices)).
* **Running Claude Science next to your data**, on a Linux server or virtual machine you control, keeps datasets on your infrastructure, apart from what Claude reads into the conversation, while Claude's inference runs on Anthropic's service (see [Run on a remote Linux server](/docs/claude-science/run-on-remote-linux-server)).
* **Usage analytics** show adoption and session metrics without conversation content (see [Monitor usage](/docs/claude-science/monitor-usage)).

## Compliance API coverage

On Enterprise plans with the [Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api) enabled, your organization gets a record of Claude Science settings changes and its own read-only transcripts of members' Claude Science sessions (coverage is in beta), which are kept for your organization's own retention period (6 years by default) and, in organizations that use customer-managed encryption keys, encrypted under your key. [Retrieve session transcripts](https://platform.claude.com/docs/en/manage-claude/compliance-sessions) describes what a transcript contains and which sessions aren't captured, including those in organizations with HIPAA compliance enabled.

## Customer-managed encryption keys

Organizations that use [customer-managed encryption keys (CMEK)](https://platform.claude.com/docs/en/manage-claude/cmek) can turn on Claude Science. The content Anthropic stores from the app is encrypted under your key, including the model-call logs of members' conversations with Claude, skills members publish, and, for Enterprise organizations with the Compliance API enabled, session transcripts.

The app's conversation history, files, artifacts, and memory are stored on the member's computer and aren't hosted by Anthropic; of these, only what the app sends to Claude reaches Anthropic, where your key covers it as this section describes. Work members send to their own SSH hosts, Modal account, or scientific model endpoints goes directly there, not through Anthropic, and isn't under your key or any Anthropic-managed key, so review those providers' data handling. You can turn these connections off under **Organization settings** > **Claude Science**.

In organizations with CMEK enabled, the app hides its response rating buttons and feedback form, as claude.ai does.

## What isn't available for Claude Science

Zero data retention (a Claude Code zero-data-retention arrangement covers Claude Code sessions, not Claude Science), Enterprise Frontier Safeguards, coverage under Anthropic's Business Associate Agreement (keep protected health information out of Claude Science), and inference through a third-party cloud platform or your own cloud tenancy aren't available for Claude Science. See [Admin controls](/docs/claude-science/admin-controls#how-other-admin-settings-apply-to-claude-science) for how the other claude.ai admin settings apply to the app.

## Related resources

[Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms), [Data Processing Addendum](https://www.anthropic.com/legal/data-processing-addendum), [subprocessor list](https://www.anthropic.com/subprocessors), [Usage Policy](https://www.anthropic.com/legal/aup), the [Anthropic Trust Center](https://trust.anthropic.com) for certifications and security documentation, and [Admin controls](/docs/claude-science/admin-controls).
