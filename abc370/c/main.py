#!/usr/bin/env python3
S = input()
T = input()


if S == T:
    print(0)
    exit()

S_list = [s for s in S]
T_list = [t for t in T]

ans = []
for i in range(len(S)):
    if S_list[i] == T_list[i]:
        continue
    elif S_list[i] < T_list[i]:
        continue
    elif i == len(S) - 1:
        S_list[i] = T_list[i]
        ans.append("".join(S_list))
    else:
        S_list[i] = T_list[i]
        ans.append("".join(S_list))

if "".join(S_list) == T:
    print(len(ans))
    for i in ans:
        print(i)
else:
    for i in range(len(S) - 1, -1, -1):
        if S_list[i] == T_list[i]:
            continue
        else:
            S_list[i] = T_list[i]
            ans.append("".join(S_list))
    print(len(ans))
    for i in ans:
        print(i)
