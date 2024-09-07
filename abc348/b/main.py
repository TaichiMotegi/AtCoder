#!/usr/bin/env python3
import math

N = int(input())
L = [list(map(int, input().split())) for l in range(N)]

result = []

for l in L:
    max = 0
    index = 0
    for j in range(N):
        cal = math.sqrt((l[0] - L[j][0]) ** 2 + (l[1] - L[j][1]) ** 2)
        if max < cal:
            max = cal
            index = j + 1
    result.append(index)

for r in result:
    print(r)
