#!/usr/bin/env python3
S = input()
T = input()

st = set()

for i in range(len(S)):
    k = (ord(T[i]) - ord(S[i]) + 26) % 26
    st.add(k)

if len(st) == 1:
    print("Yes")
else:
    print("No")
