#!/usr/bin/env python3
"""Split a word/difficulty/pos TSV into separate txt files, one per difficulty.

Input format (tab-separated), e.g. candidates.tsv:
    aah	2	verb
    aardvark	1	noun

Output:
    difficulty_1.txt, difficulty_2.txt, ... each containing one word per line
    for that difficulty level (word only, no tabs/pos).

Usage:
    python3 split_by_difficulty.py candidates.tsv
    python3 split_by_difficulty.py candidates.tsv --outdir ./out --prefix difficulty_
"""
import argparse
import os
from collections import defaultdict


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input", help="input TSV file (word<TAB>difficulty<TAB>pos)")
    ap.add_argument("--outdir", default=".", help="directory for output txt files")
    ap.add_argument("--prefix", default="", help="output filename prefix")
    args = ap.parse_args()

    words_by_level = defaultdict(list)

    with open(args.input, encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            parts = line.split("\t")
            if len(parts) < 2:
                print(f"skipping malformed line {lineno}: {line!r}")
                continue
            word = parts[0].strip()
            level = parts[1].strip()
            if not word or not level:
                continue
            words_by_level[level].append(word)

    os.makedirs(args.outdir, exist_ok=True)

    for level, words in sorted(words_by_level.items()):
        out_path = os.path.join(args.outdir, f"{args.prefix}{level}.txt")
        with open(out_path, "w", encoding="utf-8") as out:
            out.write("\n".join(words) + "\n")
        print(f"wrote {out_path}: {len(words)} words")


if __name__ == "__main__":
    main()

