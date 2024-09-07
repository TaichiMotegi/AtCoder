#!/usr/bin/env python3
n, x, y, z = map(int, input().split())

if x < z and z < y:
    print("Yes")
elif y < z and z < x:
    print("Yes")
else:
    print("No")
