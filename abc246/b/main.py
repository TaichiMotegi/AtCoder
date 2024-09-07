#!/usr/bin/env python3
N, K, X = map(int, input().split())
L = list(map(int, input().split()))
index = 0
L.sort(reverse=True)

for i in range(K):
    L[index] = max(L[index] - X,0)
    if L[index] < X:
        index += 1

print(sum(L))
