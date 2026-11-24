#!/usr/bin/env python3
"""Entry point: copy the pre-drawn front page to the output directory.

Stdlib only. Writes entry.png into $MAKEFUN_OUTPUT_DIR (or /output),
mode 0644. Deterministic: the same bytes on every run.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    os.chmod(dst, 0o644)
    print("wrote", dst)


if __name__ == "__main__":
    sys.exit(main())
