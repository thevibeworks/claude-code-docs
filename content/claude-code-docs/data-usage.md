# Data usage

> Learn about Anthropic's data usage policies for Claude

## Data policies

### Data training policy

By default, Anthropic does not train generative models using code or prompts that are sent to Claude Code.

We aim to be fully transparent about how we use your data. We may use feedback to improve our products and services, but we will not train generative models using your feedback from Claude Code.

### Development Partner Program

If you explicitly opt in to methods to provide us with materials to train on, such as via the [Development Partner Program](https://support.anthropic.com/en/articles/11174108-about-the-development-partner-program), we may use those materials provided to train our models. An organization admin can expressly opt-in to the Development Partner Program for their organization. Note that this program is available only for Anthropic first-party API, and not for Bedrock or Vertex users.

### Feedback transcripts

If you choose to send us feedback about Claude Code, such as transcripts of your usage, Anthropic may use that feedback to debug related issues and improve Claude Code's functionality (e.g., to reduce the risk of similar bugs occurring in the future). We will not train generative models using this feedback. Given their potentially sensitive nature, we store user feedback transcripts for only 30 days.

### Data retention

You can use an API key from a zero data retention organization. When doing so, Claude Code will not retain your chat transcripts on our servers. Users' local Claude Code clients may store sessions locally for up to 30 days so that users can resume them. This behavior is configurable.

### Privacy safeguards

We have implemented several safeguards to protect your data, including:

* Limited retention periods for sensitive information
* Restricted access to user session data
* Clear policies against using feedback for model training

For full details, please review our [Commercial Terms of Service](https://www.anthropic.com/legal/commercial-terms) and [Privacy Policy](https://www.anthropic.com/legal/privacy).

## Data flow and dependencies

<img src="https://mintcdn.com/anthropic/images/claude-code-data-flow.png?maxW=1597&auto=format&n=TJyVEsJNS7-wcDQw&q=85&s=fa613fe5084e8c714de3e8251344135d" alt="Claude Code data flow diagram" width="1597" height="1285" data-path="images/claude-code-data-flow.png" srcset="https://mintcdn.com/anthropic/images/claude-code-data-flow.png?w=280&maxW=1597&auto=format&n=TJyVEsJNS7-wcDQw&q=85&s=9b98f9447b3fa42f12bdabf890062c72 280w, https://mintcdn.com/anthropic/images/claude-code-data-flow.png?w=560&maxW=1597&auto=format&n=TJyVEsJNS7-wcDQw&q=85&s=edc5e1f783fae53f9067ba51dcb87d87 560w, https://mintcdn.com/anthropic/images/claude-code-data-flow.png?w=840&maxW=1597&auto=format&n=TJyVEsJNS7-wcDQw&q=85&s=b675e341c4797dbfe8a1c2d32838b6c8 840w, https://mintcdn.com/anthropic/images/claude-code-data-flow.png?w=1100&maxW=1597&auto=format&n=TJyVEsJNS7-wcDQw&q=85&s=e0c22bc2577235900e7b08b351ce9d59 1100w, https://mintcdn.com/anthropic/images/claude-code-data-flow.png?w=1650&maxW=1597&auto=format&n=TJyVEsJNS7-wcDQw&q=85&s=174115b36520b289b985968bf90ad1d7 1650w, https://mintcdn.com/anthropic/images/claude-code-data-flow.png?w=2500&maxW=1597&auto=format&n=TJyVEsJNS7-wcDQw&q=85&s=753faf09b799b3087fdda86d86796a36 2500w" data-optimize="true" data-opv="2" />

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
