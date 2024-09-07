N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = A + B
A.sort()
B.sort()
C.sort()

if len(C) == 2:
    print("No")
    exit()

index = 0
count = 0

for i in C:
    if index > len(A) - 1:
        break
    if i == A[index]:
        count += 1
        index += 1
    else:
        count = 0
    if count == 2:
        print("Yes")
        exit()
print("No")
