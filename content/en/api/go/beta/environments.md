# Environments

## Create Environment

`client.Beta.Environments.New(ctx, params) (*BetaEnvironment, error)`

**POST** `/v1/environments`

Create a new environment with the specified configuration.

### Parameters

- `params BetaEnvironmentNewParams`

  - `Name param.Field[string]`

    Body param: Human-readable name for the environment

    maxLength: 256, minLength: 1

  - `Config param.Field[BetaEnvironmentNewParamsConfigUnion] Optional`

    Body param: Environment configuration

    - `type BetaCloudConfigParamsResp struct{…}`

      Request params for `cloud` environment configuration.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `Type Cloud`

        Environment type

      - `Networking BetaCloudConfigParamsNetworkingUnionResp Optional`

        Network configuration policy. Omit on update to preserve the existing value.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

        - `type BetaLimitedNetworkParamsResp struct{…}`

          Limited network request params.

          Fields default to null; on update, omitted fields preserve the
          existing value.

          - `Type Limited`

            Network policy type

          - `AllowMCPServers bool Optional`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

          - `AllowPackageManagers bool Optional`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false` on creation. Must be `true` when `packages` are specified.

          - `AllowedHosts []string Optional`

            Specifies domains the container can reach.

      - `Packages BetaPackagesParamsResp Optional`

        Specify packages (and optionally their versions) available in this environment.

        When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

        Under `limited` networking, requires `networking.allow_package_managers` to be `true`.

        - `Apt []string Optional`

          Ubuntu/Debian packages to install

        - `Cargo []string Optional`

          Rust packages to install

        - `Gem []string Optional`

          Ruby packages to install

        - `Go []string Optional`

          Go packages to install

        - `Npm []string Optional`

          Node.js packages to install

        - `Pip []string Optional`

          Python packages to install

        - `Type BetaPackagesParamsType Optional`

          Package configuration type

          default: packages

    - `type BetaSelfHostedConfigParamsResp struct{…}`

      Request params for `self_hosted` environment configuration.

      - `Type SelfHosted`

        Environment type

  - `Description param.Field[string] Optional`

    Body param: Optional description of the environment

    maxLength: 1024

  - `Metadata param.Field[map[string, string]] Optional`

    Body param: User-provided metadata key-value pairs

  - `Scope param.Field[BetaEnvironmentNewParamsScope] Optional`

    Body param: The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. Only applicable for self-hosted environments. If not specified, defaults based on organization type.

    - `const BetaEnvironmentNewParamsScopeOrganization BetaEnvironmentNewParamsScope = "organization"`

    - `const BetaEnvironmentNewParamsScopeAccount BetaEnvironmentNewParamsScope = "account"`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaEnvironmentConfigUnion`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `type BetaCloudConfig struct{…}`

      `cloud` environment configuration.

      - `Networking BetaCloudConfigNetworkingUnion`

        Network configuration policy.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

        - `type BetaLimitedNetwork struct{…}`

          Limited network access.

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

          - `Type Limited`

            Network policy type

      - `Packages BetaPackages`

        Package manager configuration.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesType Optional`

          Package configuration type

          default: packages

      - `Type Cloud`

        Environment type

    - `type BetaSelfHostedConfig struct{…}`

      Configuration for self-hosted environments.

      - `Type SelfHosted`

        Environment type

  - `CreatedAt string`

    RFC 3339 timestamp when environment was created

  - `Description string`

    User-provided description for the environment; null when unset

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs

  - `Name string`

    Human-readable name for the environment

  - `Type Environment`

    The type of object (always 'environment')

    default: environment

  - `UpdatedAt string`

    RFC 3339 timestamp when environment was last updated

  - `Scope BetaEnvironmentScope Optional`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"`

    - `const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaEnvironment, err := client.Beta.Environments.New(context.TODO(), anthropic.BetaEnvironmentNewParams{
		Name: "python-data-analysis",
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaEnvironment.ID)
}
```

#### Response (200)

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## List Environments

`client.Beta.Environments.List(ctx, params) (*PageCursor[BetaEnvironment], error)`

**GET** `/v1/environments`

List environments with pagination support.

### Parameters

- `params BetaEnvironmentListParams`

  - `IncludeArchived param.Field[bool] Optional`

    Query param: Include archived environments in the response

  - `Limit param.Field[int64] Optional`

    Query param: Maximum number of environments to return

    maximum: 1000, minimum: 1

  - `Page param.Field[string] Optional`

    Query param: Opaque cursor from previous response for pagination. Pass the `next_page` value from the previous response.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaEnvironmentConfigUnion`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `type BetaCloudConfig struct{…}`

      `cloud` environment configuration.

      - `Networking BetaCloudConfigNetworkingUnion`

        Network configuration policy.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

        - `type BetaLimitedNetwork struct{…}`

          Limited network access.

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

          - `Type Limited`

            Network policy type

      - `Packages BetaPackages`

        Package manager configuration.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesType Optional`

          Package configuration type

          default: packages

      - `Type Cloud`

        Environment type

    - `type BetaSelfHostedConfig struct{…}`

      Configuration for self-hosted environments.

      - `Type SelfHosted`

        Environment type

  - `CreatedAt string`

    RFC 3339 timestamp when environment was created

  - `Description string`

    User-provided description for the environment; null when unset

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs

  - `Name string`

    Human-readable name for the environment

  - `Type Environment`

    The type of object (always 'environment')

    default: environment

  - `UpdatedAt string`

    RFC 3339 timestamp when environment was last updated

  - `Scope BetaEnvironmentScope Optional`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"`

    - `const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Environments.List(context.TODO(), anthropic.BetaEnvironmentListParams{})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

#### Response (200)

```json
{
  "data": [
    {
      "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
      "archived_at": null,
      "config": {
        "networking": {
          "allow_mcp_servers": false,
          "allow_package_managers": true,
          "allowed_hosts": [
            "api.example.com"
          ],
          "type": "limited"
        },
        "packages": {
          "apt": [
            "string"
          ],
          "cargo": [
            "string"
          ],
          "gem": [
            "string"
          ],
          "go": [
            "string"
          ],
          "npm": [
            "string"
          ],
          "pip": [
            "pandas",
            "numpy"
          ],
          "type": "packages"
        },
        "type": "cloud"
      },
      "created_at": "2026-03-15T10:00:00Z",
      "description": "Python environment with data-analysis packages.",
      "metadata": {},
      "name": "python-data-analysis",
      "type": "environment",
      "updated_at": "2026-03-15T10:00:00Z",
      "scope": "organization"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

## Get Environment

`client.Beta.Environments.Get(ctx, environmentID, query) (*BetaEnvironment, error)`

**GET** `/v1/environments/{environment_id}`

Retrieve a specific environment by ID.

### Parameters

- `environmentID string`

- `query BetaEnvironmentGetParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaEnvironmentConfigUnion`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `type BetaCloudConfig struct{…}`

      `cloud` environment configuration.

      - `Networking BetaCloudConfigNetworkingUnion`

        Network configuration policy.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

        - `type BetaLimitedNetwork struct{…}`

          Limited network access.

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

          - `Type Limited`

            Network policy type

      - `Packages BetaPackages`

        Package manager configuration.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesType Optional`

          Package configuration type

          default: packages

      - `Type Cloud`

        Environment type

    - `type BetaSelfHostedConfig struct{…}`

      Configuration for self-hosted environments.

      - `Type SelfHosted`

        Environment type

  - `CreatedAt string`

    RFC 3339 timestamp when environment was created

  - `Description string`

    User-provided description for the environment; null when unset

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs

  - `Name string`

    Human-readable name for the environment

  - `Type Environment`

    The type of object (always 'environment')

    default: environment

  - `UpdatedAt string`

    RFC 3339 timestamp when environment was last updated

  - `Scope BetaEnvironmentScope Optional`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"`

    - `const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaEnvironment, err := client.Beta.Environments.Get(
		context.TODO(),
		"env_011CZkZ9X2dpNyB7HsEFoRfW",
		anthropic.BetaEnvironmentGetParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaEnvironment.ID)
}
```

#### Response (200)

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Update Environment

`client.Beta.Environments.Update(ctx, environmentID, params) (*BetaEnvironment, error)`

**POST** `/v1/environments/{environment_id}`

Update an existing environment's configuration.

### Parameters

- `environmentID string`

- `params BetaEnvironmentUpdateParams`

  - `Config param.Field[BetaEnvironmentUpdateParamsConfigUnion] Optional`

    Body param: Updated environment configuration

    - `type BetaCloudConfigParamsResp struct{…}`

      Request params for `cloud` environment configuration.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `Type Cloud`

        Environment type

      - `Networking BetaCloudConfigParamsNetworkingUnionResp Optional`

        Network configuration policy. Omit on update to preserve the existing value.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

        - `type BetaLimitedNetworkParamsResp struct{…}`

          Limited network request params.

          Fields default to null; on update, omitted fields preserve the
          existing value.

          - `Type Limited`

            Network policy type

          - `AllowMCPServers bool Optional`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

          - `AllowPackageManagers bool Optional`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false` on creation. Must be `true` when `packages` are specified.

          - `AllowedHosts []string Optional`

            Specifies domains the container can reach.

      - `Packages BetaPackagesParamsResp Optional`

        Specify packages (and optionally their versions) available in this environment.

        When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

        Under `limited` networking, requires `networking.allow_package_managers` to be `true`.

        - `Apt []string Optional`

          Ubuntu/Debian packages to install

        - `Cargo []string Optional`

          Rust packages to install

        - `Gem []string Optional`

          Ruby packages to install

        - `Go []string Optional`

          Go packages to install

        - `Npm []string Optional`

          Node.js packages to install

        - `Pip []string Optional`

          Python packages to install

        - `Type BetaPackagesParamsType Optional`

          Package configuration type

          default: packages

    - `type BetaSelfHostedConfigParamsResp struct{…}`

      Request params for `self_hosted` environment configuration.

      - `Type SelfHosted`

        Environment type

  - `Description param.Field[string] Optional`

    Body param: Updated description of the environment. Omit to preserve; null clears to null; an empty string is stored as an empty string.

    maxLength: 1024

  - `Metadata param.Field[map[string, string]] Optional`

    Body param: User-provided metadata key-value pairs. Set a value to null or empty string to delete the key.

  - `Name param.Field[string] Optional`

    Body param: Updated name for the environment

    maxLength: 256, minLength: 1

  - `Scope param.Field[BetaEnvironmentUpdateParamsScope] Optional`

    Body param: The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only.

    - `const BetaEnvironmentUpdateParamsScopeOrganization BetaEnvironmentUpdateParamsScope = "organization"`

    - `const BetaEnvironmentUpdateParamsScopeAccount BetaEnvironmentUpdateParamsScope = "account"`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaEnvironmentConfigUnion`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `type BetaCloudConfig struct{…}`

      `cloud` environment configuration.

      - `Networking BetaCloudConfigNetworkingUnion`

        Network configuration policy.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

        - `type BetaLimitedNetwork struct{…}`

          Limited network access.

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

          - `Type Limited`

            Network policy type

      - `Packages BetaPackages`

        Package manager configuration.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesType Optional`

          Package configuration type

          default: packages

      - `Type Cloud`

        Environment type

    - `type BetaSelfHostedConfig struct{…}`

      Configuration for self-hosted environments.

      - `Type SelfHosted`

        Environment type

  - `CreatedAt string`

    RFC 3339 timestamp when environment was created

  - `Description string`

    User-provided description for the environment; null when unset

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs

  - `Name string`

    Human-readable name for the environment

  - `Type Environment`

    The type of object (always 'environment')

    default: environment

  - `UpdatedAt string`

    RFC 3339 timestamp when environment was last updated

  - `Scope BetaEnvironmentScope Optional`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"`

    - `const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaEnvironment, err := client.Beta.Environments.Update(
		context.TODO(),
		"env_011CZkZ9X2dpNyB7HsEFoRfW",
		anthropic.BetaEnvironmentUpdateParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaEnvironment.ID)
}
```

#### Response (200)

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Delete Environment

`client.Beta.Environments.Delete(ctx, environmentID, body) (*BetaEnvironmentDeleteResponse, error)`

**DELETE** `/v1/environments/{environment_id}`

Delete an environment by ID. Returns a confirmation of the deletion.

### Parameters

- `environmentID string`

- `body BetaEnvironmentDeleteParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

### Returns

- `type BetaEnvironmentDeleteResponse struct{…}`

  Response after deleting an environment.

  - `ID string`

    Environment identifier

  - `Type BetaEnvironmentDeleteResponseType`

    The type of response

    default: environment_deleted

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaEnvironmentDeleteResponse, err := client.Beta.Environments.Delete(
		context.TODO(),
		"env_011CZkZ9X2dpNyB7HsEFoRfW",
		anthropic.BetaEnvironmentDeleteParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaEnvironmentDeleteResponse.ID)
}
```

#### Response (200)

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "type": "environment_deleted"
}
```

## Archive Environment

`client.Beta.Environments.Archive(ctx, environmentID, body) (*BetaEnvironment, error)`

**POST** `/v1/environments/{environment_id}/archive`

Archive an environment by ID. Archived environments cannot be used to create new sessions.

### Parameters

- `environmentID string`

- `body BetaEnvironmentArchiveParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

### Returns

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaEnvironmentConfigUnion`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `type BetaCloudConfig struct{…}`

      `cloud` environment configuration.

      - `Networking BetaCloudConfigNetworkingUnion`

        Network configuration policy.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

        - `type BetaLimitedNetwork struct{…}`

          Limited network access.

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

          - `Type Limited`

            Network policy type

      - `Packages BetaPackages`

        Package manager configuration.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesType Optional`

          Package configuration type

          default: packages

      - `Type Cloud`

        Environment type

    - `type BetaSelfHostedConfig struct{…}`

      Configuration for self-hosted environments.

      - `Type SelfHosted`

        Environment type

  - `CreatedAt string`

    RFC 3339 timestamp when environment was created

  - `Description string`

    User-provided description for the environment; null when unset

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs

  - `Name string`

    Human-readable name for the environment

  - `Type Environment`

    The type of object (always 'environment')

    default: environment

  - `UpdatedAt string`

    RFC 3339 timestamp when environment was last updated

  - `Scope BetaEnvironmentScope Optional`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"`

    - `const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"`

### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaEnvironment, err := client.Beta.Environments.Archive(
		context.TODO(),
		"env_011CZkZ9X2dpNyB7HsEFoRfW",
		anthropic.BetaEnvironmentArchiveParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaEnvironment.ID)
}
```

#### Response (200)

```json
{
  "id": "env_011CZkZ9X2dpNyB7HsEFoRfW",
  "archived_at": null,
  "config": {
    "networking": {
      "allow_mcp_servers": false,
      "allow_package_managers": true,
      "allowed_hosts": [
        "api.example.com"
      ],
      "type": "limited"
    },
    "packages": {
      "apt": [
        "string"
      ],
      "cargo": [
        "string"
      ],
      "gem": [
        "string"
      ],
      "go": [
        "string"
      ],
      "npm": [
        "string"
      ],
      "pip": [
        "pandas",
        "numpy"
      ],
      "type": "packages"
    },
    "type": "cloud"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "description": "Python environment with data-analysis packages.",
  "metadata": {},
  "name": "python-data-analysis",
  "type": "environment",
  "updated_at": "2026-03-15T10:00:00Z",
  "scope": "organization"
}
```

## Domain types

### Beta Cloud Config

- `type BetaCloudConfig struct{…}`

  `cloud` environment configuration.

  - `Networking BetaCloudConfigNetworkingUnion`

    Network configuration policy.

    - `type BetaUnrestrictedNetwork struct{…}`

      Unrestricted network access.

      - `Type Unrestricted`

        Network policy type

    - `type BetaLimitedNetwork struct{…}`

      Limited network access.

      - `AllowMCPServers bool`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

      - `AllowPackageManagers bool`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

      - `AllowedHosts []string`

        Specifies domains the container can reach.

      - `Type Limited`

        Network policy type

  - `Packages BetaPackages`

    Package manager configuration.

    - `Apt []string`

      Ubuntu/Debian packages to install

    - `Cargo []string`

      Rust packages to install

    - `Gem []string`

      Ruby packages to install

    - `Go []string`

      Go packages to install

    - `Npm []string`

      Node.js packages to install

    - `Pip []string`

      Python packages to install

    - `Type BetaPackagesType Optional`

      Package configuration type

      default: packages

  - `Type Cloud`

    Environment type

### Beta Cloud Config Params

- `type BetaCloudConfigParamsResp struct{…}`

  Request params for `cloud` environment configuration.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `Type Cloud`

    Environment type

  - `Networking BetaCloudConfigParamsNetworkingUnionResp Optional`

    Network configuration policy. Omit on update to preserve the existing value.

    - `type BetaUnrestrictedNetwork struct{…}`

      Unrestricted network access.

      - `Type Unrestricted`

        Network policy type

    - `type BetaLimitedNetworkParamsResp struct{…}`

      Limited network request params.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `Type Limited`

        Network policy type

      - `AllowMCPServers bool Optional`

        Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

      - `AllowPackageManagers bool Optional`

        Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false` on creation. Must be `true` when `packages` are specified.

      - `AllowedHosts []string Optional`

        Specifies domains the container can reach.

  - `Packages BetaPackagesParamsResp Optional`

    Specify packages (and optionally their versions) available in this environment.

    When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

    Under `limited` networking, requires `networking.allow_package_managers` to be `true`.

    - `Apt []string Optional`

      Ubuntu/Debian packages to install

    - `Cargo []string Optional`

      Rust packages to install

    - `Gem []string Optional`

      Ruby packages to install

    - `Go []string Optional`

      Go packages to install

    - `Npm []string Optional`

      Node.js packages to install

    - `Pip []string Optional`

      Python packages to install

    - `Type BetaPackagesParamsType Optional`

      Package configuration type

      default: packages

### Beta Environment

- `type BetaEnvironment struct{…}`

  Unified Environment resource for both cloud and self-hosted environments.

  - `ID string`

    Environment identifier (e.g., 'env_...')

  - `ArchivedAt string`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `Config BetaEnvironmentConfigUnion`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `type BetaCloudConfig struct{…}`

      `cloud` environment configuration.

      - `Networking BetaCloudConfigNetworkingUnion`

        Network configuration policy.

        - `type BetaUnrestrictedNetwork struct{…}`

          Unrestricted network access.

          - `Type Unrestricted`

            Network policy type

        - `type BetaLimitedNetwork struct{…}`

          Limited network access.

          - `AllowMCPServers bool`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `AllowPackageManagers bool`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `AllowedHosts []string`

            Specifies domains the container can reach.

          - `Type Limited`

            Network policy type

      - `Packages BetaPackages`

        Package manager configuration.

        - `Apt []string`

          Ubuntu/Debian packages to install

        - `Cargo []string`

          Rust packages to install

        - `Gem []string`

          Ruby packages to install

        - `Go []string`

          Go packages to install

        - `Npm []string`

          Node.js packages to install

        - `Pip []string`

          Python packages to install

        - `Type BetaPackagesType Optional`

          Package configuration type

          default: packages

      - `Type Cloud`

        Environment type

    - `type BetaSelfHostedConfig struct{…}`

      Configuration for self-hosted environments.

      - `Type SelfHosted`

        Environment type

  - `CreatedAt string`

    RFC 3339 timestamp when environment was created

  - `Description string`

    User-provided description for the environment; null when unset

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs

  - `Name string`

    Human-readable name for the environment

  - `Type Environment`

    The type of object (always 'environment')

    default: environment

  - `UpdatedAt string`

    RFC 3339 timestamp when environment was last updated

  - `Scope BetaEnvironmentScope Optional`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `const BetaEnvironmentScopeOrganization BetaEnvironmentScope = "organization"`

    - `const BetaEnvironmentScopeAccount BetaEnvironmentScope = "account"`

### Beta Environment Delete Response

- `type BetaEnvironmentDeleteResponse struct{…}`

  Response after deleting an environment.

  - `ID string`

    Environment identifier

  - `Type BetaEnvironmentDeleteResponseType`

    The type of response

    default: environment_deleted

### Beta Limited Network

- `type BetaLimitedNetwork struct{…}`

  Limited network access.

  - `AllowMCPServers bool`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

  - `AllowPackageManagers bool`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

  - `AllowedHosts []string`

    Specifies domains the container can reach.

  - `Type Limited`

    Network policy type

### Beta Limited Network Params

- `type BetaLimitedNetworkParamsResp struct{…}`

  Limited network request params.

  Fields default to null; on update, omitted fields preserve the
  existing value.

  - `Type Limited`

    Network policy type

  - `AllowMCPServers bool Optional`

    Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

  - `AllowPackageManagers bool Optional`

    Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false` on creation. Must be `true` when `packages` are specified.

  - `AllowedHosts []string Optional`

    Specifies domains the container can reach.

### Beta Packages

- `type BetaPackages struct{…}`

  Packages (and their versions) available in this environment.

  - `Apt []string`

    Ubuntu/Debian packages to install

  - `Cargo []string`

    Rust packages to install

  - `Gem []string`

    Ruby packages to install

  - `Go []string`

    Go packages to install

  - `Npm []string`

    Node.js packages to install

  - `Pip []string`

    Python packages to install

  - `Type BetaPackagesType Optional`

    Package configuration type

    default: packages

### Beta Packages Params

- `type BetaPackagesParamsResp struct{…}`

  Specify packages (and optionally their versions) available in this environment.

  When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

  Under `limited` networking, requires `networking.allow_package_managers` to be `true`.

  - `Apt []string Optional`

    Ubuntu/Debian packages to install

  - `Cargo []string Optional`

    Rust packages to install

  - `Gem []string Optional`

    Ruby packages to install

  - `Go []string Optional`

    Go packages to install

  - `Npm []string Optional`

    Node.js packages to install

  - `Pip []string Optional`

    Python packages to install

  - `Type BetaPackagesParamsType Optional`

    Package configuration type

    default: packages

### Beta Self Hosted Config

- `type BetaSelfHostedConfig struct{…}`

  Configuration for self-hosted environments.

  - `Type SelfHosted`

    Environment type

### Beta Self Hosted Config Params

- `type BetaSelfHostedConfigParamsResp struct{…}`

  Request params for `self_hosted` environment configuration.

  - `Type SelfHosted`

    Environment type

### Beta Unrestricted Network

- `type BetaUnrestrictedNetwork struct{…}`

  Unrestricted network access.

  - `Type Unrestricted`

    Network policy type

## Environments › Work

### Get Work Item

`client.Beta.Environments.Work.Get(ctx, workID, params) (*BetaSelfHostedWork, error)`

**GET** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Retrieve detailed information about a specific work item.

#### Parameters

- `workID string`

- `params BetaEnvironmentWorkGetParams`

  - `EnvironmentID param.Field[string]`

    Path param

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `type BetaSelfHostedWork struct{…}`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `ID string`

    Work identifier (e.g., 'work_...')

  - `AcknowledgedAt string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `CreatedAt string`

    RFC 3339 timestamp when work was created

  - `Data BetaSessionWorkData`

    The actual work to be performed

    - `ID string`

      Session identifier (e.g., 'session_...')

    - `Type Session`

      Type of work data

  - `EnvironmentID string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `LatestHeartbeatAt string`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs associated with this work item

  - `Secret string`

    Credential payload used by the environment worker to execute this work item. May be populated when polling for work; null on all other retrieval paths.

  - `StartedAt string`

    RFC 3339 timestamp when work execution started

  - `State BetaSelfHostedWorkState`

    Current state of the work item

    - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

    - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

    - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

    - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

    - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

  - `StopRequestedAt string`

    RFC 3339 timestamp when stop was requested

  - `StoppedAt string`

    RFC 3339 timestamp when work execution stopped

  - `Type Work`

    The type of object (always 'work')

    default: work

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaSelfHostedWork, err := client.Beta.Environments.Work.Get(
		context.TODO(),
		"work_id",
		anthropic.BetaEnvironmentWorkGetParams{
			EnvironmentID: "env_011CZkZ9X2dpNyB7HsEFoRfW",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaSelfHostedWork.ID)
}
```

##### Response (200)

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "secret": "secret",
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

### Poll for Work

`client.Beta.Environments.Work.Poll(ctx, environmentID, params) (*BetaSelfHostedWork, error)`

**GET** `/v1/environments/{environment_id}/work/poll`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Long poll for work items in the queue.

#### Parameters

- `environmentID string`

- `params BetaEnvironmentWorkPollParams`

  - `BlockMs param.Field[int64] Optional`

    Query param: How long to wait for work to arrive before returning. Must be 1-999 in milliseconds. Defaults to non-blocking (returns immediately if no work is available).

    minimum: 1

  - `ReclaimOlderThanMs param.Field[int64] Optional`

    Query param: Reclaim unacknowledged work items older than this many milliseconds. If omitted, uses the default (5000ms).

    minimum: 1

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

  - `AnthropicWorkerID param.Field[string] Optional`

    Header param: Unique identifier for the specific worker polling, used to track aggregated environment-level work metrics in Console

#### Returns

- `type BetaSelfHostedWork struct{…}`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `ID string`

    Work identifier (e.g., 'work_...')

  - `AcknowledgedAt string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `CreatedAt string`

    RFC 3339 timestamp when work was created

  - `Data BetaSessionWorkData`

    The actual work to be performed

    - `ID string`

      Session identifier (e.g., 'session_...')

    - `Type Session`

      Type of work data

  - `EnvironmentID string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `LatestHeartbeatAt string`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs associated with this work item

  - `Secret string`

    Credential payload used by the environment worker to execute this work item. May be populated when polling for work; null on all other retrieval paths.

  - `StartedAt string`

    RFC 3339 timestamp when work execution started

  - `State BetaSelfHostedWorkState`

    Current state of the work item

    - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

    - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

    - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

    - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

    - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

  - `StopRequestedAt string`

    RFC 3339 timestamp when stop was requested

  - `StoppedAt string`

    RFC 3339 timestamp when work execution stopped

  - `Type Work`

    The type of object (always 'work')

    default: work

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaSelfHostedWork, err := client.Beta.Environments.Work.Poll(
		context.TODO(),
		"env_011CZkZ9X2dpNyB7HsEFoRfW",
		anthropic.BetaEnvironmentWorkPollParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaSelfHostedWork.ID)
}
```

##### Response (200)

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "secret": "secret",
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

### Acknowledge Work

`client.Beta.Environments.Work.Ack(ctx, workID, params) (*BetaSelfHostedWork, error)`

**POST** `/v1/environments/{environment_id}/work/{work_id}/ack`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Acknowledge receipt of a work item, transitioning it from 'queued' to 'starting' and removing it from the queue.

#### Parameters

- `workID string`

- `params BetaEnvironmentWorkAckParams`

  - `EnvironmentID param.Field[string]`

    Path param

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `type BetaSelfHostedWork struct{…}`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `ID string`

    Work identifier (e.g., 'work_...')

  - `AcknowledgedAt string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `CreatedAt string`

    RFC 3339 timestamp when work was created

  - `Data BetaSessionWorkData`

    The actual work to be performed

    - `ID string`

      Session identifier (e.g., 'session_...')

    - `Type Session`

      Type of work data

  - `EnvironmentID string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `LatestHeartbeatAt string`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs associated with this work item

  - `Secret string`

    Credential payload used by the environment worker to execute this work item. May be populated when polling for work; null on all other retrieval paths.

  - `StartedAt string`

    RFC 3339 timestamp when work execution started

  - `State BetaSelfHostedWorkState`

    Current state of the work item

    - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

    - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

    - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

    - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

    - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

  - `StopRequestedAt string`

    RFC 3339 timestamp when stop was requested

  - `StoppedAt string`

    RFC 3339 timestamp when work execution stopped

  - `Type Work`

    The type of object (always 'work')

    default: work

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaSelfHostedWork, err := client.Beta.Environments.Work.Ack(
		context.TODO(),
		"work_id",
		anthropic.BetaEnvironmentWorkAckParams{
			EnvironmentID: "env_011CZkZ9X2dpNyB7HsEFoRfW",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaSelfHostedWork.ID)
}
```

##### Response (200)

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "secret": "secret",
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

### Record Heartbeat

`client.Beta.Environments.Work.Heartbeat(ctx, workID, params) (*BetaSelfHostedWorkHeartbeatResponse, error)`

**POST** `/v1/environments/{environment_id}/work/{work_id}/heartbeat`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Record a heartbeat for a work item to maintain the lease.

#### Parameters

- `workID string`

- `params BetaEnvironmentWorkHeartbeatParams`

  - `EnvironmentID param.Field[string]`

    Path param

  - `DesiredTTLSeconds param.Field[int64] Optional`

    Query param: Desired TTL in seconds

  - `ExpectedLastHeartbeat param.Field[string] Optional`

    Query param: Expected last_heartbeat for conditional update (optimistic concurrency). Use literal 'NO_HEARTBEAT' to claim an unclaimed lease (first heartbeat). For subsequent heartbeats, echo the server's previous last_heartbeat value exactly. Returns 412 Precondition Failed if the actual value doesn't match.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `type BetaSelfHostedWorkHeartbeatResponse struct{…}`

  Response after recording a heartbeat for a work item.

  - `LastHeartbeat string`

    RFC 3339 timestamp of the actual heartbeat from DB

  - `LeaseExtended bool`

    Whether the heartbeat succeeded in extending the lease

  - `State BetaSelfHostedWorkHeartbeatResponseState`

    Current state of the work item (active/stopping/stopped)

    - `const BetaSelfHostedWorkHeartbeatResponseStateQueued BetaSelfHostedWorkHeartbeatResponseState = "queued"`

    - `const BetaSelfHostedWorkHeartbeatResponseStateStarting BetaSelfHostedWorkHeartbeatResponseState = "starting"`

    - `const BetaSelfHostedWorkHeartbeatResponseStateActive BetaSelfHostedWorkHeartbeatResponseState = "active"`

    - `const BetaSelfHostedWorkHeartbeatResponseStateStopping BetaSelfHostedWorkHeartbeatResponseState = "stopping"`

    - `const BetaSelfHostedWorkHeartbeatResponseStateStopped BetaSelfHostedWorkHeartbeatResponseState = "stopped"`

  - `TTLSeconds int64`

    Effective TTL applied to the lease

  - `Type WorkHeartbeat`

    The type of response

    default: work_heartbeat

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaSelfHostedWorkHeartbeatResponse, err := client.Beta.Environments.Work.Heartbeat(
		context.TODO(),
		"work_id",
		anthropic.BetaEnvironmentWorkHeartbeatParams{
			EnvironmentID: "env_011CZkZ9X2dpNyB7HsEFoRfW",
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaSelfHostedWorkHeartbeatResponse.LastHeartbeat)
}
```

##### Response (200)

```json
{
  "last_heartbeat": "last_heartbeat",
  "lease_extended": true,
  "state": "queued",
  "ttl_seconds": 0,
  "type": "work_heartbeat"
}
```

### Stop Work

`client.Beta.Environments.Work.Stop(ctx, workID, params) (*BetaSelfHostedWork, error)`

**POST** `/v1/environments/{environment_id}/work/{work_id}/stop`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Stop a work item, initiating graceful or forced shutdown.

#### Parameters

- `workID string`

- `params BetaEnvironmentWorkStopParams`

  - `EnvironmentID param.Field[string]`

    Path param

  - `BetaSelfHostedWorkStopRequest param.Field[BetaSelfHostedWorkStopRequest]`

    Body param: Request to stop a work item.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `type BetaSelfHostedWork struct{…}`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `ID string`

    Work identifier (e.g., 'work_...')

  - `AcknowledgedAt string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `CreatedAt string`

    RFC 3339 timestamp when work was created

  - `Data BetaSessionWorkData`

    The actual work to be performed

    - `ID string`

      Session identifier (e.g., 'session_...')

    - `Type Session`

      Type of work data

  - `EnvironmentID string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `LatestHeartbeatAt string`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs associated with this work item

  - `Secret string`

    Credential payload used by the environment worker to execute this work item. May be populated when polling for work; null on all other retrieval paths.

  - `StartedAt string`

    RFC 3339 timestamp when work execution started

  - `State BetaSelfHostedWorkState`

    Current state of the work item

    - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

    - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

    - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

    - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

    - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

  - `StopRequestedAt string`

    RFC 3339 timestamp when stop was requested

  - `StoppedAt string`

    RFC 3339 timestamp when work execution stopped

  - `Type Work`

    The type of object (always 'work')

    default: work

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaSelfHostedWork, err := client.Beta.Environments.Work.Stop(
		context.TODO(),
		"work_id",
		anthropic.BetaEnvironmentWorkStopParams{
			EnvironmentID:                 "env_011CZkZ9X2dpNyB7HsEFoRfW",
			BetaSelfHostedWorkStopRequest: anthropic.BetaSelfHostedWorkStopRequestParam{},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaSelfHostedWork.ID)
}
```

##### Response (200)

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "secret": "secret",
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

### List Work Items

`client.Beta.Environments.Work.List(ctx, environmentID, params) (*PageCursor[BetaSelfHostedWork], error)`

**GET** `/v1/environments/{environment_id}/work`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

List work items in an environment.

#### Parameters

- `environmentID string`

- `params BetaEnvironmentWorkListParams`

  - `Limit param.Field[int64] Optional`

    Query param: Maximum number of work items to return

    maximum: 1000, minimum: 1

  - `Page param.Field[string] Optional`

    Query param: Opaque cursor from previous response for pagination

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `type BetaSelfHostedWork struct{…}`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `ID string`

    Work identifier (e.g., 'work_...')

  - `AcknowledgedAt string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `CreatedAt string`

    RFC 3339 timestamp when work was created

  - `Data BetaSessionWorkData`

    The actual work to be performed

    - `ID string`

      Session identifier (e.g., 'session_...')

    - `Type Session`

      Type of work data

  - `EnvironmentID string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `LatestHeartbeatAt string`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs associated with this work item

  - `Secret string`

    Credential payload used by the environment worker to execute this work item. May be populated when polling for work; null on all other retrieval paths.

  - `StartedAt string`

    RFC 3339 timestamp when work execution started

  - `State BetaSelfHostedWorkState`

    Current state of the work item

    - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

    - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

    - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

    - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

    - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

  - `StopRequestedAt string`

    RFC 3339 timestamp when stop was requested

  - `StoppedAt string`

    RFC 3339 timestamp when work execution stopped

  - `Type Work`

    The type of object (always 'work')

    default: work

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	page, err := client.Beta.Environments.Work.List(
		context.TODO(),
		"env_011CZkZ9X2dpNyB7HsEFoRfW",
		anthropic.BetaEnvironmentWorkListParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", page)
}
```

##### Response (200)

```json
{
  "data": [
    {
      "id": "id",
      "acknowledged_at": "acknowledged_at",
      "created_at": "created_at",
      "data": {
        "id": "id",
        "type": "session"
      },
      "environment_id": "environment_id",
      "latest_heartbeat_at": "latest_heartbeat_at",
      "metadata": {
        "foo": "string"
      },
      "secret": "secret",
      "started_at": "started_at",
      "state": "queued",
      "stop_requested_at": "stop_requested_at",
      "stopped_at": "stopped_at",
      "type": "work"
    }
  ],
  "next_page": "next_page"
}
```

### Update Work Item

`client.Beta.Environments.Work.Update(ctx, workID, params) (*BetaSelfHostedWork, error)`

**POST** `/v1/environments/{environment_id}/work/{work_id}`

Note: these endpoints are called automatically by the pre-built environment worker provided in the SDKs and CLI, for orchestrating sessions with self-hosted sandbox environments. They are included here as a reference; you do not need to invoke them directly.

Update work item metadata with merge semantics.

#### Parameters

- `workID string`

- `params BetaEnvironmentWorkUpdateParams`

  - `EnvironmentID param.Field[string]`

    Path param

  - `BetaSelfHostedWorkUpdateRequest param.Field[BetaSelfHostedWorkUpdateRequest]`

    Body param: Request to update work item metadata.

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `type BetaSelfHostedWork struct{…}`

  Work resource representing a unit of work in a self-hosted environment.

  Work items are queued when sessions are created or when long-dormant sessions
  receive new messages. The environment worker polls for work to execute in a
  self-hosted sandbox.

  - `ID string`

    Work identifier (e.g., 'work_...')

  - `AcknowledgedAt string`

    RFC 3339 timestamp when the work item was acknowledged and assigned to a self-hosted sandbox

  - `CreatedAt string`

    RFC 3339 timestamp when work was created

  - `Data BetaSessionWorkData`

    The actual work to be performed

    - `ID string`

      Session identifier (e.g., 'session_...')

    - `Type Session`

      Type of work data

  - `EnvironmentID string`

    Environment identifier this work belongs to (e.g., `env_...`)

  - `LatestHeartbeatAt string`

    RFC 3339 timestamp of the most recent heartbeat

  - `Metadata map[string, string]`

    User-provided metadata key-value pairs associated with this work item

  - `Secret string`

    Credential payload used by the environment worker to execute this work item. May be populated when polling for work; null on all other retrieval paths.

  - `StartedAt string`

    RFC 3339 timestamp when work execution started

  - `State BetaSelfHostedWorkState`

    Current state of the work item

    - `const BetaSelfHostedWorkStateQueued BetaSelfHostedWorkState = "queued"`

    - `const BetaSelfHostedWorkStateStarting BetaSelfHostedWorkState = "starting"`

    - `const BetaSelfHostedWorkStateActive BetaSelfHostedWorkState = "active"`

    - `const BetaSelfHostedWorkStateStopping BetaSelfHostedWorkState = "stopping"`

    - `const BetaSelfHostedWorkStateStopped BetaSelfHostedWorkState = "stopped"`

  - `StopRequestedAt string`

    RFC 3339 timestamp when stop was requested

  - `StoppedAt string`

    RFC 3339 timestamp when work execution stopped

  - `Type Work`

    The type of object (always 'work')

    default: work

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaSelfHostedWork, err := client.Beta.Environments.Work.Update(
		context.TODO(),
		"work_id",
		anthropic.BetaEnvironmentWorkUpdateParams{
			EnvironmentID: "env_011CZkZ9X2dpNyB7HsEFoRfW",
			BetaSelfHostedWorkUpdateRequest: anthropic.BetaSelfHostedWorkUpdateRequestParam{
				Metadata: map[string]string{
					"foo": "string",
				},
			},
		},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaSelfHostedWork.ID)
}
```

##### Response (200)

```json
{
  "id": "id",
  "acknowledged_at": "acknowledged_at",
  "created_at": "created_at",
  "data": {
    "id": "id",
    "type": "session"
  },
  "environment_id": "environment_id",
  "latest_heartbeat_at": "latest_heartbeat_at",
  "metadata": {
    "foo": "string"
  },
  "secret": "secret",
  "started_at": "started_at",
  "state": "queued",
  "stop_requested_at": "stop_requested_at",
  "stopped_at": "stopped_at",
  "type": "work"
}
```

### Get Queue Statistics

`client.Beta.Environments.Work.Stats(ctx, environmentID, query) (*BetaSelfHostedWorkQueueStats, error)`

**GET** `/v1/environments/{environment_id}/work/stats`

Get statistics about the work queue for an environment.

#### Parameters

- `environmentID string`

- `query BetaEnvironmentWorkStatsParams`

  - `Betas param.Field[[]AnthropicBeta] Optional`

    Optional header to specify the beta version(s) you want to use.

    - `string`

    - `type AnthropicBeta string`

      - `const AnthropicBetaMessageBatches2024_09_24 AnthropicBeta = "message-batches-2024-09-24"`

      - `const AnthropicBetaPromptCaching2024_07_31 AnthropicBeta = "prompt-caching-2024-07-31"`

      - `const AnthropicBetaComputerUse2024_10_22 AnthropicBeta = "computer-use-2024-10-22"`

      - `const AnthropicBetaComputerUse2025_01_24 AnthropicBeta = "computer-use-2025-01-24"`

      - `const AnthropicBetaPDFs2024_09_25 AnthropicBeta = "pdfs-2024-09-25"`

      - `const AnthropicBetaTokenCounting2024_11_01 AnthropicBeta = "token-counting-2024-11-01"`

      - `const AnthropicBetaTokenEfficientTools2025_02_19 AnthropicBeta = "token-efficient-tools-2025-02-19"`

      - `const AnthropicBetaOutput128k2025_02_19 AnthropicBeta = "output-128k-2025-02-19"`

      - `const AnthropicBetaFilesAPI2025_04_14 AnthropicBeta = "files-api-2025-04-14"`

      - `const AnthropicBetaMCPClient2025_04_04 AnthropicBeta = "mcp-client-2025-04-04"`

      - `const AnthropicBetaMCPClient2025_11_20 AnthropicBeta = "mcp-client-2025-11-20"`

      - `const AnthropicBetaDevFullThinking2025_05_14 AnthropicBeta = "dev-full-thinking-2025-05-14"`

      - `const AnthropicBetaInterleavedThinking2025_05_14 AnthropicBeta = "interleaved-thinking-2025-05-14"`

      - `const AnthropicBetaCodeExecution2025_05_22 AnthropicBeta = "code-execution-2025-05-22"`

      - `const AnthropicBetaExtendedCacheTTL2025_04_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"`

      - `const AnthropicBetaContext1m2025_08_07 AnthropicBeta = "context-1m-2025-08-07"`

      - `const AnthropicBetaContextManagement2025_06_27 AnthropicBeta = "context-management-2025-06-27"`

      - `const AnthropicBetaModelContextWindowExceeded2025_08_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"`

      - `const AnthropicBetaSkills2025_10_02 AnthropicBeta = "skills-2025-10-02"`

      - `const AnthropicBetaFastMode2026_02_01 AnthropicBeta = "fast-mode-2026-02-01"`

      - `const AnthropicBetaOutput300k2026_03_24 AnthropicBeta = "output-300k-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_03_24 AnthropicBeta = "user-profiles-2026-03-24"`

      - `const AnthropicBetaUserProfiles2026_08_18 AnthropicBeta = "user-profiles-2026-08-18"`

      - `const AnthropicBetaAdvisorTool2026_03_01 AnthropicBeta = "advisor-tool-2026-03-01"`

      - `const AnthropicBetaManagedAgents2026_04_01 AnthropicBeta = "managed-agents-2026-04-01"`

      - `const AnthropicBetaCacheDiagnosis2026_04_07 AnthropicBeta = "cache-diagnosis-2026-04-07"`

      - `const AnthropicBetaDreaming2026_04_21 AnthropicBeta = "dreaming-2026-04-21"`

      - `const AnthropicBetaThinkingTokenCount2026_05_13 AnthropicBeta = "thinking-token-count-2026-05-13"`

      - `const AnthropicBetaServerSideFallback2026_06_01 AnthropicBeta = "server-side-fallback-2026-06-01"`

      - `const AnthropicBetaServerSideFallback2026_07_01 AnthropicBeta = "server-side-fallback-2026-07-01"`

      - `const AnthropicBetaFallbackCredit2026_06_01 AnthropicBeta = "fallback-credit-2026-06-01"`

      - `const AnthropicBetaFallbackCredit2026_07_01 AnthropicBeta = "fallback-credit-2026-07-01"`

      - `const AnthropicBetaAgentMemory2026_07_22 AnthropicBeta = "agent-memory-2026-07-22"`

      - `const AnthropicBetaMidConversationToolChanges2026_07_01 AnthropicBeta = "mid-conversation-tool-changes-2026-07-01"`

      - `const AnthropicBetaCompact2026_01_12 AnthropicBeta = "compact-2026-01-12"`

      - `const AnthropicBetaComputerUse2025_11_24 AnthropicBeta = "computer-use-2025-11-24"`

      - `const AnthropicBetaMCPTunnels2026_06_22 AnthropicBeta = "mcp-tunnels-2026-06-22"`

      - `const AnthropicBetaStructuredOutputs2025_11_13 AnthropicBeta = "structured-outputs-2025-11-13"`

      - `const AnthropicBetaTaskBudgets2026_03_13 AnthropicBeta = "task-budgets-2026-03-13"`

      - `const AnthropicBetaThinkingDisplayUpdates2026_08_18 AnthropicBeta = "thinking-display-updates-2026-08-18"`

      - `const AnthropicBetaCEUserManagement2026_07_13 AnthropicBeta = "ce-user-management-2026-07-13"`

      - `const AnthropicBetaMidConversationOutputConfig2026_07_01 AnthropicBeta = "mid-conversation-output-config-2026-07-01"`

      - `const AnthropicBetaThinkingBindingControls2026_08_01 AnthropicBeta = "thinking-binding-controls-2026-08-01"`

      - `const AnthropicBetaMidConversationSystemClearAt2026_08_21 AnthropicBeta = "mid-conversation-system-clear-at-2026-08-21"`

#### Returns

- `type BetaSelfHostedWorkQueueStats struct{…}`

  Statistics about the work queue for an environment.

  Uses Redis Stream consumer group metrics for O(1) queries.

  - `Depth int64`

    Number of work items waiting to be picked up (lag from consumer group)

  - `OldestQueuedAt string`

    RFC 3339 timestamp of oldest item in the work stream (includes both queued and pending items), null if stream empty

  - `Pending int64`

    Number of work items being processed (polled but not acknowledged)

    default: 0

  - `Type WorkQueueStats`

    The type of object

    default: work_queue_stats

  - `WorkersPolling int64`

    Number of workers that have polled for work in the last 30 seconds. Requires worker_id to be sent with poll requests.

#### Example

```go
package main

import (
	"context"
	"fmt"

	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("my-anthropic-api-key"),
	)
	betaSelfHostedWorkQueueStats, err := client.Beta.Environments.Work.Stats(
		context.TODO(),
		"env_011CZkZ9X2dpNyB7HsEFoRfW",
		anthropic.BetaEnvironmentWorkStatsParams{},
	)
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", betaSelfHostedWorkQueueStats.Depth)
}
```

##### Response (200)

```json
{
  "depth": 0,
  "oldest_queued_at": "oldest_queued_at",
  "pending": 0,
  "type": "work_queue_stats",
  "workers_polling": 0
}
```
