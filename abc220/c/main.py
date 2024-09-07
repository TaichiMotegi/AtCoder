#!/usr/bin/env python3
N = int(input())
A = list(map(int, input().split()))
X = int(input())

sum = sum(A)
count = len(A)
total = 0
total_2 = 0
ans = 0

total = X % sum
ans = (X // sum) * count

while True:
    for i in A:
        total_2 += i
        ans += 1
        if total < total_2:
            print(ans)
            exit()
