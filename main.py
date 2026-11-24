#!/usr/bin/env python3
"""Entry for make.fun's "Sum up 24 November's world news in one image".

The poster, ``entry.png``, is checked into this repository next to this
file. Rather than rendering anything at run time, the program delivers
those committed bytes verbatim to ``<out>/entry.png``. Because nothing is
generated, graded runs always see byte-identical output.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

POSTER = Path(__file__).resolve().with_name("entry.png")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Write the committed news poster to <out>/entry.png."
    )
    parser.add_argument(
        "--out",
        default="/output",
        metavar="DIR",
        help="destination directory for entry.png (default: %(default)s)",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(POSTER, target)
    target.chmod(0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
