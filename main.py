#!/usr/bin/env python3
"""Entry for make.fun competition news-image-20261119.

Copies the pre-built entry.png sitting next to this file into the grader's
output directory. Python 3.13 standard library only; no network access.

Run locally with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    source = HERE / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"missing entry image: {source}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, OUT_DIR / "entry.png")


if __name__ == "__main__":
    main()
