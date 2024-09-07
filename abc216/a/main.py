#!/usr/bin/env python3
X, Y = map(int, input().split("."))

if Y <=2:
    print(f"{X}-")
elif Y <= 6:
    print(X)
else:
    print(f"{X}+")