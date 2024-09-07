N = int(input())
A = list(map(int, input().split()))
v = []

for i in range(N):
    v.append((A[i], i + 1))

v.sort(reverse=True)
print(v[1][1])
