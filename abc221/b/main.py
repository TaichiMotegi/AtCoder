#!/usr/bin/env python3
S = input()
T = input()

string = []

for s in S:
    string.append(s)

if S == T:
    print("Yes")
else:
    for i in range(len(S) - 1):
        swap = string.copy()
        swap[i] = S[i + 1]
        swap[i + 1] = S[i]
        if T == "".join(swap):
            print("Yes")
            exit()
    print("No")
