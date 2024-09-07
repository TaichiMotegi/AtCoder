#!/usr/bin/env python3
N = list(map(int, input().split()))

alp = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
ans = ""

for i in range(len(N)):
    ans += alp[N[i] - 1]

print(ans)
