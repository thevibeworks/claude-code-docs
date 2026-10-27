---
title: Legal summarization
url: https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization
description: This guide walks through how to use Claude's advanced natural language processing capabilities to efficiently summarize legal documents, extracting key information and expediting legal research. With Claude, you can streamline the review of contracts, litigation prep, and regulatory work, saving time and ensuring accuracy in your legal processes.
---

> Visit the [summarization recipe](https://platform.claude.com/cookbook/capabilities-summarization-guide) in the Claude Cookbook to see an example legal summarization implementation using Claude.

## Before building with Claude

### Decide whether to use Claude for legal summarization

Here are some key indicators that you should employ an LLM such as Claude to summarize legal documents:

<AccordionGroup>
  <Accordion title="You want to review a high volume of documents efficiently and affordably">
    Large-scale document review can be time-consuming and expensive when done manually. Claude can process and summarize vast amounts of legal documents rapidly, significantly reducing the time and cost associated with document review. This capability is particularly valuable for tasks such as due diligence, contract analysis, or litigation discovery, where efficiency is crucial.
  </Accordion>

  <Accordion title="You need automated extraction of key metadata">
    Claude can efficiently extract and categorize important metadata from legal documents, such as parties involved, dates, contract terms, or specific clauses. This automated extraction can help organize information, making it easier to search, analyze, and manage large document sets. It’s especially useful for contract management, compliance checks, or creating searchable databases of legal information. 
  </Accordion>

  <Accordion title="You want to generate clear, concise, and standardized summaries">
    Claude can generate structured summaries that follow predetermined formats, making it easier for legal professionals to quickly grasp the key points of various documents. These standardized summaries can improve readability, facilitate comparison between documents, and enhance overall comprehension, especially when dealing with complex legal language or technical jargon.
  </Accordion>

  <Accordion title="You need precise citations for your summaries">
    When creating legal summaries, proper attribution and citation are crucial to ensure credibility and compliance with legal standards. Claude can be prompted to include accurate citations for all referenced legal points, making it easier for legal professionals to review and verify the summarized information.
  </Accordion>

  <Accordion title="You want to streamline and expedite your legal research process">
    Claude can help with legal research by quickly analyzing large volumes of case law, statutes, and legal commentary. It can identify relevant precedents, extract key legal principles, and summarize complex legal arguments. This capability can significantly speed up the research process, allowing legal professionals to focus on higher-level analysis and strategy development.
  </Accordion>
</AccordionGroup>

### Determine the details you want the summarization to extract

There is no single correct summary for any given document. Without clear direction, it can be difficult for Claude to determine which details to include. To achieve optimal results, identify the specific information you want to include in the summary.

For instance, when summarizing a sublease agreement, you might want to extract the following key points:

<CodeGroup exclude="shell">
  ```python Python
  details_to_extract = [
      "Parties involved (sublessor, sublessee, and original lessor)",
      "Property details (address, description, and permitted use)",
      "Term and rent (start date, end date, monthly rent, and security deposit)",
      "Responsibilities (utilities, maintenance, and repairs)",
      "Consent and notices (landlord's consent, and notice requirements)",
      "Special provisions (furniture, parking, and subletting restrictions)",
  ]
  ```

  ```typescript TypeScript
  const detailsToExtract = [
    "Parties involved (sublessor, sublessee, and original lessor)",
    "Property details (address, description, and permitted use)",
    "Term and rent (start date, end date, monthly rent, and security deposit)",
    "Responsibilities (utilities, maintenance, and repairs)",
    "Consent and notices (landlord's consent, and notice requirements)",
    "Special provisions (furniture, parking, and subletting restrictions)"
  ];
  ```

  ```csharp C#
  List<string> detailsToExtract =
  [
      "Parties involved (sublessor, sublessee, and original lessor)",
      "Property details (address, description, and permitted use)",
      "Term and rent (start date, end date, monthly rent, and security deposit)",
      "Responsibilities (utilities, maintenance, and repairs)",
      "Consent and notices (landlord's consent, and notice requirements)",
      "Special provisions (furniture, parking, and subletting restrictions)",
  ];
  ```

  ```go Go
  var detailsToExtract = []string{
  	"Parties involved (sublessor, sublessee, and original lessor)",
  	"Property details (address, description, and permitted use)",
  	"Term and rent (start date, end date, monthly rent, and security deposit)",
  	"Responsibilities (utilities, maintenance, and repairs)",
  	"Consent and notices (landlord's consent, and notice requirements)",
  	"Special provisions (furniture, parking, and subletting restrictions)",
  }
  ```

  ```java Java
  List<String> detailsToExtract = List.of(
      "Parties involved (sublessor, sublessee, and original lessor)",
      "Property details (address, description, and permitted use)",
      "Term and rent (start date, end date, monthly rent, and security deposit)",
      "Responsibilities (utilities, maintenance, and repairs)",
      "Consent and notices (landlord's consent, and notice requirements)",
      "Special provisions (furniture, parking, and subletting restrictions)");
  ```

  ```php PHP
  $detailsToExtract = [
      'Parties involved (sublessor, sublessee, and original lessor)',
      'Property details (address, description, and permitted use)',
      'Term and rent (start date, end date, monthly rent, and security deposit)',
      'Responsibilities (utilities, maintenance, and repairs)',
      "Consent and notices (landlord's consent, and notice requirements)",
      'Special provisions (furniture, parking, and subletting restrictions)',
  ];
  ```

  ```ruby Ruby
  details_to_extract = [
    "Parties involved (sublessor, sublessee, and original lessor)",
    "Property details (address, description, and permitted use)",
    "Term and rent (start date, end date, monthly rent, and security deposit)",
    "Responsibilities (utilities, maintenance, and repairs)",
    "Consent and notices (landlord's consent, and notice requirements)",
    "Special provisions (furniture, parking, and subletting restrictions)"
  ]
  ```
</CodeGroup>

### Establish success criteria

Evaluating the quality of summaries is a notoriously challenging task. Unlike many other natural language processing tasks, evaluation of summaries often lacks clear-cut, objective metrics. The process can be highly subjective, with different readers valuing different aspects of a summary. Here are criteria you might want to consider when assessing how well Claude performs legal summarization.

<AccordionGroup>
  <Accordion title="Factual correctness">
    The summary should accurately represent the facts, legal concepts, and key points in the document.
  </Accordion>

  <Accordion title="Legal precision">
    Terminology and references to statutes, case law, or regulations must be correct and aligned with legal standards.
  </Accordion>

  <Accordion title="Conciseness">
     The summary should condense the legal document to its essential points without losing important details.
  </Accordion>

  <Accordion title="Consistency">
    If summarizing multiple documents, the LLM should maintain a consistent structure and approach to each summary.
  </Accordion>

  <Accordion title="Readability">
    The text should be clear and easy to understand. If the audience is not legal experts, the summarization should not include legal jargon that could confuse the audience.
  </Accordion>

  <Accordion title="Bias and fairness">
    The summary should present an unbiased and fair depiction of the legal arguments and positions.
  </Accordion>
</AccordionGroup>

See the guide on [establishing success criteria](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests) for more information.

***

## How to summarize legal documents using Claude

### Select the right Claude model

Model accuracy is extremely important when summarizing legal documents. Claude Opus 5.5 is an excellent choice for use cases such as this where high accuracy is required. If the size and quantity of your documents are large such that costs start to become a concern, you can also try using a smaller model such as Claude Haiku 5.5.

To help estimate these costs, the following is a comparison of the cost to summarize 1,000 sublease agreements using Opus and Haiku models:

* **Content size**

  * Number of agreements: 1,000
  * Characters per agreement: 300,000
  * Total characters: 300M

* **Estimated tokens**

  * Input tokens: 108M, about 108,000 per agreement (about 1 token per 2.8 characters, the rate both models showed on this guide’s sample agreement)
  * Output tokens per summary, including any thinking tokens, which are billed as output: about 6,200 on Claude Opus 5.5 and 3,100 on Claude Haiku 5.5
  * Total output tokens: 6.2M on Claude Opus 5.5 and 3.1M on Claude Haiku 5.5

* **Claude Opus 5.5 estimated cost**

  * Input token cost: 108 MTok \* $4.00/MTok = $432.00 USD
  * Output token cost: 6.2 MTok \* $20.00/MTok = $124.00 USD
  * Total cost: $432.00 + $124.00 = $556.00 USD

* **Claude Haiku 5.5 estimated cost**, at its prices for prompts over 100,000 tokens

  * Input token cost: 108 MTok \* $0.50/MTok = $54.00 USD
  * Output token cost: 3.1 MTok \* $2.50/MTok = $7.75 USD
  * Total cost: $54.00 + $7.75 = $61.75 USD

<Tip>
  Actual costs might differ from these estimates. The token counts come from running the example in the 

  [Build a strong prompt](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization#build-a-strong-prompt)

   section on this guide’s sample agreement, about 105,000 input tokens, and output length varies with the document and from run to run. Each agreement here is one prompt of about 108,000 tokens, over the 100,000-token threshold of Claude Haiku 5.5’s 

  [long-prompt prices](https://platform.claude.com/docs/en/about-claude/pricing#long-context-pricing)

  . A document whose prompt stays at or under 100,000 tokens pays $0.10 / $0.50 USD per million input / output tokens instead. To see which prices apply, count your documents with 

  [token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting)

   and 

  `model`

   set to 

  `claude-haiku-5-5`

  .
</Tip>

### Transform documents into a format that Claude can process

Before you start summarizing documents, you need to prepare your data. This involves extracting text from PDFs, cleaning the text, and ensuring it’s ready to be processed by Claude.

Here is a demonstration of this process on a sample PDF:

<CodeGroup exclude="shell">
  <CodeGroupItem language="cURL">
    Extract the text from the PDF in code.
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    Extract the text from the PDF in code.
  </CodeGroupItem>

  ```python Python
  from io import BytesIO
  import re

  import pypdf
  import requests


  def get_llm_text(pdf_file):
      reader = pypdf.PdfReader(pdf_file)
      text = "\n".join([page.extract_text() for page in reader.pages])

      # Remove page numbers
      text = re.sub(r"\n\s*\d+\s*\n", "\n", text)

      # Remove extra whitespace
      text = re.sub(r"\s+", " ", text)

      return text


  # Create the full URL from the GitHub repository
  url = "https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/capabilities/summarization/data/Sample Sublease Agreement.pdf"
  url = url.replace(" ", "%20")

  # Download the PDF file into memory
  response = requests.get(url)

  # Load the PDF from memory
  pdf_file = BytesIO(response.content)

  document_text = get_llm_text(pdf_file)
  print(document_text[:50000])
  ```

  ```typescript TypeScript
  import { PDFParse } from "pdf-parse";

  async function getLlmText(pdfData: Uint8Array): Promise<string> {
    const parser = new PDFParse({ data: pdfData });
    const result = await parser.getText();
    await parser.destroy();
    let text = result.pages.map((page) => page.text).join("\n");

    // Remove page numbers
    text = text.replace(/\n\s*\d+\s*\n/g, "\n");

    // Remove extra whitespace
    text = text.replace(/\s+/g, " ");

    return text;
  }

  // Download the sample sublease agreement from the Claude Cookbook's summarization recipe
  const response = await fetch(
    "https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/capabilities/summarization/data/Sample%20Sublease%20Agreement.pdf"
  );
  const pdfData = new Uint8Array(await response.arrayBuffer());

  const documentText = await getLlmText(pdfData);
  console.log(documentText.slice(0, 50000));
  ```

  ```csharp C#
  using System.Text.RegularExpressions;
  using UglyToad.PdfPig;
  using UglyToad.PdfPig.DocumentLayoutAnalysis.TextExtractor;

  string GetLlmText(byte[] pdfData)
  {
      using var document = PdfDocument.Open(pdfData);
      var text = string.Join("\n", document.GetPages().Select(page => ContentOrderTextExtractor.GetText(page)));

      // Remove page numbers
      text = Regex.Replace(text, @"\n\s*\d+\s*\n", "\n");

      // Remove extra whitespace
      text = Regex.Replace(text, @"\s+", " ");

      return text;
  }

  // Download the sample sublease agreement from the Claude Cookbook's summarization recipe
  using var httpClient = new HttpClient();
  var pdfData = await httpClient.GetByteArrayAsync(
      "https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/capabilities/summarization/data/Sample%20Sublease%20Agreement.pdf"
  );

  var documentText = GetLlmText(pdfData);
  Console.WriteLine(documentText[..Math.Min(50000, documentText.Length)]);
  ```

  ```go Go
  import (
  	"bytes"
  	"io"
  	"net/http"
  	"regexp"

  	"github.com/ledongthuc/pdf"
  )

  // The text of the sample sublease agreement
  var documentText string

  func getLLMText(pdfData []byte) (string, error) {
  	reader, err := pdf.NewReader(bytes.NewReader(pdfData), int64(len(pdfData)))
  	if err != nil {
  		return "", err
  	}

  	var pages []string
  	for pageIndex := 1; pageIndex <= reader.NumPage(); pageIndex++ {
  		pageText, err := reader.Page(pageIndex).GetPlainText(nil)
  		if err != nil {
  			return "", err
  		}
  		pages = append(pages, pageText)
  	}
  	text := strings.Join(pages, "\n")

  	// Remove page numbers
  	text = regexp.MustCompile(`\n\s*\d+\s*\n`).ReplaceAllString(text, "\n")

  	// Remove extra whitespace
  	text = regexp.MustCompile(`\s+`).ReplaceAllString(text, " ")

  	return text, nil
  }

  // extractDocumentText downloads the sample sublease agreement and extracts its text.
  func extractDocumentText() {
  	// Download the sample sublease agreement from the Claude Cookbook's summarization recipe
  	response, err := http.Get("https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/capabilities/summarization/data/Sample%20Sublease%20Agreement.pdf")
  	if err != nil {
  		log.Fatal(err)
  	}
  	defer response.Body.Close()

  	pdfData, err := io.ReadAll(response.Body)
  	if err != nil {
  		log.Fatal(err)
  	}

  	documentText, err = getLLMText(pdfData)
  	if err != nil {
  		log.Fatal(err)
  	}
  	fmt.Println(documentText[:min(50000, len(documentText))])
  }
  ```

  ```java Java
  import java.io.IOException;
  import java.net.URI;
  import java.net.http.HttpClient;
  import java.net.http.HttpRequest;
  import java.net.http.HttpResponse;
  import org.apache.pdfbox.Loader;
  import org.apache.pdfbox.pdmodel.PDDocument;
  import org.apache.pdfbox.text.PDFTextStripper;

  // The text of the sample sublease agreement
  String documentText;

  String getLlmText(byte[] pdfData) throws IOException {
      try (PDDocument document = Loader.loadPDF(pdfData)) {
          String text = new PDFTextStripper().getText(document);

          // Remove page numbers
          text = text.replaceAll("\\n\\s*\\d+\\s*\\n", "\n");

          // Remove extra whitespace
          return text.replaceAll("\\s+", " ");
      }
  }

  void extractDocumentText() throws IOException, InterruptedException {
      // Download the sample sublease agreement from the Claude Cookbook's summarization recipe
      HttpRequest request = HttpRequest.newBuilder(URI.create(
              "https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/capabilities/summarization/data/Sample%20Sublease%20Agreement.pdf"))
          .build();
      byte[] pdfData;
      try (HttpClient httpClient = HttpClient.newHttpClient()) {
          pdfData = httpClient.send(request, HttpResponse.BodyHandlers.ofByteArray()).body();
      }

      documentText = getLlmText(pdfData);
      IO.println(documentText.substring(0, Math.min(50000, documentText.length())));
  }
  ```

  ```php PHP
  use Smalot\PdfParser\Parser;

  $getLlmText = function (string $pdfData): string {
      $document = (new Parser())->parseContent($pdfData);
      $text = implode("\n", array_map(fn ($page) => $page->getText(), $document->getPages()));

      // Remove page numbers
      $text = preg_replace('/\n\s*\d+\s*\n/', "\n", $text);

      // Remove extra whitespace
      return preg_replace('/\s+/', ' ', $text);
  };

  // Download the sample sublease agreement from the Claude Cookbook's summarization recipe
  $pdfData = file_get_contents(
      'https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/capabilities/summarization/data/Sample%20Sublease%20Agreement.pdf'
  );

  $documentText = $getLlmText($pdfData);
  echo substr($documentText, 0, 50000) . "\n";
  ```

  ```ruby Ruby
  require "net/http"
  require "pdf-reader"
  require "stringio"

  def get_llm_text(pdf_data)
    reader = PDF::Reader.new(StringIO.new(pdf_data))
    text = reader.pages.map(&:text).join("\n")

    # Remove page numbers
    text = text.gsub(/\n\s*\d+\s*\n/, "\n")

    # Remove extra whitespace
    text.gsub(/\s+/, " ")
  end

  # Download the sample sublease agreement from the Claude Cookbook's summarization recipe
  pdf_data = Net::HTTP.get(
    URI("https://raw.githubusercontent.com/anthropics/claude-cookbooks/main/capabilities/summarization/data/Sample%20Sublease%20Agreement.pdf")
  )

  document_text = get_llm_text(pdf_data)
  puts document_text[0, 50_000]
  ```
</CodeGroup>

In this example, you first download a PDF of a sample sublease agreement used in the Claude Cookbook’s [summarization recipe](https://platform.claude.com/cookbook/capabilities-summarization-guide). This agreement was sourced from a publicly available sublease agreement from the [sec.gov website](https://www.sec.gov/Archives/edgar/data/1045425/000119312507044370/dex1032.htm).

The example uses the `pypdf` (typescript: `pdf-parse`; csharp: `PdfPig`; go: `github.com/ledongthuc/pdf`; java: `org.apache.pdfbox:pdfbox`; php: `smalot/pdfparser`; ruby: `pdf-reader`) library to extract the contents of the PDF and convert it to text. The text data is then cleaned by removing page numbers and extra whitespace.

### Build a strong prompt

Claude can adapt to various summarization styles. You can change the details of the prompt to guide Claude to be more or less verbose, include more or less technical terminology, or provide a higher- or lower-level summary of the context at hand.

Here’s an example of how to create a prompt that ensures the generated summaries follow a consistent structure when analyzing sublease agreements:

<CodeGroup exclude="shell">
  <CodeGroupItem language="cURL">
    This workflow needs more logic than a single shell command. Use the Claude SDK to run it.
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    This workflow needs more logic than a single shell command. Use the Claude SDK to run it.
  </CodeGroupItem>

  ```python Python
  # Initialize the Anthropic client
  client = anthropic.Anthropic()


  def summarize_document(
      text, details_to_extract, model="claude-opus-5-5", max_tokens=16000
  ):
      # Format the details to extract to be placed within the prompt's context
      details_to_extract_str = "\n".join(details_to_extract)

      # Prompt the model to summarize the sublease agreement
      prompt = f"""Summarize the following sublease agreement. Focus on these key aspects:

      {details_to_extract_str}

      Provide the summary in bullet points nested within the XML header for each section. For example:

      <parties involved>
      - Sublessor: [Name]
      // Add more details as needed
      </parties involved>

      If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.

      Sublease agreement text:
      {text}
      """

      response = client.messages.create(
          model=model,
          max_tokens=max_tokens,
          system="You are a legal analyst specializing in real estate law, known for highly accurate and detailed summaries of sublease agreements.",
          messages=[
              {"role": "user", "content": prompt},
          ],
      )

      return next(block.text for block in response.content if block.type == "text")


  sublease_summary = summarize_document(document_text, details_to_extract)
  print(sublease_summary)
  ```

  ```typescript TypeScript
  // Initialize the Anthropic client
  const client = new Anthropic();

  async function summarizeDocument(
    text: string,
    detailsToExtract: string[],
    model: Anthropic.Model = "claude-opus-5-5",
    maxTokens = 16000
  ): Promise<string> {
    // Format the details to extract to be placed within the prompt's context
    const detailsToExtractStr = detailsToExtract.join("\n");

    // Prompt the model to summarize the sublease agreement
    const prompt = `Summarize the following sublease agreement. Focus on these key aspects:

      ${detailsToExtractStr}

      Provide the summary in bullet points nested within the XML header for each section. For example:

      <parties involved>
      - Sublessor: [Name]
      // Add more details as needed
      </parties involved>

      If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.

      Sublease agreement text:
      ${text}
      `;

    const response = await client.messages.create({
      model,
      max_tokens: maxTokens,
      system:
        "You are a legal analyst specializing in real estate law, known for highly accurate and detailed summaries of sublease agreements.",
      messages: [{ role: "user", content: prompt }]
    });

    const textBlock = response.content.find((block) => block.type === "text");
    if (!textBlock) {
      throw new Error("Expected a text block in the response");
    }
    return textBlock.text;
  }

  const subleaseSummary = await summarizeDocument(documentText, detailsToExtract);
  console.log(subleaseSummary);
  ```

  ```csharp C#
  // Initialize the Anthropic client
  var client = new AnthropicClient();

  async Task<string> SummarizeDocument(
      string text,
      IReadOnlyList<string> detailsToExtract,
      Model model = Model.ClaudeOpus5_5,
      long maxTokens = 16000
  )
  {
      // Format the details to extract to be placed within the prompt's context
      var detailsToExtractStr = string.Join("\n", detailsToExtract);

      // Prompt the model to summarize the sublease agreement
      var prompt = $"""
          Summarize the following sublease agreement. Focus on these key aspects:

              {detailsToExtractStr}

              Provide the summary in bullet points nested within the XML header for each section. For example:

              <parties involved>
              - Sublessor: [Name]
              // Add more details as needed
              </parties involved>

              If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.

              Sublease agreement text:
              {text}
          """;

      var response = await client.Messages.Create(
          new()
          {
              Model = model,
              MaxTokens = maxTokens,
              System = "You are a legal analyst specializing in real estate law, known for highly accurate and detailed summaries of sublease agreements.",
              Messages = [new UserMessageParam { Content = prompt }],
          }
      );

      foreach (var block in response.Content)
      {
          if (block.TryPickText(out var textBlock))
          {
              return textBlock.Text;
          }
      }
      throw new InvalidOperationException("Expected a text block in the response.");
  }

  var subleaseSummary = await SummarizeDocument(documentText, detailsToExtract);
  Console.WriteLine(subleaseSummary);
  ```

  ```go Go
  // Initialize the Anthropic client
  var client = anthropic.NewClient()

  func summarizeDocument(text string, detailsToExtract []string, model anthropic.Model, maxTokens int64) string {
  	// Format the details to extract to be placed within the prompt's context
  	detailsToExtractStr := strings.Join(detailsToExtract, "\n")

  	// Prompt the model to summarize the sublease agreement
  	prompt := fmt.Sprintf(`Summarize the following sublease agreement. Focus on these key aspects:

      %s

      Provide the summary in bullet points nested within the XML header for each section. For example:

      <parties involved>
      - Sublessor: [Name]
      // Add more details as needed
      </parties involved>

      If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.

      Sublease agreement text:
      %s
      `, detailsToExtractStr, text)

  	response, err := client.Messages.New(context.Background(), anthropic.MessageNewParams{
  		Model:     model,
  		MaxTokens: maxTokens,
  		System: []anthropic.TextBlockParam{
  			{Text: "You are a legal analyst specializing in real estate law, known for highly accurate and detailed summaries of sublease agreements."},
  		},
  		Messages: []anthropic.MessageParam{
  			anthropic.NewUserMessage(anthropic.NewTextBlock(prompt)),
  		},
  	})
  	if err != nil {
  		log.Fatal(err)
  	}

  	for _, block := range response.Content {
  		if textBlock, ok := block.AsAny().(anthropic.TextBlock); ok {
  			return textBlock.Text
  		}
  	}
  	panic("expected a text block in the response")
  }

  // printSubleaseSummary summarizes the sublease agreement and prints the summary.
  func printSubleaseSummary() {
  	subleaseSummary := summarizeDocument(documentText, detailsToExtract, anthropic.ModelClaudeOpus5_5, 16000)
  	fmt.Println(subleaseSummary)
  }
  ```

  ```java Java
  // Initialize the Anthropic client
  AnthropicClient client = AnthropicOkHttpClient.fromEnv();

  String summarizeDocument(String text, List<String> detailsToExtract, Model model, long maxTokens) {
      // Format the details to extract to be placed within the prompt's context
      String detailsToExtractStr = String.join("\n", detailsToExtract);

      // Prompt the model to summarize the sublease agreement
      String prompt = """
          Summarize the following sublease agreement. Focus on these key aspects:

              %s

              Provide the summary in bullet points nested within the XML header for each section. For example:

              <parties involved>
              - Sublessor: [Name]
              // Add more details as needed
              </parties involved>

              If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.

              Sublease agreement text:
              %s
          """
          .formatted(detailsToExtractStr, text);

      Message response = client.messages().create(MessageCreateParams.builder()
          .model(model)
          .maxTokens(maxTokens)
          .system("You are a legal analyst specializing in real estate law, known for highly accurate and detailed summaries of sublease agreements.")
          .addUserMessage(prompt)
          .build());

      return response.content().stream()
          .flatMap(block -> block.text().stream())
          .findFirst()
          .orElseThrow()
          .text();
  }

  void printSubleaseSummary() {
      String subleaseSummary = summarizeDocument(
          documentText, detailsToExtract, Model.CLAUDE_OPUS_5_5, 16000);
      IO.println(subleaseSummary);
  }
  ```

  ```php PHP
  // Initialize the Anthropic client
  $client = new Client();

  $summarizeDocument = function (
      string $text,
      array $detailsToExtract,
      Model $model = Model::CLAUDE_OPUS_5_5,
      int $maxTokens = 16000,
  ) use ($client): string {
      // Format the details to extract to be placed within the prompt's context
      $detailsToExtractStr = implode("\n", $detailsToExtract);

      // Prompt the model to summarize the sublease agreement
      $prompt = <<<PROMPT
          Summarize the following sublease agreement. Focus on these key aspects:

              {$detailsToExtractStr}

              Provide the summary in bullet points nested within the XML header for each section. For example:

              <parties involved>
              - Sublessor: [Name]
              // Add more details as needed
              </parties involved>

              If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.

              Sublease agreement text:
              {$text}
          PROMPT;

      $response = $client->messages->create(
          model: $model,
          maxTokens: $maxTokens,
          system: 'You are a legal analyst specializing in real estate law, known for highly accurate and detailed summaries of sublease agreements.',
          messages: [['role' => 'user', 'content' => $prompt]],
      );

      $textBlock = array_find($response->content, fn ($block) => $block instanceof \Anthropic\Messages\TextBlock)
          ?? throw new \RuntimeException('Expected a text block in the response.');

      return $textBlock->text;
  };

  $subleaseSummary = $summarizeDocument($documentText, $detailsToExtract);
  echo $subleaseSummary . "\n";
  ```

  ```ruby Ruby
  # Initialize the Anthropic client
  CLIENT = Anthropic::Client.new

  def summarize_document(text, details_to_extract, model: Anthropic::Model::CLAUDE_OPUS_5_5, max_tokens: 16_000)
    # Format the details to extract to be placed within the prompt's context
    details_to_extract_str = details_to_extract.join("\n")

    # Prompt the model to summarize the sublease agreement
    prompt = <<~PROMPT
      Summarize the following sublease agreement. Focus on these key aspects:

          #{details_to_extract_str}

          Provide the summary in bullet points nested within the XML header for each section. For example:

          <parties involved>
          - Sublessor: [Name]
          // Add more details as needed
          </parties involved>

          If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.

          Sublease agreement text:
          #{text}
    PROMPT

    response = CLIENT.messages.create(
      model:,
      max_tokens:,
      system_: "You are a legal analyst specializing in real estate law, known for highly accurate and detailed summaries of sublease agreements.",
      messages: [{role: :user, content: prompt}]
    )

    response.content.find { |block| block.is_a?(Anthropic::Models::TextBlock) }.text
  end

  sublease_summary = summarize_document(document_text, details_to_extract)
  puts sublease_summary
  ```
</CodeGroup>

This code implements a `summarize_document()` (typescript, go, java: `summarizeDocument()`; php: `$summarizeDocument()`; csharp: `SummarizeDocument()`) function that uses Claude to summarize the contents of a sublease agreement. The function accepts a text string and a list of details to extract as inputs. In this example, the code calls the function with the `document_text` (typescript, go, java, csharp: `documentText`; php: `$documentText`) and `details_to_extract` (typescript, go, java, csharp: `detailsToExtract`; php: `$detailsToExtract`) variables that were defined in the previous code snippets.

Within the function, a prompt is generated for Claude, including the document to be summarized, the details to extract, and specific instructions for summarizing the document. The prompt instructs Claude to respond with a summary of each detail to extract nested within XML headers.

Because the code outputs each section of the summary within tags, each section can be parsed out as a post-processing step. This approach makes it possible to create structured summaries that can be adapted for your use case, so that each summary follows the same pattern.

### Evaluate your prompt

Prompting often requires testing and optimization for it to be production ready. To determine the readiness of your solution, evaluate the quality of your summaries using a systematic process combining quantitative and qualitative methods. Creating a [strong empirical evaluation](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests#build-evaluations) based on your defined success criteria allows you to optimize your prompts. Here are some metrics you might want to include within your empirical evaluation:

<AccordionGroup>
  <Accordion title="ROUGE scores">
    This measures the overlap between the generated summary and an expert-created reference summary. This metric primarily focuses on recall and is useful for evaluating content coverage.
  </Accordion>

  <Accordion title="BLEU scores">
    Although originally developed for machine translation, this metric can be adapted for summarization tasks. BLEU scores measure the precision of n-gram matches between the generated summary and reference summaries. A higher score indicates that the generated summary contains similar phrases and terminology to the reference summary. 
  </Accordion>

  <Accordion title="Contextual embedding similarity">
    This metric involves creating vector representations (embeddings) of both the generated and reference summaries. The similarity between these embeddings is then calculated, often using cosine similarity. Higher similarity scores indicate that the generated summary captures the semantic meaning and context of the reference summary, even if the exact wording differs.
  </Accordion>

  <Accordion title="LLM-based grading">
    This method involves using an LLM such as Claude to evaluate the quality of generated summaries against a scoring rubric. The rubric can be tailored to your specific needs, assessing key factors such as accuracy, completeness, and coherence. For implementation guidance, see 

    [Tips for LLM-based grading](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests#tips-for-llm-based-grading)

    .
  </Accordion>

  <Accordion title="Human evaluation">
    In addition to creating the reference summaries, legal experts can also evaluate the quality of the generated summaries. Although this is expensive and time-consuming at scale, this is often done on a few summaries as a validation check before deploying to production.
  </Accordion>
</AccordionGroup>

### Deploy your prompt

Here are some additional considerations to keep in mind as you deploy your solution to production.

1. **Ensure no liability:** Understand the legal implications of errors in the summaries, which could lead to legal liability for your organization or clients. Provide disclaimers or legal notices clarifying that the summaries are generated by AI and should be reviewed by legal professionals.

2. **Handle diverse document types:** This guide discusses how to extract text from PDFs. In the real world, documents might come in a variety of formats (such as PDFs, Word documents, and text files). Ensure your data extraction pipeline can convert all of the file formats you expect to receive.

3. **Parallelize API calls to Claude:** Long documents with a large number of tokens might require up to a minute for Claude to generate a summary. For large document collections, you might want to send API calls to Claude in parallel so that the summaries can be completed in a reasonable timeframe. Refer to Anthropic’s [rate limits](https://platform.claude.com/docs/en/api/rate-limits#rate-limits) to determine the maximum number of API calls that can be performed in parallel.

***

## Improve performance

In complex scenarios, it might be helpful to consider additional strategies to improve performance beyond standard [prompt engineering techniques](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview). Here are some advanced strategies:

### Perform meta-summarization to summarize long documents

Legal summarization often involves handling long documents or many related documents at once, such that you surpass Claude’s context window. You can use a chunking method known as meta-summarization to handle this use case. This technique involves breaking down documents into smaller, manageable chunks and then processing each chunk separately. You can then combine the summaries of each chunk to create a meta-summary of the entire document.

Here’s an example of how to perform meta-summarization:

<CodeGroup exclude="shell">
  <CodeGroupItem language="cURL">
    This workflow needs more logic than a single shell command. Use the Claude SDK to run it.
  </CodeGroupItem>

  <CodeGroupItem language="CLI">
    This workflow needs more logic than a single shell command. Use the Claude SDK to run it.
  </CodeGroupItem>

  ```python Python
  def chunk_text(text, chunk_size=20000):
      return [text[i : i + chunk_size] for i in range(0, len(text), chunk_size)]


  def summarize_long_document(
      text, details_to_extract, model="claude-opus-5-5", max_tokens=16000
  ):
      # Format the details to extract to be placed within the prompt's context
      details_to_extract_str = "\n".join(details_to_extract)

      # Iterate over chunks and summarize each one
      chunk_summaries = [
          summarize_document(
              chunk, details_to_extract, model=model, max_tokens=max_tokens
          )
          for chunk in chunk_text(text)
      ]

      final_summary_prompt = f"""

      You are looking at the chunked summaries of multiple documents that are all related.
      Combine the following summaries of the document from different truthful sources into a coherent overall summary:

      <chunked_summaries>
      {"".join(chunk_summaries)}
      </chunked_summaries>

      Focus on these key aspects:
      {details_to_extract_str}

      Provide the summary in bullet points nested within the XML header for each section. For example:

      <parties involved>
      - Sublessor: [Name]
      // Add more details as needed
      </parties involved>

      If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.
      """

      response = client.messages.create(
          model=model,
          max_tokens=max_tokens,
          system="You are a legal expert that summarizes notes on one document.",
          messages=[
              {"role": "user", "content": final_summary_prompt},
          ],
      )

      return next(block.text for block in response.content if block.type == "text")


  long_summary = summarize_long_document(document_text, details_to_extract)
  print(long_summary)
  ```

  ```typescript TypeScript
  function chunkText(text: string, chunkSize = 20000): string[] {
    return Array.from({ length: Math.ceil(text.length / chunkSize) }, (_, index) =>
      text.slice(index * chunkSize, (index + 1) * chunkSize)
    );
  }

  async function summarizeLongDocument(
    text: string,
    detailsToExtract: string[],
    model: Anthropic.Model = "claude-opus-5-5",
    maxTokens = 16000
  ): Promise<string> {
    // Format the details to extract to be placed within the prompt's context
    const detailsToExtractStr = detailsToExtract.join("\n");

    // Iterate over chunks and summarize each one
    const chunkSummaries: string[] = [];
    for (const chunk of chunkText(text)) {
      chunkSummaries.push(await summarizeDocument(chunk, detailsToExtract, model, maxTokens));
    }

    const finalSummaryPrompt = `

      You are looking at the chunked summaries of multiple documents that are all related.
      Combine the following summaries of the document from different truthful sources into a coherent overall summary:

      <chunked_summaries>
      ${chunkSummaries.join("")}
      </chunked_summaries>

      Focus on these key aspects:
      ${detailsToExtractStr}

      Provide the summary in bullet points nested within the XML header for each section. For example:

      <parties involved>
      - Sublessor: [Name]
      // Add more details as needed
      </parties involved>

      If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.
      `;

    const response = await client.messages.create({
      model,
      max_tokens: maxTokens,
      system: "You are a legal expert that summarizes notes on one document.",
      messages: [{ role: "user", content: finalSummaryPrompt }]
    });

    const textBlock = response.content.find((block) => block.type === "text");
    if (!textBlock) {
      throw new Error("Expected a text block in the response");
    }
    return textBlock.text;
  }

  const longSummary = await summarizeLongDocument(documentText, detailsToExtract);
  console.log(longSummary);
  ```

  ```csharp C#
  IEnumerable<string> ChunkText(string text, int chunkSize = 20000) =>
      text.Chunk(chunkSize).Select(chars => new string(chars));

  async Task<string> SummarizeLongDocument(
      string text,
      IReadOnlyList<string> detailsToExtract,
      Model model = Model.ClaudeOpus5_5,
      long maxTokens = 16000
  )
  {
      // Format the details to extract to be placed within the prompt's context
      var detailsToExtractStr = string.Join("\n", detailsToExtract);

      // Iterate over chunks and summarize each one
      List<string> chunkSummaries = [];
      foreach (var chunk in ChunkText(text))
      {
          chunkSummaries.Add(await SummarizeDocument(chunk, detailsToExtract, model, maxTokens));
      }

      var finalSummaryPrompt = $"""

              You are looking at the chunked summaries of multiple documents that are all related.
              Combine the following summaries of the document from different truthful sources into a coherent overall summary:

              <chunked_summaries>
              {string.Concat(chunkSummaries)}
              </chunked_summaries>

              Focus on these key aspects:
              {detailsToExtractStr}

              Provide the summary in bullet points nested within the XML header for each section. For example:

              <parties involved>
              - Sublessor: [Name]
              // Add more details as needed
              </parties involved>

              If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.
          """;

      var response = await client.Messages.Create(
          new()
          {
              Model = model,
              MaxTokens = maxTokens,
              System = "You are a legal expert that summarizes notes on one document.",
              Messages = [new UserMessageParam { Content = finalSummaryPrompt }],
          }
      );

      foreach (var block in response.Content)
      {
          if (block.TryPickText(out var textBlock))
          {
              return textBlock.Text;
          }
      }
      throw new InvalidOperationException("Expected a text block in the response.");
  }

  var longSummary = await SummarizeLongDocument(documentText, detailsToExtract);
  Console.WriteLine(longSummary);
  ```

  ```go Go
  func chunkText(text string, chunkSize int) []string {
  	var chunks []string
  	for chunk := range slices.Chunk([]rune(text), chunkSize) {
  		chunks = append(chunks, string(chunk))
  	}
  	return chunks
  }

  func summarizeLongDocument(text string, detailsToExtract []string, model anthropic.Model, maxTokens int64) string {
  	// Format the details to extract to be placed within the prompt's context
  	detailsToExtractStr := strings.Join(detailsToExtract, "\n")

  	// Iterate over chunks and summarize each one
  	var chunkSummaries []string
  	for _, chunk := range chunkText(text, 20000) {
  		chunkSummaries = append(chunkSummaries, summarizeDocument(chunk, detailsToExtract, model, maxTokens))
  	}

  	finalSummaryPrompt := fmt.Sprintf(`

      You are looking at the chunked summaries of multiple documents that are all related.
      Combine the following summaries of the document from different truthful sources into a coherent overall summary:

      <chunked_summaries>
      %s
      </chunked_summaries>

      Focus on these key aspects:
      %s

      Provide the summary in bullet points nested within the XML header for each section. For example:

      <parties involved>
      - Sublessor: [Name]
      // Add more details as needed
      </parties involved>

      If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.
      `, strings.Join(chunkSummaries, ""), detailsToExtractStr)

  	response, err := client.Messages.New(context.Background(), anthropic.MessageNewParams{
  		Model:     model,
  		MaxTokens: maxTokens,
  		System: []anthropic.TextBlockParam{
  			{Text: "You are a legal expert that summarizes notes on one document."},
  		},
  		Messages: []anthropic.MessageParam{
  			anthropic.NewUserMessage(anthropic.NewTextBlock(finalSummaryPrompt)),
  		},
  	})
  	if err != nil {
  		log.Fatal(err)
  	}

  	for _, block := range response.Content {
  		if textBlock, ok := block.AsAny().(anthropic.TextBlock); ok {
  			return textBlock.Text
  		}
  	}
  	panic("expected a text block in the response")
  }

  // printLongSummary summarizes the sublease agreement chunk by chunk and prints the combined summary.
  func printLongSummary() {
  	longSummary := summarizeLongDocument(documentText, detailsToExtract, anthropic.ModelClaudeOpus5_5, 16000)
  	fmt.Println(longSummary)
  }
  ```

  ```java Java
  List<String> chunkText(String text, int chunkSize) {
      return IntStream.iterate(0, start -> start < text.length(), start -> start + chunkSize)
          .mapToObj(start -> text.substring(start, Math.min(start + chunkSize, text.length())))
          .toList();
  }

  String summarizeLongDocument(String text, List<String> detailsToExtract, Model model, long maxTokens) {
      // Format the details to extract to be placed within the prompt's context
      String detailsToExtractStr = String.join("\n", detailsToExtract);

      // Iterate over chunks and summarize each one
      String chunkSummaries = chunkText(text, 20000).stream()
          .map(chunk -> summarizeDocument(chunk, detailsToExtract, model, maxTokens))
          .collect(Collectors.joining());

      String finalSummaryPrompt = """

              You are looking at the chunked summaries of multiple documents that are all related.
              Combine the following summaries of the document from different truthful sources into a coherent overall summary:

              <chunked_summaries>
              %s
              </chunked_summaries>

              Focus on these key aspects:
              %s

              Provide the summary in bullet points nested within the XML header for each section. For example:

              <parties involved>
              - Sublessor: [Name]
              // Add more details as needed
              </parties involved>

              If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.
          """
          .formatted(chunkSummaries, detailsToExtractStr);

      Message response = client.messages().create(MessageCreateParams.builder()
          .model(model)
          .maxTokens(maxTokens)
          .system("You are a legal expert that summarizes notes on one document.")
          .addUserMessage(finalSummaryPrompt)
          .build());

      return response.content().stream()
          .flatMap(block -> block.text().stream())
          .findFirst()
          .orElseThrow()
          .text();
  }

  void printLongSummary() {
      String longSummary = summarizeLongDocument(
          documentText, detailsToExtract, Model.CLAUDE_OPUS_5_5, 16000);
      IO.println(longSummary);
  }
  ```

  ```php PHP
  $chunkText = fn (string $text, int $chunkSize = 20000): array => mb_str_split($text, $chunkSize);

  $summarizeLongDocument = function (
      string $text,
      array $detailsToExtract,
      Model $model = Model::CLAUDE_OPUS_5_5,
      int $maxTokens = 16000,
  ) use ($client, $chunkText, $summarizeDocument): string {
      // Format the details to extract to be placed within the prompt's context
      $detailsToExtractStr = implode("\n", $detailsToExtract);

      // Iterate over chunks and summarize each one
      $chunkSummaries = array_map(
          fn (string $chunk) => $summarizeDocument($chunk, $detailsToExtract, $model, $maxTokens),
          $chunkText($text),
      );
      $chunkSummariesStr = implode('', $chunkSummaries);

      $finalSummaryPrompt = <<<PROMPT

              You are looking at the chunked summaries of multiple documents that are all related.
              Combine the following summaries of the document from different truthful sources into a coherent overall summary:

              <chunked_summaries>
              {$chunkSummariesStr}
              </chunked_summaries>

              Focus on these key aspects:
              {$detailsToExtractStr}

              Provide the summary in bullet points nested within the XML header for each section. For example:

              <parties involved>
              - Sublessor: [Name]
              // Add more details as needed
              </parties involved>

              If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.
          PROMPT;

      $response = $client->messages->create(
          model: $model,
          maxTokens: $maxTokens,
          system: 'You are a legal expert that summarizes notes on one document.',
          messages: [['role' => 'user', 'content' => $finalSummaryPrompt]],
      );

      $textBlock = array_find($response->content, fn ($block) => $block instanceof \Anthropic\Messages\TextBlock)
          ?? throw new \RuntimeException('Expected a text block in the response.');

      return $textBlock->text;
  };

  $longSummary = $summarizeLongDocument($documentText, $detailsToExtract);
  echo $longSummary . "\n";
  ```

  ```ruby Ruby
  def chunk_text(text, chunk_size: 20_000)
    text.chars.each_slice(chunk_size).map(&:join)
  end

  def summarize_long_document(text, details_to_extract, model: Anthropic::Model::CLAUDE_OPUS_5_5, max_tokens: 16_000)
    # Format the details to extract to be placed within the prompt's context
    details_to_extract_str = details_to_extract.join("\n")

    # Iterate over chunks and summarize each one
    chunk_summaries = chunk_text(text).map do |chunk|
      summarize_document(chunk, details_to_extract, model:, max_tokens:)
    end

    final_summary_prompt = <<~PROMPT

          You are looking at the chunked summaries of multiple documents that are all related.
          Combine the following summaries of the document from different truthful sources into a coherent overall summary:

          <chunked_summaries>
          #{chunk_summaries.join}
          </chunked_summaries>

          Focus on these key aspects:
          #{details_to_extract_str}

          Provide the summary in bullet points nested within the XML header for each section. For example:

          <parties involved>
          - Sublessor: [Name]
          // Add more details as needed
          </parties involved>

          If any information is not explicitly stated in the document, note it as "Not specified". Do not preamble.
    PROMPT

    response = CLIENT.messages.create(
      model:,
      max_tokens:,
      system_: "You are a legal expert that summarizes notes on one document.",
      messages: [{role: :user, content: final_summary_prompt}]
    )

    response.content.find { |block| block.is_a?(Anthropic::Models::TextBlock) }.text
  end

  long_summary = summarize_long_document(document_text, details_to_extract)
  puts long_summary
  ```
</CodeGroup>

The `summarize_long_document()` (typescript, go, java: `summarizeLongDocument()`; php: `$summarizeLongDocument()`; csharp: `SummarizeLongDocument()`) function builds upon the earlier `summarize_document()` (typescript, go, java: `summarizeDocument()`; php: `$summarizeDocument()`; csharp: `SummarizeDocument()`) function by splitting the document into smaller chunks and summarizing each chunk individually.

The code achieves this by applying the `summarize_document()` (typescript, go, java: `summarizeDocument()`; php: `$summarizeDocument()`; csharp: `SummarizeDocument()`) function to each chunk of 20,000 characters within the original document. The individual summaries are then combined, and a final summary is created from these chunk summaries.

Note that the `summarize_long_document()` (typescript, go, java: `summarizeLongDocument()`; php: `$summarizeLongDocument()`; csharp: `SummarizeLongDocument()`) function isn’t strictly necessary for the example PDF, as the entire document fits within Claude’s context window. However, it becomes essential for documents exceeding Claude’s context window or when summarizing multiple related documents together. Regardless, this meta-summarization technique often captures additional important details in the final summary that were missed in the earlier single-summary approach.

### Use summary indexed documents to explore a large collection of documents

Searching a collection of documents with an LLM usually involves retrieval-augmented generation (RAG). However, in scenarios involving large documents or when precise information retrieval is crucial, a basic RAG approach might be insufficient. Summary indexed documents is an advanced RAG approach that provides a more efficient way of ranking documents for retrieval, using less context than traditional RAG methods. In this approach, you first use Claude to generate a concise summary for each document in your corpus, and then use Claude to rank the relevance of each summary to the query being asked. For further details on this approach, including a code-based example, see the summary indexed documents section in the [summarization recipe](https://platform.claude.com/cookbook/capabilities-summarization-guide).

### Fine-tune Claude to learn from your dataset

Another advanced technique to improve Claude’s ability to generate summaries is fine-tuning. Fine-tuning involves training Claude on a custom dataset that specifically aligns with your legal summarization needs, ensuring that Claude adapts to your use case. Here’s an overview on how to perform fine-tuning:

1. **Identify errors:** Start by collecting instances where Claude’s summaries are inadequate. This could include missing critical legal details, misunderstanding context, or using inappropriate legal terminology.

2. **Curate a dataset:** Once you’ve identified these issues, compile a dataset of these problematic examples. This dataset should include the original legal documents alongside your corrected summaries, ensuring that Claude learns the behavior you want.

3. **Perform fine-tuning:** Fine-tuning involves retraining the model on your curated dataset to adjust its weights and parameters. This retraining helps Claude better adapt to the specific requirements of your legal domain, improving its ability to summarize documents according to your standards.

4. **Improve iteratively:** Fine-tuning is not a one-time process. As Claude continues to generate summaries, you can iteratively add new examples where it has underperformed, further refining its capabilities. Over time, this continuous feedback loop will result in a model that is highly specialized for your legal summarization tasks.

<Tip>
  Fine-tuning is currently only available through Amazon Bedrock. Additional details are available in the 

  [AWS launch blog](https://aws.amazon.com/blogs/machine-learning/fine-tune-anthropics-claude-3-haiku-in-amazon-bedrock-to-boost-model-accuracy-and-quality/)

  .
</Tip>

<CardGroup cols={2}>
  <Card title="Summarization recipe" icon="link" href="https://platform.claude.com/cookbook/capabilities-summarization-guide">
    View a fully implemented code-based example of how to use Claude to summarize contracts.
  </Card>

  <Card title="Citations recipe" icon="link" href="https://platform.claude.com/cookbook/misc-using-citations">
    Explore the Citations recipe for guidance on how to ensure accuracy and explainability of information.
  </Card>
</CardGroup>
