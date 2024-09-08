#!/usr/bin/env python3
N, K = map(int, input().split())
S = [sum(map(int, input().split())) for _ in range(N)]
S_sorted = [10000] + sorted(S, reverse=True)
border = S_sorted[K]
for score in S:
    print("Yes" if score + 300 >= border else "No")
