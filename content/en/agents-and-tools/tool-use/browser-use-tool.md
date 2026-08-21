---
title: Browser use tool
url: https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool
description: Let Claude navigate, read, and interact with webpages in your own browser environment with the browser use tool.
---

## Compatibility
- [ZDR](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention): eligible (excludes [Covered Models](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#model-specific-data-retention-requirements))
- Supported models: `claude-fable-5`, `claude-mythos-5`, `claude-opus-5`, `claude-sonnet-5`, `claude-opus-4-8`
- Platforms: Claude API; not available on Claude Platform on AWS, Amazon Bedrock, Google Cloud, Microsoft Foundry

The browser use tool lets Claude navigate, read, and interact with webpages in a browser that your application runs. It works with the page both through its structure (the accessibility tree, elements, forms, and tabs) and through pixels (screenshots and viewport coordinates), whereas the [computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) works with a whole desktop through screenshots and coordinates alone. It's an Anthropic-defined [client toolset](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets): one `browser_toolset_20260801` entry in your `tools` array gives Claude 27 member tools by default, such as `navigate`, `read_page`, `left_click`, and `screenshot`, plus four more (`javascript_exec`, `file_upload`, `read_console`, and `read_network`) when you [enable them](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#enable-optional-member-tools). Your application runs every call against its own browser automation; nothing runs on Anthropic's side. It isn't currently available in [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/tools). This page says "your application" for the agent loop that calls the Messages API and "your executor" for the part of it that drives the browser and produces tool results.

Choose browser use over computer use when the task stays inside webpages: Claude can read a page's structure, act on an element by reference in addition to by coordinate, set form values directly, and work across tabs, and you don't need to run a desktop. If Claude only needs to read pages you can point it to, or to find sources on the web, the [web fetch tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool) and [web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool) are lighter still, because they're [server tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools) that the API runs for you with no browser to operate. Choose browser use instead when pages build their content with JavaScript or the task means acting on the page rather than only reading it.

With browser use, Claude reads and acts on live webpages, so everything a page supplies is untrusted input and the actions Claude takes can have real effects. See [Security considerations](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#security-considerations) before you deploy.

## Quick start

The browser use tool is generally available on the Claude API with no beta header: add one entry of type `browser_toolset_20260801`, with no `name`, to the `tools` array of a [Messages API](https://platform.claude.com/docs/en/api/messages/create) request.

<CodeGroup>
  ```bash cURL
  curl https://api.anthropic.com/v1/messages \
    -H "content-type: application/json" \
    -H "x-api-key: $ANTHROPIC_API_KEY" \
    -H "anthropic-version: 2023-06-01" \
    -d '{
      "model": "claude-opus-5",
      "max_tokens": 2048,
      "tools": [
        {
          "type": "browser_toolset_20260801"
        }
      ],
      "messages": [
        {
          "role": "user",
          "content": "Open example.com/docs and tell me how to get started."
        }
      ]
    }'
  ```

  ```bash CLI
  ant messages create <<'YAML'
  model: claude-opus-5
  max_tokens: 2048
  tools:
    - type: browser_toolset_20260801
  messages:
    - role: user
      content: Open example.com/docs and tell me how to get started.
  YAML
  ```

  ```python Python
  client = anthropic.Anthropic()

  response = client.messages.create(
      model="claude-opus-5",
      max_tokens=2048,
      tools=[{"type": "browser_toolset_20260801"}],
      messages=[
          {
              "role": "user",
              "content": "Open example.com/docs and tell me how to get started.",
          }
      ],
  )
  print(response)
  ```

  ```typescript TypeScript
  const client = new Anthropic();

  const response = await client.messages.create({
    model: "claude-opus-5",
    max_tokens: 2048,
    tools: [{ type: "browser_toolset_20260801" }],
    messages: [
      {
        role: "user",
        content: "Open example.com/docs and tell me how to get started."
      }
    ]
  });

  console.log(response);
  ```

  ```csharp C#
  var client = new AnthropicClient();

  var parameters = new MessageCreateParams
  {
      Model = Model.ClaudeOpus5,
      MaxTokens = 2048,
      Tools = [new BrowserToolset20260801()],
      Messages =
      [
          new MessageParam
          {
              Role = Role.User,
              Content = "Open example.com/docs and tell me how to get started.",
          },
      ],
  };

  var response = await client.Messages.Create(parameters);
  Console.WriteLine(response);
  ```

  ```go Go
  client := anthropic.NewClient()

  response, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
  	Model:     anthropic.ModelClaudeOpus5,
  	MaxTokens: 2048,
  	Tools: []anthropic.ToolUnionParam{
  		{OfBrowserToolset20260801: &anthropic.BrowserToolset20260801Param{}},
  	},
  	Messages: []anthropic.MessageParam{
  		anthropic.NewUserMessage(anthropic.NewTextBlock("Open example.com/docs and tell me how to get started.")),
  	},
  })
  if err != nil {
  	log.Fatal(err)
  }
  fmt.Println(response.RawJSON())
  ```

  ```java Java
  import com.anthropic.models.messages.BrowserToolset20260801;
  // ...

  void main() {
      AnthropicClient client = AnthropicOkHttpClient.fromEnv();

      MessageCreateParams params = MessageCreateParams.builder()
          .model(Model.CLAUDE_OPUS_5)
          .maxTokens(2048L)
          .addTool(BrowserToolset20260801.builder().build())
          .addUserMessage("Open example.com/docs and tell me how to get started.")
          .build();

      Message response = client.messages().create(params);
      IO.println(response);
  }
  ```

  ```php PHP
  $client = new Client();

  $response = $client->messages->create(
      maxTokens: 2048,
      messages: [
          ['role' => 'user', 'content' => 'Open example.com/docs and tell me how to get started.'],
      ],
      model: 'claude-opus-5',
      tools: [
          ['type' => 'browser_toolset_20260801'],
      ],
  );

  echo $response;
  ```

  ```ruby Ruby
  client = Anthropic::Client.new

  response = client.messages.create(
    model: "claude-opus-5",
    max_tokens: 2048,
    tools: [
      { type: "browser_toolset_20260801" }
    ],
    messages: [
      {
        role: "user",
        content: "Open example.com/docs and tell me how to get started."
      }
    ]
  )

  puts response
  ```
</CodeGroup>

Claude's first response ends with `stop_reason: "tool_use"` and carries one or more member `tool_use` blocks, each naming a member tool in `name` and carrying `"toolset_name": "browser"`:

```json Output
{
  "id": "msg_01HCDu4XSTLzTAcodEQ58vDo",
  "type": "message",
  "role": "assistant",
  "model": "claude-opus-5",
  "content": [
    {
      "type": "text",
      "text": "I'll open the documentation and read the page to find the getting-started instructions."
    },
    {
      "type": "tool_use",
      "id": "toolu_01NRLabsLyVHZPKxbKvkfSMn",
      "name": "navigate",
      "toolset_name": "browser",
      "input": { "url": "https://example.com/docs" }
    },
    {
      "type": "tool_use",
      "id": "toolu_01UvHU5cDyTZ2vXKf5wCkPqR",
      "name": "read_page",
      "toolset_name": "browser",
      "input": { "filter": "interactive" }
    }
  ],
  "stop_reason": "tool_use",
  "stop_sequence": null
}
```

Your executor runs `navigate`, then `read_page`, and your application returns one `tool_result` per block in its next request, echoing `toolset_name` on each. The `navigate` result reports the tab it loaded in a `browser_state` block; the `read_page` result is text in which every element carries a reference:

```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01NRLabsLyVHZPKxbKvkfSMn",
      "toolset_name": "browser",
      "content": [
        { "type": "text", "text": "Navigated to https://example.com/docs" },
        {
          "type": "browser_state",
          "tabs": [
            {
              "tab_id": "tab-1",
              "title": "Documentation",
              "url": "https://example.com/docs",
              "active": true
            }
          ]
        }
      ]
    },
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01UvHU5cDyTZ2vXKf5wCkPqR",
      "toolset_name": "browser",
      "content": [
        {
          "type": "text",
          "text": "link \"Documentation\" [ref_1]\nlink \"Getting started\" [ref_2]\ntextbox \"Search docs\" [ref_3]\nbutton \"Search\" [ref_4]\nlink \"Pricing\" [ref_5]"
        }
      ]
    }
  ]
}
```

Claude now holds references it can act on, so its next turn can click `ref_2` to open the getting-started page, with no need to locate the link in a screenshot first.

## How browser use works

Browser use runs as an agent loop: Claude returns member tool calls, your executor runs them against the browser, and you return the results until Claude answers in text.

<Steps>
  <Step title="Provide Claude with the browser use tool and a user prompt" icon="tool">
    * Add the `browser_toolset_20260801` entry, and optionally other tools, to your API request.
    * Include a user prompt that calls for working with webpages, for example, "Open example.com/docs and tell me how to get started."
  </Step>

  <Step title="Claude responds with member tool calls" icon="wrench">
    * Claude returns one or more `tool_use` blocks in a single assistant turn; several in one turn form a batch action, for example, `left_click`, then `type`, then `key`.
    * Each block's `name` is the member name, each carries `"toolset_name": "browser"`, and `input` holds only that member's parameters, with no `action` field. The response's `stop_reason` is `tool_use`.
  </Step>

  <Step title="Run the calls in order and return results" icon="browser">
    * Iterate every `tool_use` block in `response.content` (don't assume there's exactly one) and run them sequentially, in the order they appear, because later calls usually depend on earlier ones.
    * Return one `tool_result` per block in a new `user` message, matched by `tool_use_id`, and echo `"toolset_name": "browser"` on each. Every call must be answered or the next request is rejected.
    * If a call fails, return `is_error: true` with a text description for that block, then apply the halt rule in [Batch actions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#batch-actions) to every later block in the turn.
  </Step>

  <Step title="Claude continues until the task is complete" icon="arrows-clockwise">
    * Claude reads the results (page text, accessibility trees, screenshots, tab state) and, if it needs more, returns further member calls, which takes you back to step 3.
    * Otherwise, it returns a text response to the user.
  </Step>
</Steps>

Here's a skeleton of that loop's tool-call step in two parts. First, stub member handlers stand in for your browser automation. Five members (`navigate`, `read_page`, `left_click`, `type`, and `screenshot`) return the text, or for `screenshot` the image block, that becomes the result content, and the dispatcher raises an error for any member it doesn't implement.

<CodeGroup exclude="shell">
  ```python Python
  # Placeholder image data; a real executor captures the viewport and returns the PNG bytes
  PLACEHOLDER_PNG = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="


  def navigate(url):
      return f"navigated to {url}"


  def read_page():
      return 'link "Docs" [ref_1]\nbutton "Search" [ref_2]'


  def click(target):
      # A target is an element reference from read_page or find, or a viewport coordinate
      if target["type"] == "ref":
          return f"clicked {target['ref']}"
      return f"clicked at ({target['x']}, {target['y']})"


  def type_text(text):
      return f"typed: {text}"


  def capture_screenshot() -> list[ImageBlockParam]:
      # screenshot answers with an image block rather than text: return the result content list
      return [
          {
              "type": "image",
              "source": {"type": "base64", "media_type": "image/png", "data": PLACEHOLDER_PNG},
          }
      ]


  def handle_browser_action(name, tool_input):
      if name == "navigate":
          return navigate(tool_input["url"])
      elif name == "read_page":
          return read_page()
      elif name == "left_click":
          return click(tool_input["target"])
      elif name == "type":
          return type_text(tool_input["text"])
      elif name == "screenshot":
          return capture_screenshot()
      # Handle other actions as needed
      raise ValueError(f"Unknown or unimplemented member: {name}")
  ```

  ```typescript TypeScript
  // Placeholder image data; a real executor captures the viewport as PNG bytes
  const PLACEHOLDER_PNG = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==";

  function navigate(url: string): string {
    return `navigated to ${url}`;
  }

  function readPage(): string {
    return 'link "Docs" [ref_1]\nbutton "Search" [ref_2]';
  }

  function clickElement(ref: string): string {
    return `clicked ${ref}`;
  }

  function clickAt(x: number, y: number): string {
    return `clicked at (${x}, ${y})`;
  }

  function typeText(text: string): string {
    return `typed: ${text}`;
  }

  function captureScreenshot(): Anthropic.ImageBlockParam[] {
    // screenshot answers with an image block rather than text
    return [
      {
        type: "image",
        source: {
          type: "base64",
          media_type: "image/png",
          data: PLACEHOLDER_PNG,
        },
      },
    ];
  }

  function handleBrowserAction(
    action: string,
    input: unknown,
  ): string | Anthropic.ImageBlockParam[] {
    const params: object =
      typeof input === "object" && input !== null ? input : {};
    if (action === "navigate" && "url" in params) {
      return navigate(String(params.url));
    } else if (action === "read_page") {
      return readPage();
    } else if (action === "left_click" && "target" in params) {
      // target is an element reference from read_page or a viewport coordinate
      const target: object =
        typeof params.target === "object" && params.target !== null
          ? params.target
          : {};
      if ("type" in target && target.type === "ref" && "ref" in target) {
        return clickElement(String(target.ref));
      } else if ("x" in target && "y" in target) {
        return clickAt(Number(target.x), Number(target.y));
      }
    } else if (action === "type" && "text" in params) {
      return typeText(String(params.text));
    } else if (action === "screenshot") {
      return captureScreenshot();
    }
    // Handle other actions as needed
    throw new Error(`Unknown or unimplemented member: ${action}`);
  }
  ```

  ```csharp C#
  // Placeholder image data; a real executor captures the viewport and returns the PNG bytes
  const string PlaceholderPng = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==";

  string Navigate(string url) => $"navigated to {url}";

  string ReadPage() =>
      """
      link "Docs" [ref_1]
      button "Search" [ref_2]
      """;

  string ClickRef(string elementRef) => $"clicked {elementRef}";

  string ClickAt(int x, int y) => $"clicked at ({x}, {y})";

  // target is {"type": "ref", "ref": "ref_1"} or {"type": "coordinate", "x": 640, "y": 380}
  string Click(JsonElement target) =>
      target.GetProperty("type").GetString() == "ref"
          ? ClickRef(target.GetProperty("ref").GetString()!)
          : ClickAt(target.GetProperty("x").GetInt32(), target.GetProperty("y").GetInt32());

  string TypeText(string text) => $"typed: {text}";

  // screenshot answers with an image block rather than text: return the result content list
  List<Block> CaptureScreenshot() =>
      [
          new ImageBlockParam(
              new Base64ImageSource { Data = PlaceholderPng, MediaType = MediaType.ImagePng }
          ),
      ];

  ToolResultBlockParamContent HandleBrowserAction(
      string action,
      IReadOnlyDictionary<string, JsonElement> input
  ) =>
      action switch
      {
          "navigate" => Navigate(input["url"].GetString()!),
          "read_page" => ReadPage(),
          "left_click" => Click(input["target"]),
          "type" => TypeText(input["text"].GetString()!),
          "screenshot" => CaptureScreenshot(),
          // Handle other actions as needed
          _ => throw new NotSupportedException($"Unknown or unimplemented member: {action}"),
      };
  ```

  ```go Go
  // placeholderPNG stands in for a real capture: an executor returns the
  // viewport as base64-encoded PNG data.
  const placeholderPNG = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="

  // textContent wraps text as tool_result content.
  func textContent(text string) []anthropic.ToolResultBlockParamContentUnion {
  	return []anthropic.ToolResultBlockParamContentUnion{
  		{OfText: &anthropic.TextBlockParam{Text: text}},
  	}
  }

  func navigate(url string) string {
  	return fmt.Sprintf("navigated to %s", url)
  }

  func readPage() string {
  	return "link \"Docs\" [ref_1]\nbutton \"Search\" [ref_2]"
  }

  func clickRef(ref string) string {
  	return fmt.Sprintf("clicked %s", ref)
  }

  func clickAt(x, y int) string {
  	return fmt.Sprintf("clicked at (%d, %d)", x, y)
  }

  func typeText(text string) string {
  	return fmt.Sprintf("typed: %s", text)
  }

  // captureScreenshot returns an image block rather than text.
  func captureScreenshot() []anthropic.ToolResultBlockParamContentUnion {
  	return []anthropic.ToolResultBlockParamContentUnion{{
  		OfImage: &anthropic.ImageBlockParam{
  			Source: anthropic.ImageBlockParamSourceUnion{
  				OfBase64: &anthropic.Base64ImageSourceParam{
  					MediaType: anthropic.Base64ImageSourceMediaTypeImagePNG,
  					Data:      placeholderPNG,
  				},
  			},
  		},
  	}}
  }

  func handleBrowserAction(action string, params map[string]any) ([]anthropic.ToolResultBlockParamContentUnion, error) {
  	switch action {
  	case "navigate":
  		if url, ok := params["url"].(string); ok {
  			return textContent(navigate(url)), nil
  		}
  	case "read_page":
  		return textContent(readPage()), nil
  	case "left_click":
  		// target is either an element reference from read_page or a viewport coordinate
  		target, _ := params["target"].(map[string]any)
  		if ref, ok := target["ref"].(string); ok && target["type"] == "ref" {
  			return textContent(clickRef(ref)), nil
  		}
  		x, xok := target["x"].(float64)
  		y, yok := target["y"].(float64)
  		if xok && yok {
  			return textContent(clickAt(int(x), int(y))), nil
  		}
  	case "type":
  		if text, ok := params["text"].(string); ok {
  			return textContent(typeText(text)), nil
  		}
  	case "screenshot":
  		return captureScreenshot(), nil
  	// Handle other actions as needed
  	default:
  		return nil, fmt.Errorf("unknown or unimplemented member: %s", action)
  	}
  	// Reached when a member's input is missing a field or a field has the wrong type
  	return nil, fmt.Errorf("invalid input for %s", action)
  }

  ```

  ```java Java
  /** Placeholder pixels; a real executor captures the viewport and base64-encodes the PNG. */
  static final String PLACEHOLDER_PNG = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==";

  ToolResultBlockParam.Content captureScreenshot() {
      ImageBlockParam image = ImageBlockParam.builder()
              .source(Base64ImageSource.builder()
                      .mediaType(Base64ImageSource.MediaType.IMAGE_PNG)
                      .data(PLACEHOLDER_PNG)
                      .build())
              .build();
      return ToolResultBlockParam.Content.ofBlocks(
              List.of(ToolResultBlockParam.Content.Block.ofImage(image)));
  }

  String navigate(String url) {
      return "navigated to " + url;
  }

  String readPage() {
      return """
              link "Docs" [ref_1]
              button "Search" [ref_2]""";
  }

  String clickRef(String ref) {
      return "clicked " + ref;
  }

  String clickAt(long x, long y) {
      return "clicked at (" + x + ", " + y + ")";
  }

  String typeText(String text) {
      return "typed: " + text;
  }

  /** Runs one browser toolset member; {@code action} is the tool_use block's name. */
  ToolResultBlockParam.Content handleBrowserAction(String action, Map<String, JsonValue> input) {
      if (action.equals("screenshot")) {
          return captureScreenshot(); // the one member here that answers with an image block
      }
      String output = switch (action) {
          case "navigate" -> navigate(input.get("url").asStringOrThrow());
          case "read_page" -> readPage();
          case "left_click" -> {
              // target is {"type": "ref", "ref": "ref_1"} or {"type": "coordinate", "x": 640, "y": 380}
              Map<String, JsonValue> target =
                      (Map<String, JsonValue>) input.get("target").asObject().get();
              if (target.get("type").asStringOrThrow().equals("ref")) {
                  yield clickRef(target.get("ref").asStringOrThrow());
              }
              long x = ((Number) target.get("x").asNumber().get()).longValue();
              long y = ((Number) target.get("y").asNumber().get()).longValue();
              yield clickAt(x, y);
          }
          case "type" -> typeText(input.get("text").asStringOrThrow());
          // Handle other actions as needed
          default -> throw new UnsupportedOperationException("Unknown or unimplemented member: " + action);
      };
      return ToolResultBlockParam.Content.ofString(output);
  }
  ```

  ```php PHP
  // Stand-in for real PNG bytes; a real executor captures the viewport
  const PLACEHOLDER_PNG = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==';

  function navigateTo(string $url): string
  {
      return "navigated to {$url}";
  }

  function readPage(): string
  {
      return <<<'TEXT'
          link "Docs" [ref_1]
          button "Search" [ref_2]
          TEXT;
  }

  function clickTarget(array $target): string
  {
      // A target is an element reference from read_page or find, or a viewport pixel coordinate
      if ($target['type'] === 'ref') {
          return "clicked {$target['ref']}";
      }

      return "clicked at ({$target['x']}, {$target['y']})";
  }

  function typeText(string $text): string
  {
      return "typed: {$text}";
  }

  function captureScreenshot(): array
  {
      // screenshot answers with an image block rather than text, so return the result content list
      $image = [
          'type' => 'image',
          'source' => ['type' => 'base64', 'media_type' => 'image/png', 'data' => PLACEHOLDER_PNG],
      ];

      return [$image];
  }

  function handleBrowserAction(string $name, array $input): string|array
  {
      return match ($name) {
          'navigate' => navigateTo($input['url']),
          'read_page' => readPage(),
          'left_click' => clickTarget($input['target']),
          'type' => typeText($input['text']),
          'screenshot' => captureScreenshot(),
          // Handle other actions as needed
          default => throw new RuntimeException("Unknown or unimplemented member: {$name}"),
      };
  }
  ```

  ```ruby Ruby
  # Stand-in image data; a real executor captures the viewport as a PNG.
  PLACEHOLDER_PNG = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="

  def navigate(url)
    "navigated to #{url}"
  end

  def read_page
    <<~TREE
      link "Docs" [ref_1]
      button "Search" [ref_2]
    TREE
  end

  def click(target)
    return "clicked #{target[:ref]}" if target[:type] == "ref"

    "clicked at (#{target[:x]}, #{target[:y]})"
  end

  def type_text(text)
    "typed: #{text}"
  end

  def capture_screenshot
    [
      {
        type: "image",
        source: { type: "base64", media_type: "image/png", data: PLACEHOLDER_PNG }
      }
    ]
  end

  def handle_browser_action(name, input)
    case name
    when "navigate"
      navigate(input[:url])
    when "read_page"
      read_page
    when "left_click"
      # target is an element reference (from read_page or find) or a coordinate
      click(input[:target])
    when "type"
      type_text(input[:text])
    when "screenshot"
      capture_screenshot
    # Handle other actions as needed
    else
      raise ArgumentError, "Unknown or unimplemented member: #{name}"
    end
  end
  ```
</CodeGroup>

The second part runs a batch in order, dispatches each block to those handlers, echoes `toolset_name` on every result, and applies the halt rule from [Batch actions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#batch-actions), turning a handler error into an error result. The sampling loop that calls it is the one shown in [Understand the agent loop](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#understanding-the-agentic-loop), with the browser toolset in `tools`.

<CodeGroup exclude="shell">
  ```python Python
  NOT_EXECUTED = "Not executed: an earlier action in this turn failed."


  def process_tool_calls(response: Message) -> list[ToolResultBlockParam]:
      """
      Run the browser actions in Claude's response in order and answer each
      one. After the first failure the rest are skipped, because Claude planned
      them assuming the earlier actions succeeded.
      """
      tool_results: list[ToolResultBlockParam] = []
      failed = False
      for block in response.content:
          # Only the browser toolset is declared; route other tools here if you add them
          if block.type != "tool_use" or block.toolset_name != "browser":
              continue
          result: ToolResultBlockParam = {
              "type": "tool_result",
              "tool_use_id": block.id,
              "toolset_name": "browser",
          }
          if failed:
              result["content"] = NOT_EXECUTED
              result["is_error"] = True
          else:
              try:
                  # A string or a list of content blocks; a real executor also adds a
                  # browser_state block to navigation and tab-management results
                  result["content"] = handle_browser_action(block.name, block.input)
              except Exception as err:
                  result["content"] = f"Error: {err}"
                  result["is_error"] = True
                  failed = True
          tool_results.append(result)
      return tool_results
  ```

  ```typescript TypeScript
  const HALT_TEXT = "Not executed: an earlier action in this turn failed.";

  function browserResult(
    toolUseId: string,
    content: string | Anthropic.ImageBlockParam[],
    isError?: boolean,
  ): Anthropic.ToolResultBlockParam {
    return {
      type: "tool_result",
      tool_use_id: toolUseId,
      toolset_name: "browser",
      content,
      is_error: isError,
    };
  }

  function processToolCalls(
    response: Anthropic.Message,
  ): Anthropic.ToolResultBlockParam[] {
    const toolResults: Anthropic.ToolResultBlockParam[] = [];
    let failed = false;
    for (const block of response.content) {
      if (block.type !== "tool_use") {
        continue;
      }
      if (block.toolset_name !== "browser") {
        // This example declares only the browser toolset; route other tools
        // here if you add them.
        continue;
      }
      if (failed) {
        // A batch stops at its first failure; answer later actions unexecuted
        toolResults.push(browserResult(block.id, HALT_TEXT, true));
        continue;
      }
      try {
        // A string or an image block list; a real executor also adds a
        // browser_state block to navigation and tab-management results
        const result = handleBrowserAction(block.name, block.input);
        toolResults.push(browserResult(block.id, result));
      } catch (error) {
        failed = true;
        const message = error instanceof Error ? error.message : String(error);
        toolResults.push(browserResult(block.id, `Error: ${message}`, true));
      }
    }
    return toolResults;
  }
  ```

  ```csharp C#
  const string HaltText = "Not executed: an earlier action in this turn failed.";

  List<ContentBlockParam> ProcessToolCalls(Message response)
  {
      List<ContentBlockParam> toolResults = [];
      var failed = false;
      foreach (var block in response.Content)
      {
          if (!block.TryPickToolUse(out var toolUse))
          {
              continue;
          }

          if (toolUse.ToolsetName != "browser")
          {
              // This example declares only the browser toolset; route other tools
              // here if you add them.
              continue;
          }

          if (failed)
          {
              // A batch stops at its first failure; answer later actions without running them
              toolResults.Add(
                  new ToolResultBlockParam(toolUse.ID)
                  {
                      Content = HaltText,
                      IsError = true,
                      ToolsetName = "browser",
                  }
              );
              continue;
          }

          try
          {
              // A string or a list of content blocks; a real executor also adds a
              // browser_state block to navigation and tab-management results
              var result = HandleBrowserAction(toolUse.Name, toolUse.Input);
              toolResults.Add(
                  new ToolResultBlockParam(toolUse.ID) { Content = result, ToolsetName = "browser" }
              );
          }
          catch (Exception e)
          {
              failed = true;
              toolResults.Add(
                  new ToolResultBlockParam(toolUse.ID)
                  {
                      Content = $"Error: {e.Message}",
                      IsError = true,
                      ToolsetName = "browser",
                  }
              );
          }
      }
      return toolResults;
  }
  ```

  ```go Go
  const notExecuted = "Not executed: an earlier action in this turn failed."

  // browserToolResult builds the result for one browser action. Unlike an
  // ordinary tool result, it must echo the toolset name. A real executor also
  // adds a browser_state block to navigation and tab-management results.
  func browserToolResult(toolUseID string, content []anthropic.ToolResultBlockParamContentUnion, isError bool) anthropic.ContentBlockParamUnion {
  	result := anthropic.ToolResultBlockParam{
  		ToolUseID:   toolUseID,
  		ToolsetName: anthropic.String("browser"),
  		Content:     content,
  	}
  	if isError {
  		result.IsError = anthropic.Bool(true)
  	}
  	return anthropic.ContentBlockParamUnion{OfToolResult: &result}
  }

  // processToolCalls runs the browser actions in Claude's response in order and
  // builds one tool_result per tool_use block. After the first failure it skips
  // the rest: Claude planned them assuming the earlier actions succeeded.
  func processToolCalls(response *anthropic.Message) []anthropic.ContentBlockParamUnion {
  	var toolResults []anthropic.ContentBlockParamUnion
  	failed := false
  	for _, block := range response.Content {
  		switch variant := block.AsAny().(type) {
  		case anthropic.ToolUseBlock:
  			// This example declares only the browser toolset; route other tools here if you add them.
  			if variant.ToolsetName != "browser" {
  				continue
  			}
  			if failed {
  				toolResults = append(toolResults, browserToolResult(variant.ID, textContent(notExecuted), true))
  				continue
  			}
  			var input map[string]any
  			var content []anthropic.ToolResultBlockParamContentUnion
  			err := json.Unmarshal(variant.Input, &input)
  			if err == nil {
  				content, err = handleBrowserAction(variant.Name, input)
  			}
  			if err != nil {
  				failed = true
  				content = textContent("Error: " + err.Error())
  			}
  			toolResults = append(toolResults, browserToolResult(variant.ID, content, err != nil))
  		}
  	}
  	return toolResults
  }

  ```

  ```java Java
  /** The exact text the toolset contract prescribes for member calls skipped after a failure. */
  static final String HALT_TEXT = "Not executed: an earlier action in this turn failed.";

  /** Every result answering a browser toolset member echoes toolset_name. */
  ToolResultBlockParam.Builder browserResult(ToolUseBlock toolUse) {
      return ToolResultBlockParam.builder()
              .toolUseId(toolUse.id())
              .toolsetName("browser");
  }

  /**
   * Run the browser actions in Claude's response in order and build one
   * tool_result per tool_use block. After the first failure, skip the rest:
   * Claude planned them assuming the earlier actions succeeded.
   */
  List<ContentBlockParam> processToolCalls(Message response) {
      List<ContentBlockParam> toolResults = new ArrayList<>();
      boolean failed = false;
      for (ContentBlock block : response.content()) {
          // This example declares only the browser toolset; route other tools here if you add them.
          if (!block.isToolUse() || !block.asToolUse().toolsetName().equals(Optional.of("browser"))) {
              continue;
          }
          ToolUseBlock toolUse = block.asToolUse();
          ToolResultBlockParam result;
          if (failed) {
              result = browserResult(toolUse).content(HALT_TEXT).isError(true).build();
          } else {
              try {
                  Map<String, JsonValue> input =
                          (Map<String, JsonValue>) toolUse._input().asObject().get();
                  ToolResultBlockParam.Content output = handleBrowserAction(toolUse.name(), input);
                  // A real executor also adds a browser_state block to navigation and
                  // tab-management results; see "Track tabs with browser_state" on this page.
                  result = browserResult(toolUse).content(output).build();
              } catch (RuntimeException e) {
                  failed = true;
                  result = browserResult(toolUse).content("Error: " + e.getMessage()).isError(true).build();
              }
          }
          toolResults.add(ContentBlockParam.ofToolResult(result));
      }
      return toolResults;
  }
  ```

  ```php PHP
  const HALT_TEXT = 'Not executed: an earlier action in this turn failed.';

  function processToolCalls(Message $response): array
  {
      $toolResults = [];
      $failed = false;
      foreach ($response->content as $block) {
          // This example declares only the browser toolset; route other tools here if you add them.
          // Read toolset_name through array access: the SDK keeps it as raw data until a release types it.
          if (!($block instanceof ToolUseBlock) || ($block['toolsetName'] ?? $block['toolset_name'] ?? null) !== 'browser') {
              continue;
          }
          $result = ['type' => 'tool_result', 'tool_use_id' => $block->id, 'toolset_name' => 'browser'];
          if ($failed) {
              // A batch stops at its first failure; the remaining actions are answered without running
              $toolResults[] = [...$result, 'content' => HALT_TEXT, 'is_error' => true];
              continue;
          }
          try {
              // A real executor also returns a browser_state block on navigation and tab-management results
              $toolResults[] = [...$result, 'content' => handleBrowserAction($block->name, $block->input)];
          } catch (Throwable $e) {
              $failed = true;
              $toolResults[] = [...$result, 'content' => 'Error: ' . $e->getMessage(), 'is_error' => true];
          }
      }

      return $toolResults;
  }
  ```

  ```ruby Ruby
  NOT_EXECUTED = "Not executed: an earlier action in this turn failed."

  # Run the browser actions in Claude's response in order and build one
  # tool_result per tool_use block. After the first failure, skip the rest:
  # Claude planned them assuming the earlier actions succeeded.
  def process_tool_calls(response)
    tool_results = []
    failed = false
    response.content.each do |block|
      # This example declares only the browser toolset; route other tools here
      # if you add them.
      next unless block.type == :tool_use && block.toolset_name == "browser"

      result = { type: "tool_result", tool_use_id: block.id, toolset_name: "browser" }
      if failed
        result.update(content: NOT_EXECUTED, is_error: true)
      else
        begin
          # A String, or content blocks for a screenshot. A real executor also adds
          # a browser_state block to navigation and tab-management results.
          result[:content] = handle_browser_action(block.name, block.input)
        rescue => e
          result.update(content: "Error: #{e.message}", is_error: true)
          failed = true
        end
      end
      tool_results << result
    end
    tool_results
  end
  ```
</CodeGroup>

Dispatch each block on the pair (`toolset_name`, `name`) rather than on `name` alone, because a custom tool in the same request may share a member's name; [Client toolsets](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets) describes the parts of this contract both toolsets share. If Claude names a member your executor doesn't implement, or one you disabled, answer that block with an [error result](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#return-errors-from-your-executor) rather than dropping it.

When you stream the response, each member's `input` arrives as one complete `input_json_delta` rather than as fragments, so wait for the turn to finish before running the batch.

### Batch actions

A turn with several member calls is a batch action: run the calls in the order they appear, stop at the first failure, and answer every later call with `is_error: true` and the exact text `Not executed: an earlier action in this turn failed.` A batch uses the same response shape as [parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use); the difference is that you run the blocks in order rather than concurrently. Here Claude clicks the search box it found earlier, types a query, and presses Enter in one turn:

```json
{
  "role": "assistant",
  "content": [
    {
      "type": "tool_use",
      "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "name": "left_click",
      "toolset_name": "browser",
      "input": { "target": { "type": "ref", "ref": "ref_3" } }
    },
    {
      "type": "tool_use",
      "id": "toolu_01Ez4kLb1nQ2vXo8sJ9pWm3c",
      "name": "type",
      "toolset_name": "browser",
      "input": { "text": "install" }
    },
    {
      "type": "tool_use",
      "id": "toolu_01FkP8rTz6uYh2mNq4LsXw7v",
      "name": "key",
      "toolset_name": "browser",
      "input": { "text": "Enter" }
    }
  ]
}
```

Your application returns three `tool_result` blocks in one `user` message, each carrying `toolset_name` and a short text acknowledgment such as `Clicked element ref_3.` Pressing Enter loads a results page, so the `key` result also carries a `browser_state` block with the tab's updated URL ([Tab context on other results](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#tab-context-on-other-results)). If the click had failed instead, its result would carry your error text and the other two results would carry the halt text, as shown under [Return errors from your executor](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#return-errors-from-your-executor).

You don't need to return a screenshot after every call. Claude typically ends a batch with an observation call (`screenshot`, `read_page`, or `get_page_text`), and your application can also attach its own observation, such as a fresh screenshot or accessibility tree, as an extra content block on the last result in the batch to save a round trip. Because a tab-management result must be exactly one `browser_state` block, attach it to the last result that isn't a tab-management call.

If your executor can run only one call per round trip, set `disable_parallel_tool_use` to `true` in `tool_choice` and Claude returns at most one member call per turn, at the cost of more round trips ([Disable parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use#disable-parallel-tool-use)). The rest of the contract under [Batch actions for the computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#batch-actions) carries over, including one `tool_result` for every `tool_use` in the next `user` message, except for two things: the halt text and what a successful result's `content` holds. Result content follows [Member tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#member-tools) on this page instead: a `new_tab`, `switch_tab`, `close_tab`, or `list_tabs` result is exactly one `browser_state` block with no text or image ([Tab management results](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#tab-management-results)), and any other member's result may add a `browser_state` block to its text or image ([Tab context on other results](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#tab-context-on-other-results)). Where cache breakpoints inside a batch take effect is described in the `cache_control` row of the computer use tool's [Tool parameters](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#tool-parameters).

### Targets and coordinates

Member tools that act on a location take a `target` object, which is either a viewport-pixel coordinate or a reference to an element that `read_page` or `find` returned. The [Member tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#member-tools) tables write `Target` for a parameter that accepts either shape.

| Shape              | `target.type`  | Fields                                         | Accepted by                                                                                                                                                                               |
| ------------------ | -------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CoordinateTarget` | `"coordinate"` | `x`, `y` (integers, viewport pixels)           | `left_click`, `right_click`, `middle_click`, `double_click`, `triple_click`, `hover`, `left_click_drag` (`from` and `target`), `left_mouse_down`, `left_mouse_up`, `mouse_move`, `scroll` |
| `RefTarget`        | `"ref"`        | `ref` (an element reference such as `"ref_2"`) | `left_click`, `right_click`, `middle_click`, `double_click`, `triple_click`, `hover`, `scroll_to`, `form_input`, `file_upload`                                                            |

**Coordinates are viewport pixels**, the pixel space of a full-viewport `screenshot` with the origin at the top left of the rendered page; there's no surrounding desktop or window frame. The toolset declares no display dimensions and Claude infers the viewport size from the screenshots you return, so keep them one consistent size. A `zoom` doesn't change the frame, so its `region` and any coordinates Claude emits after seeing the zoomed image are still full-viewport pixels.

**Screenshots must fit the image limits.** The API doesn't downscale toolset images: a screenshot or zoom image over your model's [image size limits](https://platform.claude.com/docs/en/build-with-claude/vision#evaluate-image-size), or over the stricter per-image limit that applies once a request holds [more than 20 images](https://platform.claude.com/docs/en/build-with-claude/vision#request-limits), is rejected. Resize before returning, and scale Claude's coordinates back up by the inverse of your factor before dispatching them ([Size screenshots to fit image limits](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#handle-coordinate-scaling-for-higher-resolutions)).

**Element references come from `read_page` and `find`.** Each element in their output carries a tag such as `[ref_2]`, as in the Quick start result:

```text wrap
link "Documentation" [ref_1]
link "Getting started" [ref_2]
textbox "Search docs" [ref_3]
button "Search" [ref_4]
link "Pricing" [ref_5]
```

Claude passes a reference back as a `{"type": "ref", "ref": "ref_2"}` target on a later click, `hover`, `scroll_to`, `form_input`, or `file_upload` call, or as the `ref` parameter on `read_page` to read a subtree. Your executor assigns the references, keeps the mapping from each one to the underlying node (an accessibility-node ID, a stored selector, or equivalent), and acts on that node when a reference comes back.

References are scoped to the tab that produced them and stay valid until that tab navigates or its DOM changes materially. The API can't detect a stale or unknown reference, so when Claude passes a reference your executor no longer recognizes, return an error result such as `Error: ref_3 is stale or not found on the current page. Re-read the page to get fresh references.` Claude then reads the page again. Don't renumber references you've already handed out for a tab until it navigates, because that silently invalidates references Claude still holds.

Claude uses both targeting styles and switches between them based on what the page exposes; your prompt and what your executor returns steer the choice:

* **Prefer references where the page has a usable accessibility tree.** A reference survives layout shifts and reflows that make pixel coordinates fragile, and lets Claude act on controls that are hard to hit with a pointer.
* **Fall back to coordinates for content the tree doesn't describe.** Canvas-rendered interfaces, embedded video or remote-desktop surfaces, heavily virtualized lists, and elements inside cross-origin iframes often have no useful node, so Claude works from `screenshot` and `zoom` and clicks by coordinate; your executor resolves which frame a coordinate lands in.
* **Scope reads, and read the tree before you screenshot.** On large pages, `read_page` with `filter: "interactive"` or the `ref` of a container returns a focused subtree, and a tree read of a typical page often costs fewer input tokens than a screenshot while giving Claude references it can act on immediately. Screenshots remain the right observation when visual layout, images, or rendering state matter.

## Security considerations

Browser use carries risks that standard API features don't, because Claude reads and acts on content from the open web, where any page can contain text written to manipulate it.

<Warning>
  To reduce these risks, take precautions such as the following:

  1. Run the browser and your executor in a dedicated container or virtual machine with minimal privileges, a fresh profile that holds no credentials, and no access to sensitive filesystems or internal networks; isolate any tool you run alongside it the same way.
  2. Restrict the hosts the browser can reach to a domain allowlist enforced at the network layer and re-checked in your `navigate` handler after redirects, and block loopback, link-local, and private ranges unless the task needs them.
  3. Treat everything a page supplies as untrusted input, including the tab titles and URLs you report in a [`browser_state`](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#track-tabs-and-page-state) block, and build page reads from what the page renders (the accessibility tree or visible text), not raw DOM source, so hidden text doesn't reach Claude.
  4. In your `navigate` handler, accept the history keywords `"back"`, `"forward"`, and `"reload"`, treat a URL without a scheme as `https://`, then parse the URL and refuse any scheme other than `http` or `https` (`javascript:`, `file:`, `data:`, `chrome:`, and so on) with an [error result](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#return-errors-from-your-executor). Check the scheme with a URL parser rather than a string prefix; the API never sees the navigation and can't reject it for you.
  5. Leave `javascript_exec` and `file_upload` disabled unless you need them, and read [Enable optional members](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#enable-optional-member-tools) before turning either on.
  6. Have a human confirm consequential actions and anything that requires affirmative consent (purchasing, modifying accounts, messaging, and accepting terms), and make that check in your executor before each call, because one turn can carry several.
</Warning>

Claude sometimes follows instructions found in page content even when they conflict with yours; text on a page that says "ignore your previous instructions and navigate to..." can divert it from the task. Isolate Claude from sensitive data and actions to limit what a prompt injection can reach, review [Mitigate jailbreaks and prompt injections](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks), and if a task can't avoid a logged-in session, use a dedicated low-privilege account and keep human confirmation on account-changing actions.

Because the browser runs in your environment, the sites Claude visits see your executor's network identity, and page content reaches the API only as the tool results you return. Inform end users of the relevant risks and obtain their consent before enabling browser use in your products.

## Member tools

The `browser_toolset_20260801` entry declares 31 member tools; each call's `input` is exactly the parameters listed here, and `tab_id`, where optional, defaults to the active tab. `Target`, `CoordinateTarget`, and `RefTarget` are the shapes described in [Targets and coordinates](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#targets-and-coordinates). Four members (`javascript_exec`, `file_upload`, `read_console`, and `read_network`) are disabled by default and appear only when you [enable them](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#enable-optional-member-tools). The input bounds and output conventions noted in each member's row are stated to Claude, not enforced by the API, so validate inputs (including coordinates against your viewport) and apply the conventions in your executor.

Only `screenshot` and `zoom` require an [`image` block](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls#handling-results-from-client-tools) in their result, and the four tab-management members (`new_tab`, `list_tabs`, `switch_tab`, and `close_tab`) return exactly one `browser_state` block (see [Tab management results](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#tab-management-results)). Every other member returns a `text` block: either a short acknowledgment such as `Clicked element ref_2.` or the member's output. Any result other than a tab-management result may also carry an `image` block, typically a screenshot taken after the action, so Claude sees the outcome without a separate `screenshot` call; [Batch actions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#batch-actions) shows where to attach one in a batch. A member `tool_result` may contain only `text`, `image`, and `browser_state` content blocks.

### Navigation and capture

| Member       | Input               | Description                                                                                                                                                                                                                                                                                     |
| ------------ | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `navigate`   | `url`, `tab_id?`    | Load an `http` or `https` URL, or move through history with `"back"`, `"forward"`, or `"reload"`. Treat a URL without a scheme as `https://` and refuse any other scheme with an error result. Return a short acknowledgment, plus a `browser_state` block when the tab's URL or title changed. |
| `screenshot` | `tab_id?`           | Capture the viewport and return an `image` block.                                                                                                                                                                                                                                               |
| `zoom`       | `region`, `tab_id?` | Return a cropped, upscaled `image` of `region`, given as `[x0, y0, x1, y1]` in viewport pixels, for closer inspection of small text or controls.                                                                                                                                                |

### Pointer

| Member            | Input                                                                       | Description                                                                                                                                                    |
| ----------------- | --------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `left_click`      | `target: Target`, `modifiers?`, `tab_id?`                                   | Left-click a coordinate or a referenced element. `modifiers` is a chord held during the click, for example, `"shift"` or `"ctrl+shift"`.                       |
| `right_click`     | `target: Target`, `modifiers?`, `tab_id?`                                   | Right-click a coordinate or element.                                                                                                                           |
| `middle_click`    | `target: Target`, `modifiers?`, `tab_id?`                                   | Middle-click a coordinate or element.                                                                                                                          |
| `double_click`    | `target: Target`, `modifiers?`, `tab_id?`                                   | Double left-click a coordinate or element.                                                                                                                     |
| `triple_click`    | `target: Target`, `modifiers?`, `tab_id?`                                   | Triple left-click a coordinate or element, which typically selects a line or paragraph.                                                                        |
| `hover`           | `target: Target`, `tab_id?`                                                 | Move the pointer over a coordinate or element without clicking.                                                                                                |
| `left_click_drag` | `from: CoordinateTarget`, `target: CoordinateTarget`, `tab_id?`             | Press at `from`, drag to `target`, and release.                                                                                                                |
| `left_mouse_down` | `target: CoordinateTarget`, `tab_id?`                                       | Press and hold the left button at a coordinate; pair with `left_mouse_up` for a custom drag.                                                                   |
| `left_mouse_up`   | `target: CoordinateTarget`, `tab_id?`                                       | Release the left button at a coordinate.                                                                                                                       |
| `mouse_move`      | `target: CoordinateTarget`, `tab_id?`                                       | Move the pointer to a coordinate.                                                                                                                              |
| `scroll`          | `target: CoordinateTarget`, `scroll_direction`, `scroll_amount?`, `tab_id?` | Scroll at a viewport position. `scroll_direction` is `"up"`, `"down"`, `"left"`, or `"right"`; `scroll_amount` is in scroll-wheel notches, 1 to 10, default 3. |
| `scroll_to`       | `target: RefTarget`, `tab_id?`                                              | Scroll a referenced element into view.                                                                                                                         |

### Keyboard and timing

| Member     | Input                         | Description                                                                                                                                                                               |
| ---------- | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type`     | `text`, `tab_id?`             | Type a literal string at the current focus.                                                                                                                                               |
| `key`      | `text`, `repeat?`, `tab_id?`  | Press a key or chord. `text` is a single key (`"Enter"`), a chord joined with `+` (`"ctrl+a"`), or a space-separated sequence (`"Backspace Backspace"`); `repeat` is 1 to 100, default 1. |
| `hold_key` | `text`, `duration`, `tab_id?` | Hold a key or chord for `duration` seconds, 0 to 30.                                                                                                                                      |
| `wait`     | `duration`, `tab_id?`         | Pause for `duration` seconds, 0 to 30.                                                                                                                                                    |

### Page reading

| Member          | Input                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `read_page`     | `filter?`, `depth?`, `ref?`, `tab_id?` | Return the page's accessibility tree as text with each element tagged with a reference such as `[ref_2]`. With `filter` omitted, return every visible element; with `"interactive"`, only visible interactive elements; with `"all"`, also elements outside the viewport. `depth` caps the tree depth (minimum 1, default 15) and `ref` scopes the read to that element's subtree. Cap the output at 50,000 characters and say so in the text; Claude then narrows with a smaller `depth` or a `ref`. |
| `find`          | `query`, `tab_id?`                     | Search for elements matching a natural-language description such as `"search field"` or `"add to cart button"`, and return up to 20 matches in the same tagged format as `read_page`.                                                                                                                                                                                                                                                                                                                 |
| `get_page_text` | `tab_id?`                              | Return the page's visible text as plain text, prioritizing the main article content; suited to articles, documentation, and other text-heavy pages.                                                                                                                                                                                                                                                                                                                                                   |

### Forms and files

| Member                              | Input                                                     | Description                                                                                                                                                                                                                                                                      |
| ----------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `form_input`                        | `target: RefTarget`, `value`, `tab_id?`                   | Set a form element's value directly. `value` is a `string`, `number`, or `boolean`; use a `boolean` for checkboxes and an option's value or visible text for selects.                                                                                                            |
| `file_upload` (disabled by default) | `target: RefTarget`, `paths?`, `document_ids?`, `tab_id?` | Set the files on a file-input element from `paths` on the executor's filesystem, `document_ids` your application has staged, or both; at least one is required. See [Upload files](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#upload-files). |

### Diagnostics and scripting

| Member                                  | Input             | Description                                                                                                                                                                                                                                                                      |
| --------------------------------------- | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `read_console` (disabled by default)    | `tab_id?`         | Return the tab's console entries (log, warning, and error lines) accumulated since the last read, one line per entry. See [Read console and network activity](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#read-console-and-network-activity). |
| `read_network` (disabled by default)    | `tab_id?`         | Return the tab's network requests (method, URL, status, MIME type, timing) since the last read, one line per entry.                                                                                                                                                              |
| `javascript_exec` (disabled by default) | `text`, `tab_id?` | Run `text` as JavaScript in the page context and return the value of the last expression as text. See [Enable optional members](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#enable-optional-member-tools).                                    |

### Tab management

| Member       | Input               | Description                            |
| ------------ | ------------------- | -------------------------------------- |
| `new_tab`    | (none)              | Open a tab and make it the active tab. |
| `list_tabs`  | (none)              | Report the tab inventory.              |
| `switch_tab` | `tab_id` (required) | Make `tab_id` the active tab.          |
| `close_tab`  | `tab_id` (required) | Close `tab_id`.                        |

On success, each of these returns exactly one `browser_state` block and no text or image; see [Tab management results](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#tab-management-results).

## Configure the toolset

Besides `type`, the toolset entry accepts `configs`, `cache_control`, and `allowed_callers`; the rules these fields share with the computer use toolset are listed under [Client toolsets](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets), and this section covers the browser-specific defaults. `configs` is an object keyed by member name, and each member's value accepts two fields:

| Field           | Default                                                                                                                                                             | Meaning                                                                                                                                                                                                                                                                                                                                          |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `enabled`       | `true`, except `false` for the four [optional members](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#enable-optional-member-tools) | Whether the member is offered to Claude.                                                                                                                                                                                                                                                                                                         |
| `defer_loading` | `false`                                                                                                                                                             | Whether the toolset's definition is deferred for tool search. Must resolve to the same value on every enabled member. With the four optional members left disabled, deferring the toolset means setting it on the other 27; see [Client toolsets](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets). |

### Enable or disable member tools

List only the members you want to change in `configs`; every member you omit keeps its default. For example, an executor that implements console reads but not low-level pointer or key-hold control turns `read_console` on and withholds three members:

```json
{
  "type": "browser_toolset_20260801",
  "configs": {
    "read_console": { "enabled": true },
    "left_mouse_down": { "enabled": false },
    "left_mouse_up": { "enabled": false },
    "hold_key": { "enabled": false }
  }
}
```

A disabled member disappears from the definition Claude sees; that doesn't guarantee Claude never names it, so your executor still answers such a call with an [error result](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#return-errors-from-your-executor).

### Combine with other tools

Declare the browser use tool alongside your own tools and other Anthropic-provided tools in the same `tools` array. A custom tool may share a member's name (your own `navigate`, for example), because `toolset_name` distinguishes Claude's calls, but no other entry may be named `browser`, and a request may contain only one browser toolset entry.

You can also declare it alongside the [computer use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool), either the toolset or an earlier computer use tool version. The two work independently, each in its own coordinate frame (viewport pixels here, desktop screenshot pixels there), and Claude's calls to members that share a name, such as `screenshot` or `key`, are told apart by `toolset_name`.

## Enable optional members

Four member tools are disabled by default: `javascript_exec` and `file_upload` because they widen what a manipulated page could make Claude do, and `read_console` and `read_network` because not every browser automation stack can supply those logs and they widen what page-controlled content reaches Claude. Enable each one with `configs` (for example, `"configs": {"file_upload": {"enabled": true}}`) only when your executor implements it and the task needs it.

### Upload files

`file_upload` sets the files on an `<input type="file">` element directly, which is more reliable than driving a native file chooser. Its `target` is a reference only, because the call needs the element's identity, and it takes `paths`, `document_ids`, or both:

* `paths` are file paths on the executor's filesystem, for deployments where the executor can read your application's files directly (the same condition under which you populate a download's `path`).
* `document_ids` are identifiers for files your application has staged for the browser, for deployments where it can't. Your application defines what the identifiers mean; scope their resolution the way you scope `paths`, to files staged for this task.

```json
{
  "type": "tool_use",
  "id": "toolu_01N7gVzFEfZjLjgsYwnrPgrF",
  "name": "file_upload",
  "toolset_name": "browser",
  "input": {
    "target": { "type": "ref", "ref": "ref_12" },
    "paths": ["/home/user/uploads/summary.pdf"],
    "tab_id": "tab-2"
  }
}
```

Claude writes these paths while it's reading untrusted pages, so an unrestricted implementation would let a malicious page direct the upload of any file the executor can read to a site the page controls. Enable the member only when your executor resolves each path (following symlinks and `..` segments) and accepts nothing outside a dedicated, allowlisted upload directory that holds only files meant for the task. Don't reuse the browser's download directory for this; if you do, every file a page causes the browser to download becomes uploadable.

### Run JavaScript in the page

`javascript_exec` runs the expression Claude writes in the page's context and returns the value of the last expression as text; Claude writes an expression, not a `return` statement. The code runs with the page's full privileges, including its cookies, storage, and same-origin requests. Enable the member only in sessions that hold no credentials, keep the domain allowlist from [Security considerations](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#security-considerations) in force, treat the returned value as untrusted input, and log the code Claude emits.

### Read console and network activity

`read_console` returns the tab's console entries and `read_network` returns its network requests, each as text with one line per entry accumulated since the previous read of that tab. A console line carries a log, warning, or error entry; a network line carries the method, URL, status, MIME type, and timing. Entries exist only from the moment your browser automation attached to the tab, so an empty result doesn't mean a tab that was already open had no traffic.

These members let Claude diagnose a misbehaving page (a failed request behind a spinner, a script error behind a dead button) without repeated screenshots. Console and network entries are page-controlled and often contain secrets such as tokens in request URLs, so redact credential-like values you don't want in Claude's context and truncate very long entries before returning them.

## Track tabs with `browser_state`

Claude addresses tabs by `tab_id`, your application is the source of truth for which tabs exist, and you report that state in a `browser_state` content block that Claude never sees directly: the API renders the text Claude reads from it.

```json
{
  "type": "browser_state",
  "tabs": [
    {
      "tab_id": "tab-1",
      "title": "Documentation",
      "url": "https://example.com/docs",
      "active": true
    },
    { "tab_id": "tab-2", "title": "Pricing", "url": "https://example.com/pricing" }
  ]
}
```

* `tabs` is the full inventory of open tabs after the call, not a delta. It may be empty; whenever it isn't, exactly one entry carries `"active": true`.
* `state_changes` (not shown here) reports side effects of the call: a `tab_opened` entry for each tab the call opened that's still open when it finishes, whose `tab_id` must also appear in `tabs`, and [download events](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#report-downloads). Omit the field when there's nothing to report; an empty array is rejected.
* Send the block only on results that answer a browser member call, at most once per `tool_result`, and never on a result with `is_error: true`. You express "no tab state to report" by omitting the block.
* The API renders `tabs` into text for Claude as the next two sections describe; download entries in `state_changes` are validated but not rendered.

**You assign `tab_id` values.** Any stable string works, such as your automation library's page identifier or your own counter, as long as you don't reuse a `tab_id` while a tab with that identifier is still listed as open in an earlier result. The API enforces these limits on the block:

* Each `tab_id`, `title`, and `url` may be at most 4,096 characters, `tab_id` must be non-empty, and none may contain control characters (including newlines) or Unicode line or paragraph separators.
* A block may list at most 100 tabs and 200 state changes.
* The same limits apply to the `tab_id` Claude passes to `switch_tab` and `close_tab`, because the API renders it into the result text, so answer a call whose `tab_id` violates them with an error result instead of a `browser_state` block.

<Warning>
  Tab titles and URLs come from the page and render into text Claude reads, so they're a prompt-injection surface. The API renders URLs verbatim, so sanitize page-supplied URLs before populating `tabs`. It escapes double quotes and backslashes in titles when it renders them, so don't pre-escape titles (a pre-escaped title reaches Claude double-escaped); truncating or dropping suspicious titles is still worthwhile. The length and character limits the API enforces are a floor, not a defense.
</Warning>

### Tab management results

For `new_tab`, `switch_tab`, `close_tab`, and `list_tabs`, a successful result's `content` is exactly one `browser_state` block with no text or image, and the API writes the text Claude sees. A `new_tab` result's block must also carry exactly one `tab_opened` state change whose `tab_id` matches the entry marked `active: true`.

| Member       | Text Claude sees                                                                                                            |
| ------------ | --------------------------------------------------------------------------------------------------------------------------- |
| `switch_tab` | `Switched to tab {tab_id}`, taken from the call's `input.tab_id`                                                            |
| `close_tab`  | `Closed tab {tab_id}`, taken from the call's `input.tab_id`                                                                 |
| `new_tab`    | `Created new tab with tab_id: {tab_id}, URL: {url}. It is now the current tab.`, taken from the entry marked `active: true` |
| `list_tabs`  | `Available tabs:` followed by one line per tab, or `No tabs available` when `tabs` is empty                                 |

A `list_tabs` result whose block lists two tabs with the first one active renders as follows, with each line indented two spaces and `(current)` appended to the active tab only:

```text wrap
Available tabs:
  • tab_id tab-1: "Documentation" (https://example.com/docs) (current)
  • tab_id tab-2: "Pricing" (https://example.com/pricing)
```

An error result for one of these members is the reverse: ordinary error text in `content`, `is_error: true`, and no `browser_state` block.

For example, when Claude calls `new_tab` (its `input` is empty), your executor opens the tab, makes it active, and returns the inventory with one `tab_opened` entry:

```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01WvHSbQVV9j5nWGvTmk4vNL",
      "toolset_name": "browser",
      "content": [
        {
          "type": "browser_state",
          "tabs": [
            { "tab_id": "tab-1", "title": "Documentation", "url": "https://example.com/docs" },
            { "tab_id": "tab-2", "title": "Pricing", "url": "https://example.com/pricing" },
            { "tab_id": "tab-3", "title": "", "url": "about:blank", "active": true }
          ],
          "state_changes": [{ "type": "tab_opened", "tab_id": "tab-3" }]
        }
      ]
    }
  ]
}
```

Claude sees `Created new tab with tab_id: tab-3, URL: about:blank. It is now the current tab.` Report the URL the tab was opened at, as here, not one it later redirects to; later results report the tab's then-current URL.

### Tab context on other results

On every other member the block is optional: send it when the set of open tabs, the active tab, or a tab's title or URL changed, or when there are `state_changes` to report, and always include the full `tabs` inventory. When a result carries both text and a `browser_state` block, the API appends a `Tab Context` footer to that result's text, separated from your text by a blank line, so Claude receives the new state without a separate `list_tabs` call:

```text wrap
Tab Context:
- Executed on tab_id: tab-1
- Available tabs:
  • tab_id tab-1: "Documentation" (https://example.com/docs)
  • tab_id tab-2: "Pricing" (https://example.com/pricing)
```

`Executed on` names the tab the call ran on, which is its `tab_id` input when present and otherwise the active tab, and the footer's tab lines carry no `(current)` marker. Don't append this text yourself; send the structured block and let the API render it. The footer is deduplicated, so identical tab state isn't rendered again on later results and populating the block liberally costs nothing.

Three cases render no footer even when the block is present:

* Any `zoom` result.
* A result with no `text` block (an image-only `screenshot` result, for example). Nothing is rendered or remembered for that result; the tab context appears on the next result that carries both text and a `browser_state` block, so include a short text block alongside the image when you want Claude to see a tab change on that same result.
* A result whose `tabs` list is empty on a call that carried no `tab_id`, because there's no tab to name.

For example, when Claude clicked the "Pricing" link (`ref_5`) earlier in this session, the page opened it in a new tab Claude didn't ask for, and without a report Claude would have to call `list_tabs` to discover it. Return the click's acknowledgment plus a block whose `state_changes` names the opened tab, marking whichever tab your executor left active:

```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01EgTXj1FjE2FCTt2zNFWLao",
      "toolset_name": "browser",
      "content": [
        { "type": "text", "text": "Clicked element ref_5." },
        {
          "type": "browser_state",
          "tabs": [
            {
              "tab_id": "tab-1",
              "title": "Documentation",
              "url": "https://example.com/docs",
              "active": true
            },
            { "tab_id": "tab-2", "title": "Pricing", "url": "https://example.com/pricing" }
          ],
          "state_changes": [{ "type": "tab_opened", "tab_id": "tab-2" }]
        }
      ]
    }
  ]
}
```

Claude sees `Clicked element ref_5.` followed by the Tab Context footer shown earlier. A tab opened during a call that failed gets no `tab_opened` entry, because error results carry no `browser_state`; it appears in the `tabs` inventory of the next successful result instead. In a batch, attach the block to the result of the call during which the change happened, and give every successful tab-management result its own block even when an earlier result in the same turn reported the same state.

### Report downloads

When a click or navigation starts a file download, report it in `state_changes` on the result of the call during which it happened, correlated across results by a `download_id` you assign. Downloads run asynchronously and can span several results, so there are three event types:

| `type`               | Fields                                       | When to send                                                                                                                                                                                                                                                                                                                                            |
| -------------------- | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `download_started`   | `download_id`, `url`                         | On the result of the call during which the download began. `url` is the final URL the file is served from, after redirects.                                                                                                                                                                                                                             |
| `download_completed` | `download_id`, `url`, `path?`, `size_bytes?` | On the result of whichever later call is running when the download finishes. Include `path` only when another tool in the same environment (for example, the [bash tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool) or `file_upload`) can read the file there; otherwise `download_id` is the download's only identifier. |
| `download_failed`    | `download_id`, `url`, `error?`               | When the download fails or is canceled, with the reason in `error` if the browser provides one.                                                                                                                                                                                                                                                         |

The API validates these entries but doesn't render them into text Claude sees, so when Claude needs to act on the file, also mention the file name or `path` in the same result's `text` block.

For example, a click on "Download price list (CSV)" (`ref_8`) in the Pricing tab starts a download, so the click's result carries a `download_started` entry with `download_id` `"dl-1"` and the file's URL. The download finishes while a later `screenshot` call is running, so that result's `content` holds the image, a text block such as `Screenshot captured. Download complete: /home/user/downloads/price-list.csv (48,213 bytes).`, and this `browser_state` block reporting the completion under the same `download_id`:

```json
{
  "type": "browser_state",
  "tabs": [
    { "tab_id": "tab-1", "title": "Documentation", "url": "https://example.com/docs" },
    {
      "tab_id": "tab-2",
      "title": "Pricing",
      "url": "https://example.com/pricing",
      "active": true
    }
  ],
  "state_changes": [
    {
      "type": "download_completed",
      "download_id": "dl-1",
      "url": "https://example.com/pricing/price-list.csv",
      "path": "/home/user/downloads/price-list.csv",
      "size_bytes": 48213
    }
  ]
}
```

Download reports follow these rules:

* At most one entry per `download_id` in a single block, so a download that starts and finishes during the same call reports only `download_completed`.
* Never send `state_changes` on an `is_error: true` result; report a download event that occurred during a failed call on the next successful result.
* `state_changes` isn't an inventory of downloads in progress; report each event once.
* Each entry carries only the fields its `type` declares. `size_bytes` is a non-negative integer, `download_id` is non-empty, and `download_id`, `url`, `path`, and `error` are each at most 4,096 characters with no control characters or Unicode line or paragraph separators. The `url` comes from the remote server and often carries signed query-string credentials after redirects, so strip query parameters you don't want in Claude's context and sanitize it before reporting it or using it in a filesystem path.

## Handle errors

Report a failed call to Claude as an ordinary error result: `is_error: true`, text content that says what went wrong, `toolset_name` echoed, and no `browser_state` block.

### Return errors from your executor

Make error text specific, because Claude reads it and adapts: `Error: Navigation to https://example.com/status timed out after 30 seconds. The page may be unavailable.` gives Claude something to act on where a bare `Error: navigation failed` doesn't. Other common cases:

<AccordionGroup>
  <Accordion title="Refused navigation scheme">
    ```json
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01LeUTyqkhRxBFq1QTG3pkwN",
      "toolset_name": "browser",
      "is_error": true,
      "content": "Error: Navigation refused. Only http and https URLs are allowed."
    }
    ```
  </Accordion>

  <Accordion title="Stale or unknown element reference">
    ```json
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
      "toolset_name": "browser",
      "is_error": true,
      "content": "Error: ref_3 is stale or not found on the current page. Re-read the page to get fresh references."
    }
    ```
  </Accordion>

  <Accordion title="Disabled or unimplemented member">
    ```json
    {
      "type": "tool_result",
      "tool_use_id": "toolu_013h2Q55HcNwVyapSpy2s5ZG",
      "toolset_name": "browser",
      "is_error": true,
      "content": "Error: javascript_exec is not enabled in this environment."
    }
    ```
  </Accordion>

  <Accordion title="Skipped after an earlier failure in the turn">
    When the `left_click` on `ref_3` from [Batch actions](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#batch-actions) fails with the stale-reference error shown earlier, the `type` and `key` calls after it each get this result:

    ```json
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01FkP8rTz6uYh2mNq4LsXw7v",
      "toolset_name": "browser",
      "is_error": true,
      "content": "Not executed: an earlier action in this turn failed."
    }
    ```
  </Accordion>
</AccordionGroup>

### Request errors

The API validates the toolset entry and every member `tool_use` and `tool_result` block in the conversation. When one is malformed, the API returns an `invalid_request_error` before Claude runs. In the following table, the left column names what you sent.

| Request                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Why it fails and what to do                                                                                                                                                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| An option or combination the toolset entry doesn't accept, for example, a `name`, `strict: true`, `input_examples`, `defer_loading` on the entry itself, a `configs` key that isn't a member name, a field other than `enabled` or `defer_loading` in a member's `configs` value ([Configure the toolset](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#configure-the-toolset)), enabled members whose `defer_loading` values differ ([Configure the toolset](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#configure-the-toolset)), a `configs` that leaves no member enabled, a code execution caller in `allowed_callers`, the legacy `fine-grained-tool-streaming-2025-05-14` beta header on the request, a `tool_choice` of type `tool` naming `browser` or a member, or a second browser toolset entry or another tool named `browser` | These aren't supported on client toolsets. See [Client toolsets](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets) for each rule and its alternative.                                                              |
| A `tool_result` answering a member call without `"toolset_name": "browser"` or with a different value, or `toolset_name` on a result whose call wasn't a member call                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Echo `toolset_name` exactly on member results, and only on them.                                                                                                                                                                                               |
| A member `tool_use` from an earlier turn with no matching `tool_result`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Answer every member call, including the ones you didn't run after a failure.                                                                                                                                                                                   |
| A content block other than `text`, `image`, or `browser_state` in a member result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Member results accept only those three block types.                                                                                                                                                                                                            |
| A `browser_state` block that breaks a rule in [Track tabs with `browser_state`](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#track-tabs-and-page-state), for example, one on an `is_error: true` result or on a result that doesn't answer a browser member call, more than one in a result, a non-empty `tabs` without exactly one `active: true` entry, a duplicate `tab_id`, an empty `state_changes` array, a `tab_opened` whose `tab_id` isn't in `tabs`, two state changes for one `download_id` or a state-change field its `type` doesn't declare ([Report downloads](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#report-downloads)), or a field over its limits                                                                                                                                                                  | Fix the block. "Nothing to report" is expressed by omitting the block or the `state_changes` field, never by an empty value.                                                                                                                                   |
| A successful `new_tab`, `switch_tab`, `close_tab`, or `list_tabs` result whose `content` isn't exactly one `browser_state` block, or a `new_tab` result without exactly one `tab_opened` matching the active tab                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The API renders these results from the block and needs it in that exact shape; see [Tab management results](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#tab-management-results).                                            |
| An `image` in a result over your model's [image size limits](https://platform.claude.com/docs/en/build-with-claude/vision#evaluate-image-size), or over the stricter per-image limit that applies once the request holds [more than 20 images](https://platform.claude.com/docs/en/build-with-claude/vision#request-limits), counting screenshots and `zoom` images in earlier results                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The API doesn't downscale toolset images. Resize screenshots before returning them ([Size screenshots to fit image limits](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#handle-coordinate-scaling-for-higher-resolutions)). |
| A `model` that doesn't support `browser_toolset_20260801`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | See [Compatibility](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool#compatibility) for the supported models.                                                                                                                    |

## Limitations

* **Platform availability:** Browser use is available on the Claude API only.
* **Whole-input streaming only:** When you stream, each member's `input` arrives as one complete `input_json_delta` ([Client toolsets](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference#client-toolsets)).
* **Element references are best-effort:** Highly dynamic pages (virtualized lists, canvas-rendered interfaces, pages that re-render on scroll) might not expose stable references, and Claude falls back to screenshots and coordinate clicks there.
* **`read_console` and `read_network` depend on your browser automation:** They report only what it can capture, and only from the moment it attached to a tab.
* **General agent limitations apply:** Latency, vision accuracy, and prompt-injection risks carry over from computer use (see the computer use tool's [Limitations](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#understand-computer-use-limitations)), and its guidance under [Optimize model performance with prompting](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#optimize-model-performance-with-prompting), [Manage screenshot history](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#manage-screenshot-history), and [Follow implementation best practices](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool#follow-implementation-best-practices) (action delays, action validation, and logging) applies to browser executors too.

## Pricing and data retention

Browser use follows the standard [tool use pricing](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview#pricing). When using the browser use tool:

**Toolset definition overhead:** Declaring `browser_toolset_20260801` with its default members adds about 6,600 input tokens to a request (about 6,610 on Claude Fable 5, Claude Mythos 5, Claude Opus 5, and Claude Opus 4.8, and about 6,670 on Claude Sonnet 5), which covers the member tool definitions and the tool use system prompt. Enabling all four optional members adds about 880 tokens, and disabling members with `configs` reduces the count. The exact count for a request is reported in the response `usage`, and you can estimate it in advance with the [token counting endpoint](https://platform.claude.com/docs/en/build-with-claude/token-counting).

**Additional token consumption:**

* Screenshot and zoom images returned in tool results, billed as image input (see [Vision pricing](https://platform.claude.com/docs/en/build-with-claude/vision#evaluate-image-size))
* Text tool results returned to Claude, such as accessibility trees, page text, and console or network entries

<Note>
  If you also use the computer use tool, bash tool, text editor tool, or your own tools alongside browser use, those tools have their own token costs as documented on their respective pages.
</Note>

The browser session, downloads, and uploaded files stay in your environment; the screenshots, page text, and tab state you return are part of your API request content and follow the standard retention policy, or your ZDR arrangement if you have one. The browser use tool is ZDR eligible; see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention) for retention periods and eligibility across features.

## Next steps

<CardGroup cols={3}>
  <Card title="Computer use tool" icon="computer" href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool">
    Give Claude control of a full desktop when the task leaves the browser; its implementation guidance applies to browser executors too.
  </Card>

  <Card title="Handle tool calls" icon="wrench" href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls">
    Format `tool_result` blocks, return images and errors, and continue the conversation.
  </Card>

  <Card title="Tool reference" icon="book" href="https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference">
    Browse client toolsets and every other Anthropic-provided tool, with their versions and parameters.
  </Card>
</CardGroup>
