import Fuse from 'fuse.js';
import { DocumentationService, DocumentationFile } from './documentation.js';

export interface SearchResult extends DocumentationFile {
  score: number;
}

export class SearchService {
  private fuse: Fuse<DocumentationFile>;
  private documentationService: DocumentationService;

  constructor(documentationService: DocumentationService) {
    this.documentationService = documentationService;
    
    // Configure Fuse.js for fuzzy search
    const fuseOptions = {
      keys: [
        { name: 'title', weight: 0.4 },
        { name: 'content', weight: 0.3 },
        { name: 'excerpt', weight: 0.2 },
        { name: 'category', weight: 0.1 }
      ],
      threshold: 0.6, // More lenient matching
      includeScore: true,
      includeMatches: true,
      minMatchCharLength: 2,
      shouldSort: true,
    };

    this.fuse = new Fuse([], fuseOptions);
    this.refreshIndex();
  }

  private refreshIndex(): void {
    const documents = this.documentationService.getAllDocuments();
    this.fuse.setCollection(documents);
  }

  async search(query: string, category: string = 'all', limit: number = 5): Promise<SearchResult[]> {
    // Refresh index to ensure we have latest documents
    this.refreshIndex();

    let searchCollection = this.documentationService.getAllDocuments();
    
    // Filter by category if specified
    if (category !== 'all') {
      searchCollection = this.documentationService.getDocumentsByCategory(category);
      this.fuse.setCollection(searchCollection);
    }

    // Perform fuzzy search
    const fuseResults = this.fuse.search(query);
    
    // Convert to SearchResult format
    const results: SearchResult[] = fuseResults
      .slice(0, limit)
      .map(result => ({
        ...result.item,
        score: result.score || 0
      }));

    // If we don't have enough results, try a more lenient search
    if (results.length < limit) {
      const additionalResults = this.searchExact(query, category, limit - results.length);
      
      // Add additional results that aren't already included
      const existingFiles = new Set(results.map(r => r.file));
      for (const additional of additionalResults) {
        if (!existingFiles.has(additional.file)) {
          results.push(additional);
        }
      }
    }

    return results;
  }

  private searchExact(query: string, category: string, limit: number): SearchResult[] {
    const documents = category === 'all' 
      ? this.documentationService.getAllDocuments()
      : this.documentationService.getDocumentsByCategory(category);

    const queryLower = query.toLowerCase();
    const matches: SearchResult[] = [];

    for (const doc of documents) {
      let score = 0;
      
      // Title match (highest weight)
      if (doc.title.toLowerCase().includes(queryLower)) {
        score += 0.8;
      }
      
      // Content match
      const contentMatches = (doc.content.toLowerCase().match(new RegExp(queryLower, 'g')) || []).length;
      if (contentMatches > 0) {
        score += Math.min(contentMatches * 0.1, 0.5);
      }
      
      // Excerpt match
      if (doc.excerpt.toLowerCase().includes(queryLower)) {
        score += 0.3;
      }

      if (score > 0) {
        matches.push({
          ...doc,
          score: 1 - score // Invert score to match Fuse.js convention (lower is better)
        });
      }
    }

    return matches
      .sort((a, b) => a.score - b.score)
      .slice(0, limit);
  }

  async searchByKeywords(keywords: string[], category: string = 'all', limit: number = 5): Promise<SearchResult[]> {
    const allResults: Map<string, SearchResult> = new Map();

    // Search for each keyword and combine results
    for (const keyword of keywords) {
      const results = await this.search(keyword, category, limit * 2);
      
      for (const result of results) {
        const existing = allResults.get(result.file);
        if (existing) {
          // Combine scores (average them)
          existing.score = (existing.score + result.score) / 2;
        } else {
          allResults.set(result.file, result);
        }
      }
    }

    return Array.from(allResults.values())
      .sort((a, b) => a.score - b.score)
      .slice(0, limit);
  }

  async searchByConcept(concept: string): Promise<SearchResult[]> {
    // Map concepts to specific search terms
    const conceptMap: Record<string, string[]> = {
      'setup': ['install', 'configuration', 'authentication', 'api key'],
      'workflow': ['workflow', 'collaboration', 'team', 'project'],
      'mcp': ['model context protocol', 'mcp', 'server', 'integration'],
      'memory': ['memory', 'context', 'conversation', 'history'],
      'troubleshooting': ['error', 'debug', 'problem', 'issue', 'fix'],
      'security': ['security', 'permission', 'authentication', 'access'],
      'integration': ['github', 'ide', 'editor', 'vscode', 'integration'],
      'extended thinking': ['extended thinking', 'reasoning', 'analysis'],
    };

    const searchTerms = conceptMap[concept.toLowerCase()] || [concept];
    return await this.searchByKeywords(searchTerms, 'all', 10);
  }

  getPopularTopics(): { topic: string; count: number }[] {
    const documents = this.documentationService.getAllDocuments();
    const topicCounts: Record<string, number> = {};

    // Count occurrences of common topics
    const commonTopics = [
      'setup', 'install', 'configuration', 'workflow', 'github', 
      'mcp', 'memory', 'troubleshooting', 'security', 'integration',
      'extended thinking', 'collaboration', 'api', 'authentication'
    ];

    for (const topic of commonTopics) {
      topicCounts[topic] = 0;
      for (const doc of documents) {
        const content = (doc.title + ' ' + doc.content).toLowerCase();
        const matches = (content.match(new RegExp(topic, 'g')) || []).length;
        topicCounts[topic] += matches;
      }
    }

    return Object.entries(topicCounts)
      .sort(([, a], [, b]) => b - a)
      .slice(0, 10)
      .map(([topic, count]) => ({ topic, count }));
  }
}