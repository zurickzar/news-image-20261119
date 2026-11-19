#!/usr/bin/env python3
"""News-image entry for make.fun's "Sum up 19 November's world news in one image".

The entry is a program that writes one image to /output/entry.png.
This program copies the image the repository holds (entry.png) there.

Standard library only, no network, no randomness, no clock: two runs
write exactly the same bytes, as the competition requires.

Run it outside the grader's container with:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(src):
        raise SystemExit("entry.png missing beside main.py")
    shutil.copyfile(src, dst)
    # Self-check: the output must be a whole image the judge can read.
    size = os.path.getsize(dst)
    if size == 0 or size > 1048576:
        raise SystemExit(f"entry.png output is {size} bytes, outside the 1 MiB cap")
    with open(dst, "rb") as f:
        magic = f.read(3)
    if magic not in (b"\xff\xd8\xff", b"\x89PN"):
        raise SystemExit("entry.png output is neither JPEG nor PNG")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
