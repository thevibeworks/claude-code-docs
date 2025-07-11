import { DocumentationService, DocumentationFile } from './documentation.js';
import { SearchService } from './search.js';

export interface TutorialStep {
  title: string;
  description: string;
  file: string;
  url?: string;
  estimatedTime: string;
  prerequisites?: string[];
}

export interface TutorialPath {
  name: string;
  description: string;
  steps: TutorialStep[];
  totalTime: string;
}

export interface ContextualHelp {
  suggestions: string[];
  relatedDocs: DocumentationFile[];
  quickActions: string[];
  troubleshootingSteps?: string[];
}

export class TutorialService {
  private documentationService: DocumentationService;
  private searchService: SearchService;

  constructor(documentationService: DocumentationService) {
    this.documentationService = documentationService;
    this.searchService = new SearchService(documentationService);
  }

  async getTutorialPath(skillLevel: string, goal: string): Promise<TutorialPath> {
    const pathKey = `${skillLevel}_${goal}`;
    
    const tutorialPaths: Record<string, TutorialPath> = {
      'beginner_getting_started': {
        name: 'Getting Started with Claude Code',
        description: 'Learn the basics of Claude Code from installation to your first project',
        totalTime: '2-3 hours',
        steps: [
          {
            title: 'Install and Set Up Claude Code',
            description: 'Learn how to install Claude Code and configure your first project',
            file: 'claude-code-docs/setup.md',
            url: 'https://github.com/lroolle/claude-code-docs/blob/main/claude-code-docs/setup.md',
            estimatedTime: '30 minutes'
          },
          {
            title: 'Quick Start Guide',
            description: 'Follow the quickstart to understand basic commands and workflows',
            file: 'claude-code-docs/quickstart.md',
            url: 'https://github.com/lroolle/claude-code-docs/blob/main/claude-code-docs/quickstart.md',
            estimatedTime: '45 minutes',
            prerequisites: ['setup']
          },
          {
            title: 'Understanding Settings and Permissions',
            description: 'Configure Claude Code settings for your development environment',
            file: 'claude-code-docs/settings.md',
            url: 'https://github.com/lroolle/claude-code-docs/blob/main/claude-code-docs/settings.md',
            estimatedTime: '30 minutes',
            prerequisites: ['quickstart']
          },
          {
            title: 'Common Workflows',
            description: 'Learn essential workflows for daily development tasks',
            file: 'claude-code-docs/common-workflows.md',
            url: 'https://github.com/lroolle/claude-code-docs/blob/main/claude-code-docs/common-workflows.md',
            estimatedTime: '60 minutes',
            prerequisites: ['settings']
          }
        ]
      },
      
      'intermediate_team_collaboration': {
        name: 'Team Collaboration with Claude Code',
        description: 'Learn advanced collaboration features and team workflows',
        totalTime: '3-4 hours',
        steps: [
          {
            title: 'GitHub Integration',
            description: 'Set up Claude Code with GitHub for seamless collaboration',
            file: 'claude-code-docs/github-actions.md',
            url: 'https://github.com/lroolle/claude-code-docs/blob/main/claude-code-docs/github-actions.md',
            estimatedTime: '45 minutes'
          },
          {
            title: 'Team Settings Configuration',
            description: 'Configure shared settings and permissions for team projects',
            file: 'claude-code-docs/settings.md',
            url: 'https://github.com/lroolle/claude-code-docs/blob/main/claude-code-docs/settings.md',
            estimatedTime: '30 minutes'
          },
          {
            title: 'Advanced Workflows',
            description: 'Master complex workflows for team development',
            file: 'claude-code-docs/common-workflows.md',
            url: 'https://github.com/lroolle/claude-code-docs/blob/main/claude-code-docs/common-workflows.md',
            estimatedTime: '90 minutes'
          },
          {
            title: 'Security and Compliance',
            description: 'Implement security best practices for team environments',
            file: 'claude-code-docs/security.md',
            url: 'https://github.com/lroolle/claude-code-docs/blob/main/claude-code-docs/security.md',
            estimatedTime: '60 minutes'
          }
        ]
      },
      
      'advanced_integrations': {
        name: 'Advanced Claude Code Integrations',
        description: 'Master MCP, IDE integrations, and custom workflows',
        totalTime: '4-5 hours',
        steps: [
          {
            title: 'Model Context Protocol (MCP)',
            description: 'Learn to create and use MCP servers for extended functionality',
            file: 'claude-code-docs/mcp.md',
            url: 'https://github.com/lroolle/claude-code-docs/blob/main/claude-code-docs/mcp.md',
            estimatedTime: '90 minutes'
          },
          {
            title: 'IDE Integrations',
            description: 'Set up Claude Code with your favorite development environment',
            file: 'claude-code-docs/ide-integrations.md',
            url: 'https://github.com/lroolle/claude-code-docs/blob/main/claude-code-docs/ide-integrations.md',
            estimatedTime: '60 minutes'
          },
          {
            title: 'Third-Party Integrations',
            description: 'Explore integrations with external tools and services',
            file: 'claude-code-docs/third-party-integrations.md',
            url: 'https://github.com/lroolle/claude-code-docs/blob/main/claude-code-docs/third-party-integrations.md',
            estimatedTime: '75 minutes'
          },
          {
            title: 'Monitoring and Usage Optimization',
            description: 'Track usage and optimize performance for large projects',
            file: 'claude-code-docs/monitoring-usage.md',
            url: 'https://github.com/lroolle/claude-code-docs/blob/main/claude-code-docs/monitoring-usage.md',
            estimatedTime: '45 minutes'
          }
        ]
      }
    };

    // Return requested path or create a custom one
    if (tutorialPaths[pathKey]) {
      return tutorialPaths[pathKey];
    }

    // Generate a custom path based on available documentation
    return await this.generateCustomPath(skillLevel, goal);
  }

  private async generateCustomPath(skillLevel: string, goal: string): Promise<TutorialPath> {
    const docs = this.documentationService.getAllDocuments();
    const relevantDocs = docs.filter(doc => {
      const content = (doc.title + ' ' + doc.content).toLowerCase();
      return content.includes(goal.replace('_', ' '));
    }).slice(0, 4);

    const steps: TutorialStep[] = relevantDocs.map((doc, index) => ({
      title: doc.title,
      description: doc.excerpt,
      file: doc.file,
      url: doc.url,
      estimatedTime: '45 minutes',
      prerequisites: index > 0 ? [relevantDocs[index - 1].title.toLowerCase().replace(/\s+/g, '_')] : undefined
    }));

    return {
      name: `Custom ${goal.replace('_', ' ')} Path`,
      description: `Tailored learning path for ${goal.replace('_', ' ')} at ${skillLevel} level`,
      totalTime: `${steps.length * 45} minutes`,
      steps
    };
  }

  async getContextualHelp(context: string, errorMessage?: string): Promise<ContextualHelp> {
    const help: ContextualHelp = {
      suggestions: [],
      relatedDocs: [],
      quickActions: []
    };

    // Analyze context to provide relevant help
    const contextLower = context.toLowerCase();
    
    // Search for relevant documentation
    let searchQuery = context;
    if (errorMessage) {
      searchQuery += ' ' + errorMessage;
    }
    
    const searchResults = await this.searchService.search(searchQuery, 'all', 5);
    help.relatedDocs = searchResults;

    // Generate contextual suggestions
    if (contextLower.includes('install') || contextLower.includes('setup')) {
      help.suggestions = [
        'Check that you have Node.js 18+ installed',
        'Verify your API key is properly configured',
        'Review the setup documentation for platform-specific instructions',
        'Try running the installation command with elevated permissions'
      ];
      help.quickActions = [
        'Check Node.js version: node --version',
        'Verify Claude Code installation: claude --version',
        'Check API key configuration: claude auth status'
      ];
    } else if (contextLower.includes('auth') || contextLower.includes('permission')) {
      help.suggestions = [
        'Verify your API key is valid and has the necessary permissions',
        'Check if your authentication token has expired',
        'Review project-level permission settings',
        'Ensure network connectivity to Anthropic services'
      ];
      help.quickActions = [
        'Check authentication status: claude auth status',
        'Re-authenticate: claude auth login',
        'Review settings: claude settings list'
      ];
    } else if (contextLower.includes('error') || contextLower.includes('fail')) {
      help.suggestions = [
        'Check the troubleshooting documentation for common solutions',
        'Verify all dependencies are properly installed',
        'Review recent changes that might have caused the issue',
        'Try restarting Claude Code or your development environment'
      ];
      help.troubleshootingSteps = [
        'Reproduce the error with minimal test case',
        'Check Claude Code logs for detailed error information',
        'Verify network connectivity and API status',
        'Try the command with --verbose flag for more details'
      ];
    } else if (contextLower.includes('slow') || contextLower.includes('performance')) {
      help.suggestions = [
        'Review memory management settings',
        'Check for large files or directories in your project scope',
        'Consider using ignore patterns for unnecessary files',
        'Monitor usage costs and API rate limits'
      ];
      help.quickActions = [
        'Check memory usage: claude memory status',
        'Review project scope: claude project info',
        'Optimize settings: claude settings optimize'
      ];
    } else {
      // General help suggestions
      help.suggestions = [
        'Check the relevant documentation section',
        'Review common workflows for similar tasks',
        'Search the troubleshooting guide for related issues',
        'Consider asking for help with more specific context'
      ];
    }

    return help;
  }

  async explainConcept(concept: string, detailLevel: string = 'detailed'): Promise<any> {
    // Search for documentation about the concept
    const searchResults = await this.searchService.searchByConcept(concept);
    
    const explanation = {
      concept,
      definition: '',
      keyPoints: [] as string[],
      examples: [] as string[],
      relatedConcepts: [] as string[],
      learnMore: [] as DocumentationFile[]
    };

    // Extract explanation from search results
    if (searchResults.length > 0) {
      const mainDoc = searchResults[0];
      explanation.definition = mainDoc.excerpt;
      explanation.learnMore = searchResults.slice(0, 3);
      
      // Extract key points from content
      const lines = mainDoc.content.split('\\n');
      for (const line of lines) {
        if (line.startsWith('- ') || line.startsWith('* ')) {
          explanation.keyPoints.push(line.substring(2).trim());
        }
        if (line.includes('```') && explanation.examples.length < 3) {
          // Extract code examples
          const codeStart = lines.indexOf(line);
          let codeEnd = codeStart + 1;
          while (codeEnd < lines.length && !lines[codeEnd].includes('```')) {
            codeEnd++;
          }
          if (codeEnd < lines.length) {
            explanation.examples.push(lines.slice(codeStart + 1, codeEnd).join('\\n'));
          }
        }
      }
    }

    // Add concept-specific information
    const conceptDefinitions: Record<string, any> = {
      'extended thinking': {
        definition: 'Extended thinking allows Claude Code to spend more time analyzing complex problems before providing solutions.',
        keyPoints: [
          'Enables deeper analysis of complex coding problems',
          'Helps with architectural decisions and code design',
          'Useful for debugging and troubleshooting',
          'Can be enabled per-session or per-query'
        ]
      },
      'mcp': {
        definition: 'Model Context Protocol (MCP) enables Claude Code to access external tools and data sources through standardized interfaces.',
        keyPoints: [
          'Extends Claude Code capabilities beyond built-in features',
          'Supports stdio, SSE, and HTTP transport methods',
          'Allows integration with databases, APIs, and other services',
          'Can be configured per-project or globally'
        ]
      },
      'memory management': {
        definition: 'Memory management in Claude Code refers to how conversation context and project information is stored and retrieved.',
        keyPoints: [
          'Maintains context across long conversations',
          'Stores project-specific knowledge and patterns',
          'Can be configured for different retention policies',
          'Helps with consistency in large projects'
        ]
      }
    };

    if (conceptDefinitions[concept.toLowerCase()]) {
      const predefined = conceptDefinitions[concept.toLowerCase()];
      explanation.definition = predefined.definition;
      explanation.keyPoints = predefined.keyPoints;
    }

    // Adjust detail level
    if (detailLevel === 'overview') {
      explanation.keyPoints = explanation.keyPoints.slice(0, 3);
      explanation.examples = [];
    } else if (detailLevel === 'advanced') {
      // Add more technical details for advanced level
      explanation.keyPoints.push('See documentation for implementation details and advanced configuration options');
    }

    return explanation;
  }

  getAvailableConcepts(): string[] {
    return [
      'extended thinking',
      'mcp',
      'memory management',
      'authentication',
      'permissions',
      'workflows',
      'github integration',
      'ide integration',
      'troubleshooting',
      'security',
      'team collaboration',
      'project settings'
    ];
  }
}