export interface Tool {
  name: string;
  description: string;
  inputSchema: any;
  handler: (args: any) => Promise<string>;
}