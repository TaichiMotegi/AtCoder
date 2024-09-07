#!/usr/bin/env python3
S = [input() for _ in range(3)]

contests = ["ABC", "ARC", "AGC", "AHC"]

for contest in contests:
    if contest in S:
        continue
    else:
        print(contest)