#!/usr/bin/env python3
S = [input() for _ in range(12)]

ans = 0
for i in range(len(S)):
    if i + 1 == len(S[i]):
        ans += 1

print(ans)
