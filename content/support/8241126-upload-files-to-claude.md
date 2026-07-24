# Upload files to Claude

This article explains how to upload documents and images to Claude, including supported file types, size limits, and how to get started.

## Supported file types

### Documents

Claude can work with the following document types:

- PDF

- DOCX

- CSV

- TXT

- HTML

- ODT

- RTF

- EPUB

- JSON

- XLSX*

**Note:** You must enable **[code execution and file creation](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude#h_1c99382190)** in your account to upload XLSX files.

### Images

Claude supports the following image formats:

- JPEG

- PNG

- GIF

- WebP

---

## How to upload files

You can upload files to Claude in several ways:

1. Click the "+" button in the lower left corner of the chat box

2. Select "Add files or photos" from the menu.

3. Choose files from your device for upload.

4. Click "Open" to attach the files, or drag and drop the files directly into the chat window.

5. You can also copy images and paste them from your clipboard into Claude.

Files can be uploaded to individual chats or uploaded to a project's **Files** section for persistent reference across conversations.

---

## File limits

### Chat uploads

- **File size:** 500MB per file

- **Number of files:** Up to 20 files per chat

- **Image dimensions:** Up to 8000x8000 pixels

- **Number of pages:** PDFs are limited to 1000 pages

### Project files

- **File size:** 30MB per file

- **Number of files:** Unlimited, but total content must fit within Claude's context window

- **Content type:** Text extraction only (except for multimodal PDFs)

**Note:** Additional token limits may apply based on the length of extracted content.

---

## PDF processing

Claude analyzes both text and visual elements (like images, charts, and graphics) in PDFs of 100 pages or fewer. For PDFs from 101 to 1000 pages, Claude processes text only and doesn't analyze visual elements. You can't upload PDFs over 1000 pages. If you try, you'll see an "Uploaded file is too large" error.

---

## Tips for best results

**For images:** Use images that are 1000x1000 pixels or larger. Avoid small or low-resolution images where possible.

**For PDFs:** When referring to specific pages, use the PDF page numbers as shown in your PDF viewer, not the page numbers printed on the document itself.

**For large documents:** If you're working with larger files, consider dividing them into smaller sections to stay within limits.

**For non-PDF documents:** Claude extracts text only from these files. If they contain embedded images, Claude won't be able to read or interpret them.