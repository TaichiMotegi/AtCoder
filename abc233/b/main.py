#!/usr/bin/env python3
L, R = map(int, input().split())
S = input()

hoge = []
count = 0
for i in range(len(S)):
    if L <= i + 1 <= R:
        hoge.append(S[R - 1 - count])
        count += 1
    else:
        hoge.append(S[i])

print("".join(hoge))
