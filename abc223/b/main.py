#!/usr/bin/env python3
S = input()

List = []

for i in range(len(S)):
    tmp = S[i:] + S[:i]
    List.append(tmp)

List.sort()

print(List[0])
print(List[-1])
