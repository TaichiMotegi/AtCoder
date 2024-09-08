#!/usr/bin/env python3
S, T, X = map(int, input().split())
X = X + 0.5

if T < S:
    if (0 <= X <= T) or (S <= X <= 24):
        print("Yes")
    else:
        print("No")
else:
    if S <= X <= T:
        print("Yes")
    else:
        print("No")
