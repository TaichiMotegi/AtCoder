A, B = map(int, input().split())

hannin = {1,2,3}
candidate = set()
candidate.add(A)
candidate.add(B)

if A == B:
    print(-1)
else:
    shinhannin = hannin-candidate
    for x in shinhannin:
        print(x)
