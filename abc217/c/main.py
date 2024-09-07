#!/usr/bin/env python3
N = int(input())
P = list(map(int, input().split()))

index_list = []
index = 1
ans = []

for p in P:
    index_list.append([p, index])
    index += 1

sort_list = sorted(index_list)

for num in sort_list:
    ans.append(num[1])

print(*ans)
