#!/usr/bin/env python3
N = int(input())

if N < 42:
    print(f"AGC{str(N).zfill(3)}")
else:
    print(f"AGC{str(N + 1).zfill(3)}")
