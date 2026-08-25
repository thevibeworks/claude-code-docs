> ## Documentation Index
> Fetch the complete documentation index at: https://claude.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Annotations

> Annotations let you attach comments to specific parts of an artifact instead of describing a location in prose.

Annotations let you attach comments to specific parts of an artifact instead of describing a location in prose. Select text in a Markdown, plain-text, LaTeX, or code file; select text in a PDF (one page at a time); click a point on an image or figure; or turn on **Annotate** and click an element in a rendered HTML report. Tables and other artifact types can't be annotated. Session transcripts can also be annotated.

## Leaving an annotation

* Select content and click the **Annotate** pill.
* Type your comment and press Cmd/Ctrl+Enter (or click **Save**).
* The annotation appears as a highlighted badge (text) or numbered pin (images). Hover to read it; click to **Edit** or **Delete**.

## Sending annotations to Claude

Saving an annotation doesn't send it. Pending annotations collect in an **N comments** chip on the composer and are sent with your next message. This lets you batch several annotations and send them together, or send them one at a time. Claude receives each annotation with its filename, the quoted selection (or marked image), and your note.

Once sent, annotations are consumed: they leave the artifact and appear as cards on the message. Annotations don't have threads or a resolve state. To revise an artifact again after Claude updates it, annotate the new version.

Limits: annotation text is capped at 1,000 characters. PDF selections can't cross page breaks. Annotations aren't included in downloads and don't appear in the **Files** grid.
