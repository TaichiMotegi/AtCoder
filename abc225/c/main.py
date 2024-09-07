#!/usr/bin/env python3
N, M = map(int, input().split())

b = [list(map(int, input().split())) for _ in range(N)]

for col in range(M):
    if b[0][col] % 7 == 0 and col != M - 1:
        print("No")
        exit()

for i in range(N - 1):
    if b[i + 1][0] - b[i][0] == 7:
        continue
    else:
        print("No")
        exit()

for i in b:
    for j in range(M - 1):
        if i[j + 1] - i[j] == 1:
            continue
        else:
            print("No")
            exit()
print("Yes")
