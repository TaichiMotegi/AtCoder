#!/usr/bin/env python3
a = [list(map(int, input().split())) for l in range(3)]

result = []

if a[0][0] == a[1][0]:
    result.append(a[2][0])
elif a[0][0] == a[2][0]:
    result.append(a[1][0])
else:
    result.append(a[0][0])

if a[0][1] == a[1][1]:
    result.append(a[2][1])
elif a[0][1] == a[2][1]:
    result.append(a[1][1])
else:
    result.append(a[0][1])

print(*result)