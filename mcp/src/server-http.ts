#!/usr/bin/env node

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
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
import { getRemoteDocumentationResources, readRemoteDocumentationResource } from './remote-resources/index.js';
import { prompts, getPrompt } from './prompts/index.js';
import express from 'express';
import cors from 'cors';

export const VERSION = "1.0.0";

class ClaudeCodeDocsHttpServer {
  private server: Server;
  private app: express.Application;

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

    this.app = express();
    this.setupMiddleware();
    this.setupToolHandlers();
    this.setupResourceHandlers();
    this.setupPromptHandlers();
    this.setupHttpEndpoints();
    this.setupErrorHandling();
  }

  private setupMiddleware(): void {
    this.app.use(cors({
      origin: true, // Allow all origins for now
      credentials: true,
    }));
    this.app.use(express.json({ limit: '10mb' }));
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
        const result = await this.searchDocsRemotely(args || {});
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
      const resources = await getRemoteDocumentationResources();
      return { resources };
    });

    this.server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
      const { uri } = request.params;
      try {
        const content = await readRemoteDocumentationResource(uri);
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

  private setupHttpEndpoints(): void {
    // Main MCP endpoint - handles all JSON-RPC requests
    this.app.post('/mcp', async (req, res) => {
      try {
        const jsonRpcRequest = req.body;
        
        // Handle the MCP request
        const result = await this.server.request(jsonRpcRequest);
        
        res.setHeader('Content-Type', 'application/json');
        res.json(result);
      } catch (error) {
        const errorResponse = {
          jsonrpc: '2.0',
          id: req.body.id || null,
          error: {
            code: -32603,
            message: error instanceof Error ? error.message : 'Internal error',
          },
        };
        res.status(500).json(errorResponse);
      }
    });

    // Health check endpoint
    this.app.get('/health', (req, res) => {
      res.json({ 
        status: 'healthy',
        server: 'claude-code-docs-mcp-server',
        version: VERSION,
        transport: 'http'
      });
    });

    // Capabilities endpoint
    this.app.get('/capabilities', (req, res) => {
      res.json({
        capabilities: this.server.getCapabilities(),
        tools: ['search_docs'],
        prompts: Object.keys(prompts),
        resources: 'remote-github'
      });
    });
  }

  private async searchDocsRemotely(args: any): Promise<string> {
    const { query = '', limit = 5 } = args;
    
    try {
      // Fetch and search through remote documentation
      const resources = await getRemoteDocumentationResources();
      const results: Array<{file: string, matches: string[], relevance: number}> = [];
      const queryLower = query.toLowerCase();

      for (const resource of resources.slice(0, 10)) { // Limit to prevent too many requests
        try {
          const content = await readRemoteDocumentationResource(resource.uri);
          const lines = content.split('\n');
          const matches: string[] = [];
          let relevance = 0;

          for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            const lineLower = line.toLowerCase();
            
            if (lineLower.includes(queryLower)) {
              const start = Math.max(0, i - 1);
              const end = Math.min(lines.length, i + 2);
              const context = lines.slice(start, end).join('\n');
              matches.push(`**Line ${i + 1}:**\n${context}`);
              relevance++;
            }
          }

          if (matches.length > 0) {
            results.push({ file: resource.name, matches, relevance });
          }
        } catch (error) {
          console.error(`Error reading ${resource.name}:`, error);
        }
      }

      results.sort((a, b) => b.relevance - a.relevance);

      if (results.length === 0) {
        return `No documentation found for query: "${query}"\n\nTry using these prompts for guided help:\n- **claude-code-setup**: Get started with Claude Code\n- **claude-code-learn**: Get a learning path\n- **claude-code-troubleshoot**: Troubleshooting help`;
      }

      let output = `# Remote Search Results for "${query}"\n\n`;
      output += `Found ${results.length} files with matches. Showing top ${Math.min(limit, results.length)} results:\n\n`;
      
      for (const result of results.slice(0, limit)) {
        output += `## 📄 ${result.file} (${result.relevance} matches)\n\n`;
        for (const match of result.matches.slice(0, 2)) {
          output += `${match}\n\n---\n\n`;
        }
      }

      output += `\n💡 **Need more help?** Use these prompts:\n`;
      output += `- **claude-code-setup**: Setup assistance\n`;
      output += `- **claude-code-learn**: Learning guidance\n`;
      output += `- **claude-code-troubleshoot**: Problem solving\n`;

      return output;
    } catch (error) {
      return `Error searching remote documentation: ${error instanceof Error ? error.message : 'Unknown error'}`;
    }
  }

  async run(port: number = 3000): Promise<void> {
    this.app.listen(port, '127.0.0.1', () => {
      console.error(`Claude Code Docs MCP server running on http://127.0.0.1:${port}`);
      console.error(`MCP endpoint: http://127.0.0.1:${port}/mcp`);
      console.error(`Health check: http://127.0.0.1:${port}/health`);
    });
  }
}

// Start server if run directly
if (import.meta.url === `file://${process.argv[1]}`) {
  const port = process.argv[2] ? parseInt(process.argv[2]) : 3000;
  const server = new ClaudeCodeDocsHttpServer();
  server.run(port).catch(console.error);
}