#!/usr/bin/env bun

import { mkdir, writeFile, readFile } from 'fs/promises';
import { join } from 'path';

const toolName = process.argv[2];

if (!toolName) {
  console.error('Usage: bun run create-tool.ts <tool-name>');
  process.exit(1);
}

const toolDir = join('src', 'tools', toolName);
const toolFile = join(toolDir, 'index.ts');

// Create tool directory
await mkdir(toolDir, { recursive: true });

// Template for new tool
const toolTemplate = `import { z } from 'zod';
import { zodToJsonSchema } from 'zod-to-json-schema';

const ${toolName.charAt(0).toUpperCase() + toolName.slice(1)}ArgsSchema = z.object({
  // Add your parameters here
  example: z.string().describe('Example parameter'),
});

type ${toolName.charAt(0).toUpperCase() + toolName.slice(1)}Args = z.infer<typeof ${toolName.charAt(0).toUpperCase() + toolName.slice(1)}ArgsSchema>;

export const ${toolName} = {
  name: '${toolName}',
  description: 'Description of what this tool does',
  inputSchema: zodToJsonSchema(${toolName.charAt(0).toUpperCase() + toolName.slice(1)}ArgsSchema),
  handler: async (args: ${toolName.charAt(0).toUpperCase() + toolName.slice(1)}Args): Promise<string> => {
    const { example } = ${toolName.charAt(0).toUpperCase() + toolName.slice(1)}ArgsSchema.parse(args);
    
    // Implement your tool logic here
    return \`Tool \${toolName} executed with: \${example}\`;
  },
};
`;

await writeFile(toolFile, toolTemplate);

// Update tools index file
const indexPath = join('src', 'tools', 'index.ts');
const indexContent = await readFile(indexPath, 'utf-8');

const importLine = `import { ${toolName} } from './${toolName}/index.js';`;
const exportLine = `  ${toolName},`;

const lines = indexContent.split('\n');
const importIndex = lines.findIndex(line => line.includes('import'));
const exportIndex = lines.findIndex(line => line.includes('export const tools'));

// Add import
lines.splice(importIndex, 0, importLine);

// Add to exports
const exportLineIndex = lines.findIndex(line => line.includes('];'));
lines.splice(exportLineIndex, 0, exportLine);

await writeFile(indexPath, lines.join('\n'));

console.log(`✅ Tool '${toolName}' created successfully!`);
console.log(`📁 Location: ${toolFile}`);
console.log(`🔧 Updated tools index file`);