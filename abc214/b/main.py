#!/usr/bin/env python3
S, T = map(int, input().split())

result = 0

for i in range(101):
    for j in range(101):
        for k in range(101):
            total = i + j + k
            product = i * j * k
            if total <= S and product <= T:
                result += 1

print(result)
