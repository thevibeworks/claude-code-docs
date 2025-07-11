import * as fs from 'fs-extra';
import * as path from 'path';
import matter from 'gray-matter';
import MarkdownIt from 'markdown-it';

export interface DocumentationFile {
  file: string;
  title: string;
  content: string;
  excerpt: string;
  category: string;
  metadata: Record<string, any>;
  url?: string;
}

export class DocumentationService {
  private documents: DocumentationFile[] = [];
  private markdown: MarkdownIt;
  private basePath: string;

  constructor() {
    this.markdown = new MarkdownIt();
    this.basePath = process.cwd();
  }

  async initialize(): Promise<void> {
    await this.loadDocuments();
  }

  private async loadDocuments(): Promise<void> {
    this.documents = [];
    
    // Load Claude Code documentation
    await this.loadFromDirectory('claude-code-docs', 'documentation');
    
    // Load blog posts
    await this.loadFromDirectory('anthropic-blog', 'blog');
    
    // Load release notes
    await this.loadFromDirectory('release-notes', 'releases');
    
    console.error(`Loaded ${this.documents.length} documentation files`);
  }

  private async loadFromDirectory(dirName: string, category: string): Promise<void> {
    const dirPath = path.join(this.basePath, dirName);
    
    if (!await fs.pathExists(dirPath)) {
      console.error(`Directory not found: ${dirPath}`);
      return;
    }

    await this.processDirectory(dirPath, category, dirName);
  }

  private async processDirectory(dirPath: string, category: string, baseDir: string): Promise<void> {
    const items = await fs.readdir(dirPath, { withFileTypes: true });
    
    for (const item of items) {
      const fullPath = path.join(dirPath, item.name);
      
      if (item.isDirectory()) {
        await this.processDirectory(fullPath, category, baseDir);
      } else if (item.name.endsWith('.md')) {
        await this.processMarkdownFile(fullPath, category, baseDir);
      }
    }
  }

  private async processMarkdownFile(filePath: string, category: string, baseDir: string): Promise<void> {
    try {
      const content = await fs.readFile(filePath, 'utf-8');
      const parsed = matter(content);
      
      const relativePath = path.relative(this.basePath, filePath);
      const title = this.extractTitle(parsed.content, path.basename(filePath, '.md'));
      const excerpt = this.createExcerpt(parsed.content);
      
      // Determine subcategory based on file location
      const subcategory = this.determineSubcategory(relativePath, category);
      
      this.documents.push({
        file: relativePath,
        title,
        content: parsed.content,
        excerpt,
        category: subcategory,
        metadata: parsed.data,
        url: this.generateGitHubUrl(relativePath)
      });
    } catch (error) {
      console.error(`Error processing ${filePath}:`, error);
    }
  }

  private extractTitle(content: string, fallback: string): string {
    const lines = content.split('\\n');
    for (const line of lines) {
      if (line.startsWith('# ')) {
        return line.substring(2).trim();
      }
    }
    return fallback.replace(/-/g, ' ').replace(/\\b\\w/g, l => l.toUpperCase());
  }

  private createExcerpt(content: string, maxLength: number = 300): string {
    // Remove markdown headers and formatting
    let text = content
      .replace(/^#+\\s+/gm, '') // Remove headers
      .replace(/\\*\\*(.*?)\\*\\*/g, '$1') // Remove bold
      .replace(/\\*(.*?)\\*/g, '$1') // Remove italic
      .replace(/\\[(.*?)\\]\\(.*?\\)/g, '$1') // Remove links
      .replace(/```[\\s\\S]*?```/g, '') // Remove code blocks
      .replace(/`(.*?)`/g, '$1') // Remove inline code
      .replace(/\\n+/g, ' ') // Replace newlines with spaces
      .trim();

    if (text.length > maxLength) {
      text = text.substring(0, maxLength).trim() + '...';
    }

    return text;
  }

  private determineSubcategory(relativePath: string, baseCategory: string): string {
    if (baseCategory === 'documentation') {
      if (relativePath.includes('quickstart')) return 'quickstart';
      if (relativePath.includes('setup')) return 'setup';
      if (relativePath.includes('workflow') || relativePath.includes('common-workflow')) return 'workflows';
      if (relativePath.includes('troubleshoot')) return 'troubleshooting';
      if (relativePath.includes('mcp')) return 'mcp';
      if (relativePath.includes('integration') || relativePath.includes('github') || relativePath.includes('ide')) return 'integrations';
      if (relativePath.includes('security') || relativePath.includes('iam')) return 'security';
      return 'documentation';
    }
    
    return baseCategory;
  }

  private generateGitHubUrl(relativePath: string): string {
    return `https://github.com/lroolle/claude-code-docs/blob/main/${relativePath}`;
  }

  getAllDocuments(): DocumentationFile[] {
    return this.documents;
  }

  getDocumentsByCategory(category: string): DocumentationFile[] {
    if (category === 'all') {
      return this.documents;
    }
    return this.documents.filter(doc => doc.category === category);
  }

  getDocument(filePath: string): DocumentationFile | undefined {
    return this.documents.find(doc => doc.file === filePath);
  }

  searchContent(query: string): DocumentationFile[] {
    const queryLower = query.toLowerCase();
    return this.documents.filter(doc => 
      doc.title.toLowerCase().includes(queryLower) ||
      doc.content.toLowerCase().includes(queryLower) ||
      doc.excerpt.toLowerCase().includes(queryLower)
    );
  }

  async refresh(): Promise<void> {
    await this.loadDocuments();
  }
}