#!/usr/bin/env python3
H, N = map(int, input().split())

if (H - N) == 0:
    print(1)
else:
    print(32 ** (H - N))
