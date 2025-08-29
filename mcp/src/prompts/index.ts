export const prompts = {
  'claude-code-setup': {
    name: 'claude-code-setup',
    description: 'Get help setting up Claude Code for your environment',
    arguments: [
      {
        name: 'platform',
        description: 'Your operating system (mac, windows, linux)',
        required: false,
      },
      {
        name: 'experience',
        description: 'Your experience level (beginner, intermediate, advanced)',
        required: false,
      },
    ],
  },
  'claude-code-learn': {
    name: 'claude-code-learn',
    description: 'Get a personalized learning path for Claude Code',
    arguments: [
      {
        name: 'goal',
        description: 'What you want to achieve with Claude Code',
        required: true,
      },
      {
        name: 'time',
        description: 'How much time you have (30min, 2hours, 1day, flexible)',
        required: false,
      },
      {
        name: 'experience',
        description: 'Your experience level (beginner, intermediate, advanced)',
        required: false,
      },
    ],
  },
  'claude-code-troubleshoot': {
    name: 'claude-code-troubleshoot',
    description: 'Get help troubleshooting Claude Code issues',
    arguments: [
      {
        name: 'problem',
        description: 'Describe the problem you are experiencing',
        required: true,
      },
      {
        name: 'error_message',
        description: 'Any error messages you are seeing',
        required: false,
      },
    ],
  },
  'claude-code-workflow': {
    name: 'claude-code-workflow',
    description: 'Learn common Claude Code workflows and best practices',
    arguments: [
      {
        name: 'use_case',
        description: 'Your specific use case or project type',
        required: true,
      },
      {
        name: 'tools',
        description: 'Tools you want to integrate with (git, vscode, etc.)',
        required: false,
      },
    ],
  },
};

export async function getPrompt(name: string, args: Record<string, any>) {
  switch (name) {
    case 'claude-code-setup':
      return getSetupPrompt(args);
    case 'claude-code-learn':
      return getLearningPrompt(args);
    case 'claude-code-troubleshoot':
      return getTroubleshootPrompt(args);
    case 'claude-code-workflow':
      return getWorkflowPrompt(args);
    default:
      throw new Error(`Unknown prompt: ${name}`);
  }
}

async function getSetupPrompt(args: Record<string, any>) {
  const platform = args.platform || 'your system';
  const experience = args.experience || 'beginner';
  
  return {
    messages: [
      {
        role: 'user' as const,
        content: {
          type: 'text' as const,
          text: `I need help setting up Claude Code on ${platform}. My experience level is ${experience}. 

Please provide a step-by-step setup guide that includes:
1. Installation instructions
2. Initial configuration 
3. Authentication setup
4. Basic usage verification
5. Common next steps

Focus on ${platform} specific instructions and explain things clearly for a ${experience} user.`,
        },
      },
    ],
  };
}

async function getLearningPrompt(args: Record<string, any>) {
  const goal = args.goal;
  const time = args.time || 'flexible';
  const experience = args.experience || 'beginner';
  
  return {
    messages: [
      {
        role: 'user' as const,
        content: {
          type: 'text' as const,
          text: `I want to learn Claude Code to ${goal}. I have ${time} available and my experience level is ${experience}.

Please create a personalized learning path that includes:
1. Prerequisites and setup
2. Core concepts I need to understand
3. Step-by-step learning progression
4. Hands-on exercises and examples
5. Resources for further learning
6. Common pitfalls to avoid

Tailor the path for my ${experience} level and ${time} timeframe, focusing on achieving: ${goal}`,
        },
      },
    ],
  };
}

async function getTroubleshootPrompt(args: Record<string, any>) {
  const problem = args.problem;
  const errorMessage = args.error_message || 'no specific error message';
  
  return {
    messages: [
      {
        role: 'user' as const,
        content: {
          type: 'text' as const,
          text: `I'm having trouble with Claude Code. Here's what's happening:

**Problem:** ${problem}
**Error Message:** ${errorMessage}

Please help me troubleshoot this issue by:
1. Identifying the most likely causes
2. Providing step-by-step debugging steps
3. Suggesting specific solutions to try
4. Explaining how to verify the fix worked
5. Recommending prevention strategies

Focus on practical, actionable solutions I can implement right away.`,
        },
      },
    ],
  };
}

async function getWorkflowPrompt(args: Record<string, any>) {
  const useCase = args.use_case;
  const tools = args.tools || 'standard development tools';
  
  return {
    messages: [
      {
        role: 'user' as const,
        content: {
          type: 'text' as const,
          text: `I want to learn Claude Code workflows for ${useCase}. I primarily use ${tools} in my development process.

Please provide guidance on:
1. Best practices for ${useCase} with Claude Code
2. How to integrate Claude Code with ${tools}
3. Efficient workflows and shortcuts
4. Configuration recommendations
5. Example commands and usage patterns
6. Tips for maximizing productivity

Focus on practical workflows I can implement in my ${useCase} projects.`,
        },
      },
    ],
  };
}