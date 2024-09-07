#!/usr/bin/env python3

n, k, x = map(int, input().split())
a = list(map(int, input().split()))
    
    # Calculate the initial sum of array elements
ans = sum(a)
    
    # Calculate the maximum number of full x we can subtract
m = sum(ai // x for ai in a)
m = min(m, k)
ans -= m * x
k -= m
    
    # Reduce each element to its remainder when divided by x
a = [ai % x for ai in a]
a.sort()
    
    # Use up remaining k to subtract the largest possible remainders
for i in range(n - 1, -1, -1):
    if k == 0:
        break
    ans -= a[i]
    k -= 1
    
print(ans)
