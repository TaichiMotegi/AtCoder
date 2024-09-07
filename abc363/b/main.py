#!/usr/bin/env python3
N, T, P = map(int, input().split())
L = list(map(int, input().split()))

count = 0
day = 0

while True:
    for l in L:
        if T <= l:
            count += 1
    if P <= count:
        print(day)
        exit()
    else:
        count = 0
        day += 1
        L = [l + 1 for l in L]
