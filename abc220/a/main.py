#!/usr/bin/env python3
A, B, C = map(int, input().split())

for i in range(1000):
    if A <= i * C and i * C <= B:
        print(i * C)
        exit()
print("-1")
