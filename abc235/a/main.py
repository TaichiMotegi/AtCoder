#!/usr/bin/env python3
N = input()
a = N[0]
b = N[1]
c = N[2]
ans = int(a + b + c) + int(b + c + a) + int(c + a + b)
print(ans)
