#!/usr/bin/env python3
N = int(input())
L = [list(map(int, input().split())) for l in range(N)]

tase = {}
result = 0

for l in L:
    if l[1] in tase:
        tase[l[1]] = min(tase[l[1]], l[0])
    else:
        tase[l[1]] = l[0]

for val in tase.values():
    result = max(result, val)

print(result)
