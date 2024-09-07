#!/usr/bin/env python3
import math

S = input()

count = 0
if S[0] == S[1] and S[0] == S[2]:
    count = 3
elif S[0] == S[1] or S[0] == S[2]:
    count = 2
elif S[1] == S[2]:
    count = 2

print(math.factorial(3) // math.factorial(count))
