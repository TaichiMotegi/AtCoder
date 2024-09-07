N, T = map(int, input().split())
A = list(map(int, input().split()))

row_count = [0] * N
col_count = [0] * N
main_diag_count = 0
anti_diag_count = 0
turn = 0

for a in A:
    turn += 1

    i = (a - 1) // N
    j = (a - 1) % N

    row_count[i] += 1
    col_count[j] += 1

    if i == j:
        main_diag_count += 1
    if i + j == N - 1:
        anti_diag_count += 1

    if row_count[i] == N or col_count[j] == N or main_diag_count == N or anti_diag_count == N:
        print(turn)
        exit()

print(-1)
