> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Use dictation in Claude for M365

> Speak your prompts instead of typing them in Claude for Excel, PowerPoint, Word, and Outlook.

Dictation lets you speak prompts instead of typing them. Click the
microphone icon in the chat input, speak, and see your words appear in
the composer in real time.

<Note>
  Dictation requires the desktop version of Excel, PowerPoint, Word, or
  Outlook. It is not available in Office on the web because browser-hosted
  add-ins cannot access the microphone. On the web, use your operating
  system's built-in dictation or your Office application's dictation
  feature instead.

  Dictation is also available only for organizations using direct Claude
  authentication. It is not supported when Claude for M365 connects through
  a third-party platform such as Amazon Bedrock, Google Cloud Vertex AI,
  Azure AI Foundry, or an LLM gateway. See
  [Use Claude for M365 with third-party platforms](/docs/office-agents/third-party-platforms)
  for platform support details.
</Note>

## Use dictation

<Steps>
  <Step title="Start listening">
    Click the microphone icon on the right side of the chat input. The
    placeholder changes to "Listening..." and the button highlights.
  </Step>

  <Step title="Speak your prompt">
    Words appear in the composer as you talk.
  </Step>

  <Step title="Stop or send">
    Click the microphone again to stop, or press Enter to stop and send
    in one step.
  </Step>
</Steps>

To select a different microphone, hover over the microphone icon and
click the arrow that appears.

## How it works

When you start dictating, the add-in streams your audio to Anthropic's
transcription service, the same infrastructure that powers dictation in
the Claude apps. The transcribed text displays in real time in the
composer.

Nothing is transcribed on your device. Audio is streamed to Anthropic,
which uses a contracted speech-to-text subprocessor to generate the
transcript. Audio is not retained after transcription; only the
resulting text remains in your composer.

## Why dictation is not available with third-party authentication

In third-party environments, Claude for M365 does not send prompts to
Anthropic directly. Spoken audio is effectively a prompt, so dictation
is not offered there. Use your operating system's built-in dictation or
your Office application's dictation feature instead.
