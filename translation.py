#!/usr/bin/env python3
import sys


if len(sys.argv) != 1:
    print("binstr: 引数は不要です", file=sys.stderr)
    sys.exit(1)

for line in sys.stdin:
    line = line.rstrip("\n")

    bins = []
    for ch in line:
        for b in ch.encode("utf-8"):
            bins.append(format(b, "08b"))

    print(" ".join(bins))

