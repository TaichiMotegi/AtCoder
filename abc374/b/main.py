#!/usr/bin/env python3
S = input()
T = input()
min = min(len(S), len(T))

if len(S) == len(T):
    for i in range(min):
        if S[i] != T[i]:
            print(i + 1)
            exit()
    print(0)
else:
    for i in range(min):
        if S[i] != T[i]:
            print(i + 1)
            exit()
    print(min + 1)
