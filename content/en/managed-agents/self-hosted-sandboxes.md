---
title: Self-hosted sandboxes
url: https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes
description: Run Claude Managed Agents sessions in self-hosted sandboxes, keeping tool execution, files, and network egress in your own infrastructure.
featureMetadata:
  topic:
    title: Managed Agents
    url: https://platform.claude.com/docs/en/managed-agents/overview
  status: beta
  betaHeader: managed-agents-2026-04-01
---

By default, Managed Agents executes tools and code inside [Anthropic-managed cloud sandboxes](https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference). Self-hosted sandboxes keep the orchestration on Anthropic's side but move tool execution into infrastructure you control. The agent's files, processes, and network traffic stay in your environment.

Self-hosting is a good fit when the agent needs to:

* Operate on data that cannot leave your network boundary
* Reach internal services that are not publicly routable
* Run under your organization's own compliance and audit controls

## How it works

A `self_hosted` environment acts as a work queue. You run an **environment worker**, a process on your own infrastructure that serves that queue:

1. You create a [session](https://platform.claude.com/docs/en/managed-agents/sessions) that targets the environment. Anthropic enqueues the session as a work item.
2. Your worker claims the work item and downloads the agent's [skills](https://platform.claude.com/docs/en/managed-agents/skills) and the session's [memory stores](https://platform.claude.com/docs/en/managed-agents/memory).
3. Claude runs on Anthropic's side and requests tool calls. Your worker runs each call locally and posts the result back.

Tool inputs and outputs still flow to Anthropic's control plane, so the model can see results and determine what to do next. Anthropic stores skills and memory stores. Your sandbox holds a copy for the session. See [Security model](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security) for the full data-flow boundary.

Self-hosted sandboxes support every Claude model available in Managed Agents. The model is configured on the agent, not the environment.

The `ant` CLI and the Python, TypeScript, and Go SDKs ship pre-built workers. Sandbox providers such as Cloudflare, Daytona, and Modal also publish their own [platform guides](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#platform-guides).

## Quickstart

This quickstart runs one always-on worker with the `ant` CLI, sends it a session, and confirms that the agent's tool calls ran on your host.

### Prerequisites

* **An agent:** If you don't have one, complete [Get started with Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/quickstart) first and note the agent ID.
* **A Linux host:** The host needs `/bin/bash` at that exact path. The worker needs only outbound HTTPS.
* **A Claude API key:** You use it from your own machine to create sessions and read queue stats. Keep it off the worker host, where agent tool calls could read it.
* **The `ant` CLI on your own machine:** The session and stats commands in this quickstart run there, not on the worker host. Install it the same way the [install step](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#run-your-first-session) does for the worker.

<Note>
  On [Claude Platform on AWS](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws), the worker authenticates with AWS IAM (SigV4) or an [API key generated in the AWS Console](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws#api-key-authentication), not an environment key. Attach the [`AnthropicSelfHostedEnvironmentAccess`](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#managed-policies) managed policy to the IAM principal your worker runs as. Environment keys generated in the Claude Console don't work with the Claude Platform on AWS endpoint.
</Note>

### Run your first session

<Steps>
  <Step title="Create a self-hosted environment">
    In the [Console](https://platform.claude.com/workspaces/default/environments): **Workspace > Environments > New > Self-hosted**

    Or through the API:

    <CodeGroup defaultLanguage="CLI">
      ```bash cURL
      curl -sS --fail-with-body https://api.anthropic.com/v1/environments \
        -H "x-api-key: $ANTHROPIC_API_KEY" \
        -H "anthropic-version: 2023-06-01" \
        -H "anthropic-beta: managed-agents-2026-04-01" \
        -H "content-type: application/json" \
        -d '{
          "name": "self-hosted",
          "config": {"type": "self_hosted"}
        }'
      ```

      <CodeGroupItem>
        ```bash CLI
        ant apply environment.yaml
        ```

        <File filename="environment.yaml">
          ```yaml
          # yaml-language-server: $schema=https://platform.claude.com/schemas/ant/beta/environment.json
          name: self-hosted
          config:
            type: self_hosted
          ```
        </File>
      </CodeGroupItem>

      ```python Python
      client = anthropic.Anthropic()

      environment = client.beta.environments.create(
          name="self-hosted", config={"type": "self_hosted"}
      )
      print(environment.id)
      ```

      ```typescript TypeScript
      const client = new Anthropic();

      const environment = await client.beta.environments.create({
        name: "self-hosted",
        config: { type: "self_hosted" }
      });
      console.log(environment.id);
      ```

      ```csharp C#
      using Anthropic.Models.Beta.Environments;

      var client = new AnthropicClient();

      var environment = await client.Beta.Environments.Create(
          new EnvironmentCreateParams
          {
              Name = "self-hosted",
              Config = new BetaSelfHostedConfigParams(),
          }
      );
      Console.WriteLine(environment.ID);
      ```

      ```go Go
      client := anthropic.NewClient()

      environment, err := client.Beta.Environments.New(context.Background(), anthropic.BetaEnvironmentNewParams{
      	Name: "self-hosted",
      	Config: anthropic.BetaEnvironmentNewParamsConfigUnion{
      		OfSelfHosted: &anthropic.BetaSelfHostedConfigParams{},
      	},
      })
      if err != nil {
      	panic(err)
      }
      fmt.Println(environment.ID)
      ```

      ```java Java
      import com.anthropic.models.beta.environments.BetaSelfHostedConfigParams;
      import com.anthropic.models.beta.environments.EnvironmentCreateParams;

      void main() {
          var client = AnthropicOkHttpClient.fromEnv();

          var environment = client.beta().environments().create(
              EnvironmentCreateParams.builder()
                  .name("self-hosted")
                  .config(BetaSelfHostedConfigParams.builder().build())
                  .build()
          );
          IO.println(environment.id());
      }
      ```

      ```php PHP
      $client = new Anthropic\Client();

      $environment = $client->beta->environments->create(
          name: 'self-hosted',
          config: ['type' => 'self_hosted'],
      );
      echo $environment->id, PHP_EOL;
      ```

      ```ruby Ruby
      client = Anthropic::Client.new

      environment = client.beta.environments.create(
        name: "self-hosted",
        config: {type: :self_hosted}
      )
      puts environment.id
      ```
    </CodeGroup>
  </Step>

  <Step title="Generate an environment key">
    In the Console, open the environment and click **Generate environment key**. The environment key authenticates the worker to its queue. You can generate one only in the Console, even for an environment you created through the API.

    Export the environment ID and key on the worker host:

    ```bash
    export ANTHROPIC_ENVIRONMENT_KEY="sk-ant-oat01-..."
    export ANTHROPIC_ENVIRONMENT_ID="env_..."
    ```
  </Step>

  <Step title="Install the ant CLI">
    Run this on the worker host.

    <Tabs>
      <Tab title="curl (Linux/WSL)">
        For Linux environments, download the release binary directly.

        ```bash
        VERSION=1.37.0
        OS=$(uname -s | tr '[:upper:]' '[:lower:]')
        case $(uname -m) in
          x86_64) ARCH=amd64 ;;
          aarch64) ARCH=arm64 ;;
        esac
        curl -fsSL "https://github.com/anthropics/anthropic-cli/releases/download/v${VERSION}/ant_${VERSION}_${OS}_${ARCH}.tar.gz" \
          | sudo tar -xz -C /usr/local/bin ant
        ```

        You can find all releases on the [GitHub releases page](https://github.com/anthropics/anthropic-cli/releases).
      </Tab>

      <Tab title="Homebrew (macOS)">
        ```bash
        brew install anthropics/tap/ant
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step title="Start the worker">
    Create the working directory, then start the worker. `--workdir` defaults to the current directory, so pass `/workspace` to match the system default.

    ```bash
    sudo mkdir -p /workspace && sudo chown "$USER" /workspace
    ant beta:worker poll --workdir /workspace
    ```

    The worker reads the two variables you exported and polls until you stop it.
  </Step>

  <Step title="Verify the worker is connected">
    On your own machine, set `ANTHROPIC_API_KEY` to your Claude API key (not the environment key) and `ANTHROPIC_ENVIRONMENT_ID` to the environment ID. Confirm that `workers_polling` is at least 1:

    ```bash
    ant beta:environments:work stats --environment-id "$ANTHROPIC_ENVIRONMENT_ID"
    ```

    If `workers_polling` stays at 0, see [Troubleshooting](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations#troubleshooting).
  </Step>

  <Step title="Start a session">
    Set `AGENT_ID` to your agent's ID. Create a session that targets the environment, then send it a task:

    ```bash
    SESSION_ID=$(ant beta:sessions create \
      --agent "$AGENT_ID" \
      --environment-id "$ANTHROPIC_ENVIRONMENT_ID" \
      --transform id --raw-output)

    ant beta:sessions:events send --session-id "$SESSION_ID" <<'YAML'
    events:
      - type: user.message
        content:
          - type: text
            text: Write the output of "uname -a" to hello.txt in your working directory.
    YAML
    ```

    The session waits in the environment's queue until a worker claims it. If no worker is connected, the session stays queued rather than failing.
  </Step>

  <Step title="Confirm the tools ran on your host">
    On the worker host, read the file the agent wrote:

    ```bash
    cat /workspace/hello.txt
    ```

    The file describes your own host's kernel, so the agent's tool calls ran there. To follow the agent's work as it happens, see [Session event stream](https://platform.claude.com/docs/en/managed-agents/events-and-streaming).
  </Step>
</Steps>

## How it differs from cloud environments

|                               | Cloud environment                      | Self-hosted sandbox                                   |
| ----------------------------- | -------------------------------------- | ----------------------------------------------------- |
| Where tools run               | Anthropic-managed sandboxes            | Your infrastructure                                   |
| Network reach                 | Anthropic's egress controls            | Your network policy                                   |
| File and GitHub repo mounting | Managed by Anthropic                   | Managed by you                                        |
| Memory stores                 | Mounted by Anthropic at `/mnt/memory/` | Downloaded to `/mnt/memory/` and synced by the worker |
| Lifecycle                     | Managed by Anthropic                   | Managed by you                                        |

For Zero Data Retention and HIPAA BAA eligibility, see [API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#feature-eligibility).

### Session resources

Self-hosted sandboxes support `memory_store` resources only. A session on a self-hosted environment that includes a `file` or `github_repository` resource is rejected with a 400 error:

```text wrap
Environment env_... is a self-hosted environment. `resources` are not supported with self-hosted environments.
```

[Deployments](https://platform.claude.com/docs/en/managed-agents/scheduled-deployments) that target a self-hosted environment follow the same rule. To give a session its own input files, see [Stage files for a session](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers#stage-files-for-a-session).

## Self-hosted sandboxes and MCP tunnels

Self-hosting controls *where the agent's code executes*. [MCP tunnels](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview) control *how Anthropic reaches MCP servers in your network*. The two are independent:

* A session in Anthropic's cloud sandboxes can reach private MCP servers through a tunnel.
* A self-hosted session can use either tunneled or public MCP servers.

Use both when you want execution and tool access to stay inside your boundary. To skip the tunnel, [wrap the MCP server as custom tools](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools#wrap-an-mcp-server-as-custom-tools) that your worker serves.

## Platform guides

These pages describe how to build a worker on any sandboxing platform. Platform-specific guides are also available:

* [AWS Lambda MicroVMs](https://docs.aws.amazon.com/lambda/latest/dg/microvms-integrations-claude-managed-agents.html)
* [Blaxel](https://docs.blaxel.ai/Tutorials/Claude-Managed-Agents)
* [Cloudflare](https://developers.cloudflare.com/sandbox/claude-managed-agents/)
* [Daytona](https://www.daytona.io/docs/en/guides/claude/claude-managed-agents)
* [E2B](https://e2b.dev/docs/agents/claude-managed-agents)
* [Fly.io](https://docs.sprites.dev/integrations/claude-managed-agents/)
* [GKE Agent Sandbox](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/tree/main/ai-ml/anthropic-agent-sandbox)
* [Modal](https://github.com/modal-labs/claude-managed-agents-modal-sandbox)
* [Namespace](https://namespace.so/docs/integrations/claude)
* [Superserve](https://docs.superserve.ai/integrations/managed-agents/claude-managed-agents)
* [Vercel](https://vercel.com/kb/guide/run-claude-managed-agent-tools-with-vercel-sandbox)

## Next steps

<CardGroup cols={2}>
  <Card title="Deploy workers" icon="play" href="https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-workers">
    Run the SDK worker, trigger workers from webhooks, or give each session its own sandbox.
  </Card>

  <Card title="Memory stores" icon="brain" href="https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory">
    Prepare the host, configure sync, and handle read-only stores and conflicts.
  </Card>

  <Card title="Custom tools and MCP servers" icon="tool" href="https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools">
    Serve your own tools from the worker, including tools from an MCP server inside your network.
  </Card>

  <Card title="Monitor and troubleshoot" icon="lightning" href="https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations">
    Read queue depth, stop sessions and workers cleanly, and fix common failures.
  </Card>

  <Card title="Worker reference" icon="book" href="https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference">
    CLI flags, environment variables, filesystem paths, and SDK helper options.
  </Card>

  <Card title="Security model" icon="lock" href="https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-security">
    Shared responsibility model for self-hosted sandbox environments.
  </Card>
</CardGroup>
