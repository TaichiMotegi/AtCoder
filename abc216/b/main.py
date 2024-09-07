#!/usr/bin/env python3
N = int(input())
L = [list(input().split()) for _ in range(N)]

for i in range(len(L)):
    l_1 = L[i]
    for j in range(i+1,len(L)):
        l_2 = L[j]
        if l_1[0] == l_2[0] and l_1[1] == l_2[1]:
            print("Yes")
            exit()
print("No")