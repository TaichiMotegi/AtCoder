#!/usr/bin/env python3
import itertools
import math

N, K = map(int, input().split())
S = input()
dic = set()
count = 0

if len(set(S)) == N:
    print(math.factorial(N))
    exit()

for word in itertools.permutations(S):
    text = "".join(map(str, word))
    dic.add(text)


for text in dic:
    for i in range(N):
        normal = text[i : i + K]
        if len(normal) < K:
            break
        reversed = normal[::-1]
        if normal == reversed:
            count += 1
            break

print(len(dic) - count)
