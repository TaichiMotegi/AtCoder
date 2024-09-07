#!/usr/bin/env python3
import math

N = int(input())

a = [list(map(int, input().split())) for _ in range(N)]
sorted_a = sorted(a)

count = 0

for i in range(len(sorted_a) - 2):
    for j in range(i + 1, len(sorted_a) - 1):
        for k in range(j + 1, len(sorted_a)):
            hoge = (sorted_a[k][0] - sorted_a[i][0]) * (sorted_a[j][1] - sorted_a[i][1])
            fuga = (sorted_a[j][0] - sorted_a[i][0]) * (sorted_a[k][1] - sorted_a[i][1])
            if hoge == fuga:
                count += 1

print(math.comb(N, 3) - count)
