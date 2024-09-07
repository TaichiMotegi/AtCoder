#!/usr/bin/env python3
n, k = map(int, input().split())
a = list(map(int, input().split()))

data = set()

ans = (k * (k + 1)) // 2

for i in a:
    if k < i:
        continue
    else:
        data.add(i)


ans = ans - sum(data)

print(ans)
