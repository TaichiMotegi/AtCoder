#!/usr/bin/env python3
N = int(input())
a = [list(map(int, input().split())) for _ in range(N - 1)]

hoge = 0
if a[0][0] == a[1][0] or a[0][0] == a[1][1]:
    hoge = a[0][0]
elif a[0][1] == a[1][0] or a[0][1] == a[1][1]:
    hoge = a[0][1]
else:
    print("No")
    exit()

for i in range(2, len(a)):
    if hoge == a[i][0] or hoge == a[i][1]:
        continue
    else:
        print("No")
        exit()
print("Yes")
