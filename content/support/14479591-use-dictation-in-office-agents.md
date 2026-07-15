# Use dictation in Office agents

Dictation lets you speak your prompts instead of typing them when using Office agents. Click the microphone icon in the chat input, speak, and your words appear in the composer as you talk.

Dictation is available for organizations that sign in with Claude directly. It isn't available when Office agents is configured with third-party authentication such as a gateway, Vertex AI, or Bedrock. See below for more information.

## How it works

When you click the microphone, Office agents streams your audio to Anthropic's transcription service, the same infrastructure that powers dictation in the Claude apps. The transcribed text appears in the composer in real time. Click the microphone again to stop, or press Enter to stop and send in one step.

Nothing is transcribed on your device, and your audio isn’t sent to any third-party service. Audio is processed entirely on Anthropic’s infrastructure and isn’t retained; only the resulting text remains in your composer.

## Use dictation

- Click the microphone icon on the right side of the chat input. The placeholder changes to *Listening...* and the button turns blue.

- Speak your prompt. Your words appear in the composer as you talk.

- Click the microphone again to stop, or press Enter to stop and send in one step.

- To choose a different microphone, hover over the microphone icon and click the arrow that appears.

## Why dictation isn't available with third-party authentication

In third-party environments, Office agents do not send prompts to Anthropic directly. Spoken audio is effectively a prompt, so dictation isn’t offered there. If you need voice input in a third-party environment, use the dictation feature built into your operating system or Office application instead.