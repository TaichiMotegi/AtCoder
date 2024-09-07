#!/usr/bin/env python3
S = input()

if S[0] == "M":
    print("No")
elif S[1] == "M":
    if S[0] == "R":
        print("Yes")
    else:
        print("No")
else:
    if S[0] == "R" or S[1] == "R":
        print("Yes")
    else:
        print("No")
