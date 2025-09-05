# Data usage

> Learn about Anthropic's data usage policies for Claude

## Data policies

### Data training policy

**Consumer users (Free, Pro, and Max plans)**:
Starting August 28, 2025, we're giving you the choice to allow your data to be used to improve future Claude models.

We will train new models using data from Free, Pro, and Max accounts when this setting is on (including when you use Claude Code from these accounts).

* If you're a current user, you can select your preference now and your selection will immediately go into effect.
  This setting will only apply to new or resumed chats and coding sessions on Claude. Previous chats with no additional activity will not be used for model training.
* You have until September 28, 2025 to make your selection.
  If you're a new user, you can pick your setting for model training during the signup process.
  You can change your selection at any time in your Privacy Settings.

**Commercial users**: (Team and Enterprise plans, API, 3rd-party platforms, and Claude Gov) maintain existing policies: Anthropic does not train generative models using code or prompts sent to Claude Code under commercial terms, unless the customer has chosen to provide their data to us for model improvement (e.g. [Developer Partner Program](https://support.anthropic.com/en/articles/11174108-about-the-development-partner-program)).

### Development Partner Program

If you explicitly opt in to methods to provide us with materials to train on, such as via the [Development Partner Program](https://support.anthropic.com/en/articles/11174108-about-the-development-partner-program), we may use those materials provided to train our models. An organization admin can expressly opt-in to the Development Partner Program for their organization. Note that this program is available only for Anthropic first-party API, and not for Bedrock or Vertex users.

### Feedback using the `/bug` command

If you choose to send us feedback about Claude Code using the `/bug` command, we may use your feedback to improve our products and services. Transcripts shared via `/bug` are retained for 30 days.

### Data retention

Anthropic retains Claude Code data based on your account type and preferences.

**Consumer users (Free, Pro, and Max plans)**:

* Users who allow data use for model improvement: 5-year retention period to support model development and safety improvements
* Users who don't allow data use for model improvement: 30-day retention period
* Privacy settings can be changed at any time at [claude.ai/settings/data-privacy-controls](claude.ai/settings/data-privacy-controls).

**Commercial users (Team, Enterprise, and API)**:

* Standard: 30-day retention period
* Zero data retention: Available with appropriately configured API keys - Claude Code will not retain chat transcripts on servers
* Local caching: Claude Code clients may store sessions locally for up to 30 days to enable session resumption (configurable)

Learn more about data retention practices in our [Privacy Center](https://privacy.anthropic.com/).

For full details, please review our [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) (for Team, Enterprise, and API users) or [Consumer Terms](https://www.anthropic.com/legal/consumer-terms) (for Free, Pro, and Max users) and [Privacy Policy](https://www.anthropic.com/legal/privacy).

## Data flow and dependencies

<img src="https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/claude-code-data-flow.png?fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=413237a4d6564f162590c4fea074f234" alt="Claude Code data flow diagram" width="1597" height="1285" data-path="images/claude-code-data-flow.png" srcset="https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/claude-code-data-flow.png?w=280&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=dcb43f2e6408c33275a51747682804b2 280w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/claude-code-data-flow.png?w=560&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=f5bb343bddf038c62c8c7c8ff574df37 560w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/claude-code-data-flow.png?w=840&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=a25ba8e1c632bb02de4cf68e96ac5a8c 840w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/claude-code-data-flow.png?w=1100&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=434fb120de78f63df663268636485646 1100w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/claude-code-data-flow.png?w=1650&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=9baeb74ab4c1c8255e510c2c8b521e32 1650w, https://mintcdn.com/anthropic/PF_69UDRSEsLpN9D/images/claude-code-data-flow.png?w=2500&fit=max&auto=format&n=PF_69UDRSEsLpN9D&q=85&s=f4314f4067f037b57fe851d063ac2b77 2500w" data-optimize="true" data-opv="2" />

Claude Code is installed from [NPM](https://www.npmjs.com/package/@anthropic-ai/claude-code). Claude Code runs locally. In order to interact with the LLM, Claude Code sends data over the network. This data includes all user prompts and model outputs. The data is encrypted in transit via TLS and is not encrypted at rest. Claude Code is compatible with most popular VPNs and LLM proxies.

Claude Code is built on Anthropic's APIs. For details regarding our API's security controls, including our API logging procedures, please refer to compliance artifacts offered in the [Anthropic Trust Center](https://trust.anthropic.com).

## Telemetry services

Claude Code connects from users' machines to the Statsig service to log operational metrics such as latency, reliability, and usage patterns. This logging does not include any code or file paths. Data is encrypted in transit using TLS and at rest using 256-bit AES encryption. Read more in the [Statsig security documentation](https://www.statsig.com/trust/security). To opt out of Statsig telemetry, set the `DISABLE_TELEMETRY` environment variable.

Claude Code connects from users' machines to Sentry for operational error logging. The data is encrypted in transit using TLS and at rest using 256-bit AES encryption. Read more in the [Sentry security documentation](https://sentry.io/security/). To opt out of error logging, set the `DISABLE_ERROR_REPORTING` environment variable.

When users run the `/bug` command, a copy of their full conversation history including code is sent to Anthropic. The data is encrypted in transit and at rest. Optionally, a Github issue is created in our public repository. To opt out of bug reporting, set the `DISABLE_BUG_COMMAND` environment variable.

## Default behaviors by API provider

By default, we disable all non-essential traffic (including error reporting, telemetry, and bug reporting functionality) when using Bedrock or Vertex. You can also opt out of all of these at once by setting the `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` environment variable. Here are the full default behaviors:

| Service                            | Anthropic API                                            | Vertex API                                            | Bedrock API                                            |
| ---------------------------------- | -------------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------ |
| **Statsig (Metrics)**              | Default on.<br />`DISABLE_TELEMETRY=1` to disable.       | Default off.<br />`CLAUDE_CODE_USE_VERTEX` must be 1. | Default off.<br />`CLAUDE_CODE_USE_BEDROCK` must be 1. |
| **Sentry (Errors)**                | Default on.<br />`DISABLE_ERROR_REPORTING=1` to disable. | Default off.<br />`CLAUDE_CODE_USE_VERTEX` must be 1. | Default off.<br />`CLAUDE_CODE_USE_BEDROCK` must be 1. |
| **Anthropic API (`/bug` reports)** | Default on.<br />`DISABLE_BUG_COMMAND=1` to disable.     | Default off.<br />`CLAUDE_CODE_USE_VERTEX` must be 1. | Default off.<br />`CLAUDE_CODE_USE_BEDROCK` must be 1. |

All environment variables can be checked into `settings.json` ([read more](/en/docs/claude-code/settings)).
