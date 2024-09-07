#!/usr/bin/env python3
X = input()
N = int(input())
S = [input() for _ in range(N)]

ans = []
sort_ans = []

alp = "abcdefghijklmnopqrstuvwxyz"

for s in S:
    name = ""
    for i in range(len(s)):
        index = X.index(s[i])
        name += alp[index]
    ans.append(name)

ans = sorted(ans)

for a in ans:
    name = ""
    for i in range(len(a)):
        index = alp.index(a[i])
        name += X[index]
    sort_ans.append(name)

for a in sort_ans:
    print(a)
