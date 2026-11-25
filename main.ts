// Entry for make.fun's "Sum up 24 November's world news in one image" bounty.
//
// The poster, `entry.png`, is checked into this repository next to this file.
// The program delivers those committed bytes verbatim to `<out>/entry.png`;
// because nothing is generated at run time, every graded run sees the same
// byte-identical image.

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

// --out <dir> overrides MAKEFUN_OUTPUT_DIR for local runs.
const cliOut = process.argv.indexOf("--out");
const outDir =
  cliOut > -1 && process.argv[cliOut + 1]
    ? process.argv[cliOut + 1]
    : process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const poster = join(dirname(fileURLToPath(import.meta.url)), "entry.png");

mkdirSync(outDir, { recursive: true });
copyFileSync(poster, join(outDir, "entry.png"));
console.log(`wrote ${join(outDir, "entry.png")}`);
