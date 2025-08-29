#!/usr/bin/env node

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ErrorCode,
  ListToolsRequestSchema,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema,
  ListPromptsRequestSchema,
  GetPromptRequestSchema,
  McpError,
} from '@modelcontextprotocol/sdk/types.js';
import { searchTool } from './tools/search.js';
import { getDocumentationResources, readDocumentationResource, ensureDocsInstalled } from './resources/index.js';
import { prompts, getPrompt } from './prompts/index.js';

export const VERSION = "1.0.0";

class ClaudeCodeDocsServer {
  private server: Server;

  constructor() {
    this.server = new Server(
      {
        name: 'claude-code-docs-mcp-server',
        version: VERSION,
      },
      {
        capabilities: {
          tools: {},
          resources: {},
          prompts: {},
        },
      }
    );

    this.setupToolHandlers();
    this.setupResourceHandlers();
    this.setupPromptHandlers();
    this.setupErrorHandling();
    this.ensureDocsAvailable();
  }

  private setupErrorHandling(): void {
    this.server.onerror = (error) => console.error('[MCP Error]', error);
    process.on('SIGINT', async () => {
      await this.server.close();
      process.exit(0);
    });
  }

  private setupToolHandlers(): void {
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [{
        name: searchTool.name,
        description: searchTool.description,
        inputSchema: searchTool.inputSchema,
      }],
    }));

    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;
      
      if (name !== searchTool.name) {
        throw new McpError(ErrorCode.MethodNotFound, `Tool ${name} not found`);
      }

      try {
        const result = await searchTool.handler(args || {});
        return {
          content: [
            {
              type: 'text',
              text: typeof result === 'string' ? result : JSON.stringify(result, null, 2),
            },
          ],
        };
      } catch (error) {
        throw new McpError(
          ErrorCode.InternalError,
          `Tool ${name} failed: ${error instanceof Error ? error.message : 'Unknown error'}`
        );
      }
    });
  }

  private setupResourceHandlers(): void {
    this.server.setRequestHandler(ListResourcesRequestSchema, async () => {
      const resources = await getDocumentationResources();
      return { resources };
    });

    this.server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
      const { uri } = request.params;
      try {
        const content = await readDocumentationResource(uri);
        return {
          contents: [
            {
              uri,
              mimeType: 'text/markdown',
              text: content,
            },
          ],
        };
      } catch (error) {
        throw new McpError(
          ErrorCode.InvalidRequest,
          `Failed to read resource ${uri}: ${error instanceof Error ? error.message : 'Unknown error'}`
        );
      }
    });
  }

  private setupPromptHandlers(): void {
    this.server.setRequestHandler(ListPromptsRequestSchema, async () => ({
      prompts: Object.values(prompts),
    }));

    this.server.setRequestHandler(GetPromptRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;
      
      if (!prompts[name]) {
        throw new McpError(ErrorCode.MethodNotFound, `Prompt ${name} not found`);
      }

      try {
        return await getPrompt(name, args || {});
      } catch (error) {
        throw new McpError(
          ErrorCode.InternalError,
          `Prompt ${name} failed: ${error instanceof Error ? error.message : 'Unknown error'}`
        );
      }
    });
  }

  private async ensureDocsAvailable(): Promise<void> {
    try {
      await ensureDocsInstalled();
    } catch (error) {
      console.error('Warning: Could not ensure docs are available:', error);
    }
  }

  async run(): Promise<void> {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('Claude Code Docs MCP server running on stdio');
  }
}

const server = new ClaudeCodeDocsServer();
server.run().catch(console.error);