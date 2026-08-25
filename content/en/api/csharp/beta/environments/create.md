# Create Environment

`BetaEnvironment Beta.Environments.Create(parameters, cancellationToken = default)`

**POST** `/v1/environments`

Create a new environment with the specified configuration.

## Parameters

- `EnvironmentCreateParams parameters`

  - `required string name`

    Body param: Human-readable name for the environment

    maxLength: 256, minLength: 1

  - `Config? config`

    Body param: Environment configuration

    - `class BetaCloudConfigParams:`

      Request params for `cloud` environment configuration.

      Fields default to null; on update, omitted fields preserve the
      existing value.

      - `JsonElement Type constant`

        Environment type

      - `Networking? Networking`

        Network configuration policy. Omit on update to preserve the existing value.

        - `class BetaUnrestrictedNetwork:`

          Unrestricted network access.

          - `JsonElement Type constant`

            Network policy type

        - `class BetaLimitedNetworkParams:`

          Limited network request params.

          Fields default to null; on update, omitted fields preserve the
          existing value.

          - `JsonElement Type constant`

            Network policy type

          - `bool? AllowMcpServers`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

          - `bool? AllowPackageManagers`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

          - `IReadOnlyList<string>? AllowedHosts`

            Specifies domains the container can reach.

      - `BetaPackagesParams? Packages`

        Specify packages (and optionally their versions) available in this environment.

        When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

        - `IReadOnlyList<string>? Apt`

          Ubuntu/Debian packages to install

        - `IReadOnlyList<string>? Cargo`

          Rust packages to install

        - `IReadOnlyList<string>? Gem`

          Ruby packages to install

        - `IReadOnlyList<string>? Go`

          Go packages to install

        - `IReadOnlyList<string>? Npm`

          Node.js packages to install

        - `IReadOnlyList<string>? Pip`

          Python packages to install

        - `Type Type`

          Package configuration type

    - `class BetaSelfHostedConfigParams:`

      Request params for `self_hosted` environment configuration.

      - `JsonElement Type constant`

        Environment type

  - `string? description`

    Body param: Optional description of the environment

    maxLength: 1024

  - `IReadOnlyDictionary<string, string> metadata`

    Body param: User-provided metadata key-value pairs

  - `Scope? scope`

    Body param: The visibility scope for this environment. 'organization' makes the environment visible to all accounts. 'account' restricts visibility to the owning account only. Only applicable for self-hosted environments. If not specified, defaults based on organization type.

    - `Organization`

    - `Account`

  - `IReadOnlyList<AnthropicBeta> betas`

    Header param: Optional header to specify the beta version(s) you want to use.

    - `MessageBatches2024_09_24`

    - `PromptCaching2024_07_31`

    - `ComputerUse2024_10_22`

    - `ComputerUse2025_01_24`

    - `Pdfs2024_09_25`

    - `TokenCounting2024_11_01`

    - `TokenEfficientTools2025_02_19`

    - `Output128k2025_02_19`

    - `FilesApi2025_04_14`

    - `McpClient2025_04_04`

    - `McpClient2025_11_20`

    - `DevFullThinking2025_05_14`

    - `InterleavedThinking2025_05_14`

    - `CodeExecution2025_05_22`

    - `ExtendedCacheTtl2025_04_11`

    - `Context1m2025_08_07`

    - `ContextManagement2025_06_27`

    - `ModelContextWindowExceeded2025_08_26`

    - `Skills2025_10_02`

    - `FastMode2026_02_01`

    - `Output300k2026_03_24`

    - `UserProfiles2026_03_24`

    - `UserProfiles2026_08_18`

    - `AdvisorTool2026_03_01`

    - `ManagedAgents2026_04_01`

    - `CacheDiagnosis2026_04_07`

    - `Dreaming2026_04_21`

    - `ThinkingTokenCount2026_05_13`

    - `ServerSideFallback2026_06_01`

    - `ServerSideFallback2026_07_01`

    - `FallbackCredit2026_06_01`

    - `FallbackCredit2026_07_01`

    - `AgentMemory2026_07_22`

    - `MidConversationToolChanges2026_07_01`

## Returns

- `class BetaEnvironment:`

  Unified Environment resource for both cloud and self-hosted environments.

  - `required string ID`

    Environment identifier (e.g., 'env_...')

  - `required string? ArchivedAt`

    RFC 3339 timestamp when environment was archived, or null if not archived

  - `required Config Config`

    Environment configuration (either Anthropic Cloud or self-hosted)

    - `class BetaCloudConfig:`

      `cloud` environment configuration.

      - `required Networking Networking`

        Network configuration policy.

        - `class BetaUnrestrictedNetwork:`

          Unrestricted network access.

          - `JsonElement Type constant`

            Network policy type

        - `class BetaLimitedNetwork:`

          Limited network access.

          - `required bool AllowMcpServers`

            Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

          - `required bool AllowPackageManagers`

            Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

          - `required IReadOnlyList<string> AllowedHosts`

            Specifies domains the container can reach.

          - `JsonElement Type constant`

            Network policy type

      - `required BetaPackages Packages`

        Package manager configuration.

        - `required IReadOnlyList<string> Apt`

          Ubuntu/Debian packages to install

        - `required IReadOnlyList<string> Cargo`

          Rust packages to install

        - `required IReadOnlyList<string> Gem`

          Ruby packages to install

        - `required IReadOnlyList<string> Go`

          Go packages to install

        - `required IReadOnlyList<string> Npm`

          Node.js packages to install

        - `required IReadOnlyList<string> Pip`

          Python packages to install

        - `Type Type`

          Package configuration type

      - `JsonElement Type constant`

        Environment type

    - `class BetaSelfHostedConfig:`

      Configuration for self-hosted environments.

      - `JsonElement Type constant`

        Environment type

  - `required string CreatedAt`

    RFC 3339 timestamp when environment was created

  - `required string? Description`

    User-provided description for the environment; null when unset

  - `required IReadOnlyDictionary<string, string> Metadata`

    User-provided metadata key-value pairs

  - `required string Name`

    Human-readable name for the environment

  - `JsonElement Type constant`

    The type of object (always 'environment')

  - `required string UpdatedAt`

    RFC 3339 timestamp when environment was last updated

  - `Scope Scope`

    The visibility scope for this environment. 'organization' means visible to all accounts. 'account' means visible only to the owning account.

    - `Organization`

    - `Account`

## Example

```csharp
EnvironmentCreateParams parameters = new() { Name = "python-data-analysis" };

var betaEnvironment = await client.Beta.Environments.Create(parameters);

Console.WriteLine(betaEnvironment);
```

### Response (200)

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
