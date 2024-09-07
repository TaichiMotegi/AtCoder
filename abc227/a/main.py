#!/usr/bin/env python3
N, K, A = map(int, input().split())

order = []

for i in range(A, N + 1):
    order.append(i)

for j in range(1, A):
    order.append(j)

# print(order)

if N % K == 0:
    print(order[-1])
else:
    print(order[K % N - 1])
