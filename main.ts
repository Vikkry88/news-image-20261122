// Entry program for the Sunday 22 November 2026 news-image competition (Node 22).
//
// The front-page picture is drawn ahead of time by make_image.py and stored as
// entry.png beside this file. This program copies those exact bytes to the
// output directory (/output in the grader, MAKEFUN_OUTPUT_DIR when local),
// so every run writes identical bytes as the rules require.

import { copyFileSync, existsSync, mkdirSync, statSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const sourceImage = join(here, 'entry.png');
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const destination = join(outputDir, 'entry.png');

if (!existsSync(sourceImage)) {
  throw new Error(`entry.png is missing beside main.ts (looked in ${here})`);
}

mkdirSync(outputDir, { recursive: true });
copyFileSync(sourceImage, destination);

const size = statSync(destination).size;
if (size === 0 || size > 1024 * 1024) {
  throw new Error(`entry.png must be a whole image of at most 1 MiB, got ${size} bytes`);
}

console.log(`wrote ${destination} (${size} bytes)`);
