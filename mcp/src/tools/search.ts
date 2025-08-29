import { z } from 'zod';
import { zodToJsonSchema } from 'zod-to-json-schema';
import { readFile, readdir } from 'fs/promises';
import { join } from 'path';
import { getDocsPath } from '../resources/index.js';

const SearchArgsSchema = z.object({
  query: z.string().describe('Search query to find relevant documentation'),
  limit: z.number().default(5).describe('Maximum number of results to return'),
});

type SearchArgs = z.infer<typeof SearchArgsSchema>;

export const searchTool = {
  name: 'search_docs',
  description: 'Search through Claude Code documentation for relevant content',
  inputSchema: zodToJsonSchema(SearchArgsSchema),
  handler: async (args: SearchArgs): Promise<string> => {
    const { query, limit } = SearchArgsSchema.parse(args);
    
    const docsPath = await getDocsPath();
    const contentDir = join(docsPath, 'content', 'claude-code-docs');
    
    try {
      const files = await readdir(contentDir);
      const markdownFiles = files.filter(f => f.endsWith('.md'));
      
      const results: Array<{file: string, matches: string[], relevance: number}> = [];
      const queryLower = query.toLowerCase();

      for (const file of markdownFiles) {
        try {
          const content = await readFile(join(contentDir, file), 'utf-8');
          const lines = content.split('\n');
          const matches: string[] = [];
          let relevance = 0;

          for (let i = 0; i < lines.length; i++) {
            const line = lines[i];
            const lineLower = line.toLowerCase();
            
            if (lineLower.includes(queryLower)) {
              // Get context around the match
              const start = Math.max(0, i - 1);
              const end = Math.min(lines.length, i + 2);
              const context = lines.slice(start, end).join('\n');
              matches.push(`**Line ${i + 1}:**\n${context}`);
              relevance++;
            }
          }

          if (matches.length > 0) {
            results.push({ file, matches, relevance });
          }
        } catch (error) {
          console.error(`Error reading ${file}:`, error);
        }
      }

      // Sort by relevance
      results.sort((a, b) => b.relevance - a.relevance);

      if (results.length === 0) {
        return `No documentation found for query: "${query}"\n\nTry using these prompts for guided help:\n- **claude-code-setup**: Get started with Claude Code\n- **claude-code-learn**: Get a learning path\n- **claude-code-troubleshoot**: Troubleshooting help`;
      }

      let output = `# Search Results for "${query}"\n\n`;
      output += `Found ${results.length} files with matches. Showing top ${Math.min(limit, results.length)} results:\n\n`;
      
      for (const result of results.slice(0, limit)) {
        output += `## 📄 ${result.file} (${result.relevance} matches)\n\n`;
        for (const match of result.matches.slice(0, 2)) { // Top 2 matches per file
          output += `${match}\n\n---\n\n`;
        }
      }

      output += `\n💡 **Need more help?** Use these prompts:\n`;
      output += `- **claude-code-setup**: Setup assistance\n`;
      output += `- **claude-code-learn**: Learning guidance\n`;
      output += `- **claude-code-troubleshoot**: Problem solving\n`;

      return output;
    } catch (error) {
      return `Error searching documentation: ${error instanceof Error ? error.message : 'Unknown error'}`;
    }
  },
};