# Getting Started with Local MCP Servers on Claude Desktop

The Model Context Protocol (MCP) is an open protocol that enables seamless integration between LLM applications and external data sources and tools. With the introduction of desktop extensions, installing and managing local MCP servers has become significantly easier.

## Desktop Extensions

Desktop extensions provide a streamlined way to install and manage local MCP servers through single-click installable packages. Instead of manually configuring JSON files and managing dependencies, you can now install local MCP servers on your computer as easily as browser extensions.

**Note:** We’re building a directory of desktop extensions – if you’re a developer hoping to add an extension you built to the directory, complete our [desktop extensions interest form](https://docs.google.com/forms/d/14_Dmcig4z8NeRMB_e7TOyrKzuZ88-BLYdLvS6LPhiZU/viewform?edit_requested=true) to share more information with us.

## Installing desktop extensions from the directory

1. Navigate to Settings > Extensions on Claude Desktop.

2. Click “Browse extensions” to view our directory and click on any Anthropic-reviewed tools you want to use. Click "Install" on your desired extension.

3. Configure any required settings (like API keys) through the user-friendly interface.

4. The extension will automatically be available in your conversations.

## Installing custom desktop extensions

1. Navigate to Settings > Extensions on Claude Desktop.

2. Click “Advanced settings” and find the **Extension Developer** section.

3. Click “Install Extension…”

4. Select the .mcpb file and follow the prompts to install.

## Admin Controls for Desktop Extensions

Owners and Primary Owners of Team and Enterprise plans can manage team access to desktop extensions using two controls:

1. Enable or disable public desktop extensions depending on your organization’s security standards.

2. Upload custom desktop extensions and make them available to your team for one-click install.

These controls allow organizations to fully customize their registries by adding only the extensions the team needs to access, and removing any others.

### Enabling/disabling specific extensions on Team and Enterprise plans

Owners and Primary Owners of Team and Enterprise organizations can manage which desktop extensions are enabled for your organization and accessible to other members via Claude Desktop. See [Enabling and using the desktop extension allowlist](https://support.claude.com/en/articles/12592343-enabling-and-using-the-desktop-extension-allowlist)

for specific instructions.

### Create and upload custom extensions for your organization

Custom desktop extensions uploads allow Team and Enterprise plans to leverage organization-specific workflows that aren’t available in the public directory. After creating a custom desktop extension, Owners and Primary Owners can navigate to Settings > Extensions within Claude Desktop and click “Advanced settings” to access the **Extension Developer** section:

![](https://downloads.intercomcdn.com/i/o/lupk8zyo/1681607607/ba6e379d2769d190f0970a0adaed/AD_4nXd4aZkqjJFpiXMPF28Pih7HmSJ9pPsnoWAfVgiLdFRFiTkO92YtXteIjvDHaPl7T0tjfpRTBOlyrMbQ_aciCNDgfIuEvV3szmKvt72x5O51DMSClXOYWk1JIRIzylwkj3joXqZcLw?expires=1784394900&amp;signature=004aebaa396bce1e73c475d226ac7bd00a2a35814b575b48b69ec8ccbc9206b2&amp;req=dSYvF89%2BmodfXvMW1HO4zWbPxER8Pjk7Hn9K2IaIG2IoN%2F67XEZrpaM4J2m0%0AUYs4061ST2zjls07BUk%3D%0A)

Click “Install Extension…” and select the .mcpb file. Follow the prompts to install and configure your custom desktop extension. For more in-depth information, please refer to our [desktop extension developer documentation](https://github.com/anthropics/mcpb).

## Enterprise Policy Controls

**Note:** Enterprise policy controls at the user-machine level will override any in-app controls (blocklist and allowlist). If you want to use an in-app control, ensure `isDesktopExtensionEnabled` and `isDesktopExtensionDirectoryEnabled` are not set to "false" so the allowlist can populate the available registry.

For controlling desktop extensions through system policies, please refer to our [desktop enterprise configuration documentation](https://support.claude.com/en/articles/12622667-enterprise-configuration).

## Troubleshooting desktop extension installation issues

### Extension won't install

- Ensure you're running the latest version of Claude Desktop.

- Check that the extension file isn't corrupted by re-downloading it.

- Verify you have sufficient disk space for the installation.

### Extension appears installed but tools aren't available

- Restart Claude Desktop to refresh the extension registry.

- Check the extension's configuration settings for missing required fields.

- Verify any API keys or authentication credentials are entered correctly.

### Extension configuration issues

- Navigate to Settings > Extensions and click on the extension to review its settings.

- Ensure all required configuration fields are completed.

- Check that file paths (if applicable) point to existing directories you have access to.

### Permission or security errors

- On macOS, check System Preferences > Security & Privacy if you receive security warnings.

- On Windows and Linux, ensure Claude Desktop has necessary permissions to access required directories.

- For enterprise environments, verify that desktop extensions are enabled through your organization's policies.

## Developer FAQ

### How do I check if my MCP servers are properly connected in Claude Desktop?

Click the "+" button on bottom the chat box within Claude Desktop, then select "Connectors." This will show you connected MCP servers and their tools. Alternatively, you can visit Developer settings (under **Desktop app**) to see connection status and look at the logs for any MCP servers.

### How do I convert my existing MCP server to a desktop extension?

1. Add a manifest.json file to your MCP server directory with the required metadata.

2. Package it using the `mcpb pack` command.

3. See the [MCPB documentation](https://github.com/anthropics/mcpb) for detailed instructions.

### What programming languages are supported for desktop extensions?

Desktop extensions support Node.js, Python, and binary MCP servers. Claude Desktop includes a built-in Node.js environment, so Node.js installation isn't required.

### How do I handle sensitive configuration like API keys?

Mark configuration fields as "sensitive": true in your manifest.json. Claude Desktop will automatically encrypt these values using the operating system's secure storage (Keychain on macOS, Credential Manager on Windows, and your distro’s keychain manager on Linux).

### Can I distribute my custom desktop extension privately?

Yes, you can share .mcpb files directly with specific users or teams. For broader distribution, you can submit extensions to the official directory.

### How do I debug issues with my desktop extension?

Enable debug logging in Claude Desktop settings, check the extension logs in the Extensions settings panel, and refer to the MCP debugging guide for protocol-specific troubleshooting.

### What happens when my extension needs updates?

Extensions from the official directory update automatically by default. For privately distributed extensions, users will need to install updated .mcpb files manually.

## Interested in learning more about MCP?

For more in-depth information on building your own MCP clients and servers, we recommend reviewing the following resources:

- [MCP Quickstart Guide](https://modelcontextprotocol.io/docs/getting-started/intro) - A step-by-step tutorial perfect for getting started with basic MCP integration.

- [Model Context Protocol Github](https://github.com/modelcontextprotocol) - Contains the complete technical documentation, code examples, and implementation guides.

- [Guide to debugging MCP integrations](https://modelcontextprotocol.io/docs/tools/debugging) - Troubleshooting tips and solutions for common implementation challenges.

If you need further guidance, visit our guide on [How to Get Support](https://support.claude.com/en/articles/9015913-how-to-get-support) for additional support options.