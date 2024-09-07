#!/usr/bin/env python3
N, P = map(int, input().split())
a = list(map(int, input().split()))

count = 0

for i in a:
    if i < P:
        count += 1

print(count)
