#!/usr/bin/env python3

N = int(input())
L = [tuple(map(int, input().split())) for _ in range(N)]

a = set()
for i in range(len(L)):
    a.add(L[i])

print(len(a))
