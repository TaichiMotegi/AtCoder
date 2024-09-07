#!/usr/bin/env python3
K = int(input())
A, B = input().split()

A = A[::-1]
A = str(A)
B = B[::-1]
B = str(B)
ten_a = 0
ten_b = 0


def calc_ten(k, number):
    ans = 0
    for i in range(len(number)):
        if i == 0:
            ans += int(number[i])
        else:
            ans += int(number[i]) * k**i
    return ans


ten_a = calc_ten(K, A)
ten_b = calc_ten(K, B)
print(ten_a * ten_b)
