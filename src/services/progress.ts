import * as fs from 'fs-extra';
import * as path from 'path';

export interface ProgressEntry {
  topic: string;
  completedAt: Date;
  timeSpent?: number; // in minutes
  notes?: string;
}

export interface LearningProgress {
  totalTopicsCompleted: number;
  totalTimeSpent: number; // in minutes
  completedTopics: ProgressEntry[];
  currentStreak: number;
  level: 'beginner' | 'intermediate' | 'advanced';
  badges: string[];
}

export interface NextSteps {
  recommendedTopics: string[];
  estimatedTime: string;
  reasoning: string;
}

export class ProgressService {
  private progressFile: string;
  private progress: LearningProgress;

  constructor() {
    this.progressFile = path.join(process.cwd(), '.claude-code-progress.json');
    this.progress = this.loadProgress();
  }

  private loadProgress(): LearningProgress {
    try {
      if (fs.existsSync(this.progressFile)) {
        const data = fs.readFileSync(this.progressFile, 'utf-8');
        const parsed = JSON.parse(data);
        
        // Convert date strings back to Date objects
        parsed.completedTopics = parsed.completedTopics.map((entry: any) => ({
          ...entry,
          completedAt: new Date(entry.completedAt)
        }));
        
        return parsed;
      }
    } catch (error) {
      console.error('Error loading progress:', error);
    }

    // Return default progress
    return {
      totalTopicsCompleted: 0,
      totalTimeSpent: 0,
      completedTopics: [],
      currentStreak: 0,
      level: 'beginner',
      badges: []
    };
  }

  private saveProgress(): void {
    try {
      fs.writeFileSync(this.progressFile, JSON.stringify(this.progress, null, 2));
    } catch (error) {
      console.error('Error saving progress:', error);
    }
  }

  async markComplete(topic: string, timeSpent?: number, notes?: string): Promise<any> {
    // Check if already completed
    const existingIndex = this.progress.completedTopics.findIndex(
      entry => entry.topic.toLowerCase() === topic.toLowerCase()
    );

    if (existingIndex >= 0) {
      // Update existing entry
      this.progress.completedTopics[existingIndex] = {
        topic,
        completedAt: new Date(),
        timeSpent,
        notes
      };
    } else {
      // Add new entry
      this.progress.completedTopics.push({
        topic,
        completedAt: new Date(),
        timeSpent,
        notes
      });
      this.progress.totalTopicsCompleted++;
    }

    if (timeSpent) {
      this.progress.totalTimeSpent += timeSpent;
    }

    // Update level and badges
    this.updateLevel();
    this.updateBadges();
    this.updateStreak();

    this.saveProgress();

    return {
      success: true,
      message: `Marked "${topic}" as complete`,
      newLevel: this.progress.level,
      newBadges: this.getNewBadges(topic)
    };
  }

  async getProgress(): Promise<LearningProgress> {
    return { ...this.progress };
  }

  async getNextSteps(): Promise<NextSteps> {
    const completedTopics = this.progress.completedTopics.map(entry => entry.topic.toLowerCase());
    
    // Define learning paths and dependencies
    const learningPaths = {
      beginner: [
        'installation and setup',
        'quickstart guide',
        'basic settings',
        'common workflows',
        'troubleshooting basics'
      ],
      intermediate: [
        'advanced settings',
        'github integration',
        'team collaboration',
        'security configuration',
        'ide integration'
      ],
      advanced: [
        'mcp development',
        'custom workflows',
        'performance optimization',
        'enterprise deployment',
        'advanced troubleshooting'
      ]
    };

    const currentPath = learningPaths[this.progress.level];
    const nextTopics = currentPath.filter(topic => 
      !completedTopics.some(completed => 
        completed.includes(topic.toLowerCase()) || topic.toLowerCase().includes(completed)
      )
    );

    let recommendedTopics: string[];
    let reasoning: string;

    if (nextTopics.length > 0) {
      recommendedTopics = nextTopics.slice(0, 3);
      reasoning = `Based on your ${this.progress.level} level progress, these topics will build on your existing knowledge.`;
    } else {
      // Suggest topics from next level
      const nextLevel = this.progress.level === 'beginner' ? 'intermediate' : 'advanced';
      const nextLevelTopics = learningPaths[nextLevel];
      recommendedTopics = nextLevelTopics.slice(0, 3);
      reasoning = `You've completed the ${this.progress.level} path! Ready to move to ${nextLevel} topics.`;
    }

    // Add personalized recommendations based on recent activity
    const recentTopics = this.progress.completedTopics
      .sort((a, b) => b.completedAt.getTime() - a.completedAt.getTime())
      .slice(0, 3)
      .map(entry => entry.topic.toLowerCase());

    if (recentTopics.some(topic => topic.includes('github'))) {
      if (!recommendedTopics.some(topic => topic.toLowerCase().includes('collaboration'))) {
        recommendedTopics.push('team collaboration');
      }
    }

    if (recentTopics.some(topic => topic.includes('setting'))) {
      if (!recommendedTopics.some(topic => topic.toLowerCase().includes('security'))) {
        recommendedTopics.push('security configuration');
      }
    }

    return {
      recommendedTopics: recommendedTopics.slice(0, 5),
      estimatedTime: `${recommendedTopics.length * 45} minutes`,
      reasoning
    };
  }

  private updateLevel(): void {
    const completed = this.progress.totalTopicsCompleted;
    
    if (completed >= 15) {
      this.progress.level = 'advanced';
    } else if (completed >= 7) {
      this.progress.level = 'intermediate';
    } else {
      this.progress.level = 'beginner';
    }
  }

  private updateBadges(): void {
    const badges = new Set(this.progress.badges);
    const completed = this.progress.totalTopicsCompleted;
    const timeSpent = this.progress.totalTimeSpent;

    // Completion badges
    if (completed >= 5 && !badges.has('First Steps')) {
      badges.add('First Steps');
    }
    if (completed >= 10 && !badges.has('Getting Serious')) {
      badges.add('Getting Serious');
    }
    if (completed >= 20 && !badges.has('Claude Code Expert')) {
      badges.add('Claude Code Expert');
    }

    // Time-based badges
    if (timeSpent >= 180 && !badges.has('Dedicated Learner')) { // 3 hours
      badges.add('Dedicated Learner');
    }
    if (timeSpent >= 600 && !badges.has('Power User')) { // 10 hours
      badges.add('Power User');
    }

    // Topic-specific badges
    const topicTypes = this.progress.completedTopics.map(entry => 
      this.categorizeTopic(entry.topic)
    );
    
    if (topicTypes.filter(type => type === 'setup').length >= 3 && !badges.has('Setup Master')) {
      badges.add('Setup Master');
    }
    if (topicTypes.filter(type => type === 'integration').length >= 2 && !badges.has('Integration Specialist')) {
      badges.add('Integration Specialist');
    }
    if (topicTypes.filter(type => type === 'advanced').length >= 3 && !badges.has('Advanced User')) {
      badges.add('Advanced User');
    }

    // Streak badges
    if (this.progress.currentStreak >= 3 && !badges.has('On Fire')) {
      badges.add('On Fire');
    }
    if (this.progress.currentStreak >= 7 && !badges.has('Unstoppable')) {
      badges.add('Unstoppable');
    }

    this.progress.badges = Array.from(badges);
  }

  private updateStreak(): void {
    if (this.progress.completedTopics.length === 0) {
      this.progress.currentStreak = 0;
      return;
    }

    // Sort by completion date
    const sorted = this.progress.completedTopics
      .sort((a, b) => b.completedAt.getTime() - a.completedAt.getTime());

    let streak = 1;
    let currentDate = new Date(sorted[0].completedAt);
    currentDate.setHours(0, 0, 0, 0); // Reset to start of day

    for (let i = 1; i < sorted.length; i++) {
      const entryDate = new Date(sorted[i].completedAt);
      entryDate.setHours(0, 0, 0, 0);
      
      const daysDiff = Math.floor((currentDate.getTime() - entryDate.getTime()) / (1000 * 60 * 60 * 24));
      
      if (daysDiff === 1) {
        streak++;
        currentDate = entryDate;
      } else if (daysDiff > 1) {
        break;
      }
      // If daysDiff === 0, same day, continue without incrementing streak
    }

    this.progress.currentStreak = streak;
  }

  private categorizeTopic(topic: string): string {
    const topicLower = topic.toLowerCase();
    
    if (topicLower.includes('setup') || topicLower.includes('install') || topicLower.includes('config')) {
      return 'setup';
    }
    if (topicLower.includes('github') || topicLower.includes('ide') || topicLower.includes('integration')) {
      return 'integration';
    }
    if (topicLower.includes('mcp') || topicLower.includes('advanced') || topicLower.includes('performance')) {
      return 'advanced';
    }
    if (topicLower.includes('workflow') || topicLower.includes('collaboration')) {
      return 'workflow';
    }
    return 'general';
  }

  private getNewBadges(topic: string): string[] {
    const previousBadges = new Set(this.progress.badges);
    this.updateBadges();
    
    return this.progress.badges.filter(badge => !previousBadges.has(badge));
  }

  async resetProgress(): Promise<any> {
    this.progress = {
      totalTopicsCompleted: 0,
      totalTimeSpent: 0,
      completedTopics: [],
      currentStreak: 0,
      level: 'beginner',
      badges: []
    };
    
    this.saveProgress();
    
    return {
      success: true,
      message: 'Progress has been reset'
    };
  }

  async exportProgress(): Promise<string> {
    const export_data = {
      exportDate: new Date(),
      progress: this.progress,
      summary: {
        totalTopicsCompleted: this.progress.totalTopicsCompleted,
        totalTimeSpentHours: Math.round(this.progress.totalTimeSpent / 60 * 10) / 10,
        currentLevel: this.progress.level,
        currentStreak: this.progress.currentStreak,
        badgesEarned: this.progress.badges.length
      }
    };

    return JSON.stringify(export_data, null, 2);
  }
}