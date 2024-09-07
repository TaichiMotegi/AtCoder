#!/usr/bin/env python3
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

need = [0] * N
need[N - 1] = 1
res = 0
for i in range(N)[::-1]:
    if need[i]:
        res += A[i][0]
        if A[i][1] == 0:
            continue
        for x in A[i][2:]:
            need[x - 1] = 1

print(res)
