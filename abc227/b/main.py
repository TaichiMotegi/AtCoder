#!/usr/bin/env python3
N = int(input())
S = map(int, input().split())
ans = 0

for s in S:
    flag = False
    for i in range(1, 334):
        for j in range(1, 334):
            if s == 4 * i * j + 3 * i + 3 * j:
                flag = True
                break
    if not flag:
        ans += 1

print(ans)
