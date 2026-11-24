#!/usr/bin/env python3
"""Entry for make.fun's "Sum up 24 November's world news in one image".

The poster is committed next to this file; the program copies it into
/output/entry.png byte-for-byte so both grading runs see identical output.
"""

import argparse
import os
import shutil
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="/output", help="output directory (the grader keeps the default)")
    args = parser.parse_args()
    os.umask(0o022)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    dst = out / "entry.png"
    shutil.copyfile(Path(__file__).resolve().parent / "entry.png", dst)
    dst.chmod(0o644)


if __name__ == "__main__":
    main()
