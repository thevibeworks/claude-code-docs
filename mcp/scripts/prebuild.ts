#!/usr/bin/env bun

import { mkdir } from 'fs/promises';

// Ensure dist directory exists
await mkdir('dist', { recursive: true });

console.log('✅ Build preparation complete');