#!/usr/bin/env python3
n = int(input())

A = []
B = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

time = 0
for i in range(n):
    tmp = A[i] / B[i]
    time += tmp
time /= 2

ans = 0
for i in range(n):
    if A[i] / B[i] <= time:
        ans += A[i]
        time -= A[i] / B[i]
        print(f"ans:{ans}")
        print(f"time:{time}")
    else:
        ans += B[i] * time
        print(f"ans:{ans}")
        break

print(ans)
