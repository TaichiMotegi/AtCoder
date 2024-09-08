#!/usr/bin/env python3
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

previousNum = 1
for i in range(1, N + 1):
    if previousNum < i:
        previousNum = A[i - 1][previousNum - 1]
    else:
        previousNum = A[previousNum - 1][i - 1]

print(previousNum)
