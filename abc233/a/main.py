#!/usr/bin/env python3

H, N = map(int, input().split())
ans = 0

if H > N:
    print(0)
else:
    while H < N:
        H += 10
        ans += 1
    print(ans)
