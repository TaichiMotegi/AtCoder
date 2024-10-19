#!/usr/bin/env python3
import math

N = int(input())
dot = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(i + 1, N):
        if ans < math.sqrt((dot[i][0] - dot[j][0]) ** 2 + (dot[i][1] - dot[j][1]) ** 2):
            ans = math.sqrt((dot[i][0] - dot[j][0]) ** 2 + (dot[i][1] - dot[j][1]) ** 2)
print(ans)
