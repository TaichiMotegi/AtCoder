#!/usr/bin/env python3
import math

N = int(input())
dot = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(i + 1, N):
        if ans < math.sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2):
            ans = math.sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2)
print(ans)
