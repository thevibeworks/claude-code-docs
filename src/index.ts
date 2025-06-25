#!/usr/bin/env node

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  Tool,
} from '@modelcontextprotocol/sdk/types.js';
import { DocumentationService } from './services/documentation.js';
import { SearchService } from './services/search.js';
import { TutorialService } from './services/tutorial.js';
import { ProgressService } from './services/progress.js';

class ClaudeCodeDocsMCPServer {
  private server: Server;
  private documentationService: DocumentationService;
  private searchService: SearchService;
  private tutorialService: TutorialService;
  private progressService: ProgressService;

  constructor() {
    this.server = new Server(
      {
        name: 'claude-code-docs-mcp-server',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
        },
      }
    );

    this.documentationService = new DocumentationService();
    this.searchService = new SearchService(this.documentationService);
    this.tutorialService = new TutorialService(this.documentationService);
    this.progressService = new ProgressService();

    this.setupHandlers();
  }

  private setupHandlers() {
    this.server.setRequestHandler(ListToolsRequestSchema, async () => {
      return {
        tools: [
          {
            name: 'search_documentation',
            description: 'Search Claude Code documentation for specific topics, commands, or concepts',
            inputSchema: {
              type: 'object',
              properties: {
                query: {
                  type: 'string',
                  description: 'Search query for documentation content',
                },
                category: {
                  type: 'string',
                  enum: ['all', 'quickstart', 'setup', 'workflows', 'troubleshooting', 'mcp', 'integrations', 'security'],
                  description: 'Optional category filter for search results',
                },
                limit: {
                  type: 'number',
                  description: 'Maximum number of results to return (default: 5)',
                  minimum: 1,
                  maximum: 20,
                },
              },
              required: ['query'],
            },
          },
          {
            name: 'get_tutorial_path',
            description: 'Get a personalized learning path based on user skill level and goals',
            inputSchema: {
              type: 'object',
              properties: {
                skill_level: {
                  type: 'string',
                  enum: ['beginner', 'intermediate', 'advanced'],
                  description: 'Current skill level with Claude Code',
                },
                goal: {
                  type: 'string',
                  enum: ['getting_started', 'team_collaboration', 'advanced_workflows', 'integrations', 'troubleshooting'],
                  description: 'Learning goal or focus area',
                },
              },
              required: ['skill_level', 'goal'],
            },
          },
          {
            name: 'get_contextual_help',
            description: 'Get help based on current situation or error messages',
            inputSchema: {
              type: 'object',
              properties: {
                context: {
                  type: 'string',
                  description: 'Description of current situation or problem',
                },
                error_message: {
                  type: 'string',
                  description: 'Optional error message if encountering issues',
                },
              },
              required: ['context'],
            },
          },
          {
            name: 'track_progress',
            description: 'Track learning progress and get recommendations for next steps',
            inputSchema: {
              type: 'object',
              properties: {
                completed_topic: {
                  type: 'string',
                  description: 'Topic or section just completed',
                },
                action: {
                  type: 'string',
                  enum: ['mark_complete', 'get_progress', 'get_next_steps'],
                  description: 'Action to perform with progress tracking',
                },
              },
              required: ['action'],
            },
          },
          {
            name: 'explain_concept',
            description: 'Get detailed explanation of Claude Code concepts with examples',
            inputSchema: {
              type: 'object',
              properties: {
                concept: {
                  type: 'string',
                  description: 'Concept to explain (e.g., "extended thinking", "MCP", "memory management")',
                },
                detail_level: {
                  type: 'string',
                  enum: ['overview', 'detailed', 'advanced'],
                  description: 'Level of detail for explanation',
                },
              },
              required: ['concept'],
            },
          },
        ],
      };
    });

    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      try {
        switch (name) {
          case 'search_documentation':
            return await this.handleSearchDocumentation(args);
          case 'get_tutorial_path':
            return await this.handleGetTutorialPath(args);
          case 'get_contextual_help':
            return await this.handleGetContextualHelp(args);
          case 'track_progress':
            return await this.handleTrackProgress(args);
          case 'explain_concept':
            return await this.handleExplainConcept(args);
          default:
            throw new Error(`Unknown tool: ${name}`);
        }
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: `Error: ${error instanceof Error ? error.message : String(error)}`,
            },
          ],
        };
      }
    });
  }

  private async handleSearchDocumentation(args: any) {
    const { query, category = 'all', limit = 5 } = args;
    const results = await this.searchService.search(query, category, limit);
    
    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify({
            query,
            category,
            results: results.map(result => ({
              title: result.title,
              file: result.file,
              excerpt: result.excerpt,
              score: result.score,
              url: result.url
            }))
          }, null, 2),
        },
      ],
    };
  }

  private async handleGetTutorialPath(args: any) {
    const { skill_level, goal } = args;
    const path = await this.tutorialService.getTutorialPath(skill_level, goal);
    
    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify({
            skill_level,
            goal,
            tutorial_path: path
          }, null, 2),
        },
      ],
    };
  }

  private async handleGetContextualHelp(args: any) {
    const { context, error_message } = args;
    const help = await this.tutorialService.getContextualHelp(context, error_message);
    
    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify({
            context,
            error_message,
            help
          }, null, 2),
        },
      ],
    };
  }

  private async handleTrackProgress(args: any) {
    const { completed_topic, action } = args;
    let result;
    
    switch (action) {
      case 'mark_complete':
        result = await this.progressService.markComplete(completed_topic);
        break;
      case 'get_progress':
        result = await this.progressService.getProgress();
        break;
      case 'get_next_steps':
        result = await this.progressService.getNextSteps();
        break;
      default:
        throw new Error(`Unknown progress action: ${action}`);
    }
    
    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify({
            action,
            completed_topic,
            result
          }, null, 2),
        },
      ],
    };
  }

  private async handleExplainConcept(args: any) {
    const { concept, detail_level = 'detailed' } = args;
    const explanation = await this.tutorialService.explainConcept(concept, detail_level);
    
    return {
      content: [
        {
          type: 'text',
          text: JSON.stringify({
            concept,
            detail_level,
            explanation
          }, null, 2),
        },
      ],
    };
  }

  async run() {
    // Initialize services
    await this.documentationService.initialize();
    
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('Claude Code Documentation MCP server running on stdio');
  }
}

async function main() {
  const server = new ClaudeCodeDocsMCPServer();
  await server.run();
}

if (import.meta.url === `file://${process.argv[1]}`) {
  main().catch((error) => {
    console.error('Server error:', error);
    process.exit(1);
  });
}