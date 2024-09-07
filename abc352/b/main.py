#!/usr/bin/env python3
S = input()
T = input()

index_list = []
point = 0

for s in S:
    for _ in range(len(T)):
        if s == T[point]:
            index_list.append(point + 1)
            point += 1
            break
        point += 1

print(*index_list)
