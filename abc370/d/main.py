#!/usr/bin/env python3
H, W, Q = map(int, input().split())
xy = [map(int, input().split()) for _ in range(Q)]
x, y = [list(i) for i in zip(*xy)]

board = [[1] * W for _ in range(H)]

for i in range(Q):
    a = x[i] - 1
    b = y[i] - 1
    if board[a][b] == 1:
        board[a][b] = 0
    else:
        if 0 <= a - 1:
            board[a - 1][b] = 0
        elif a + 1 <= W - 1:
            board[a + 1][b] = 0
        elif 0 <= b - 1:
            board[a][b] = 0
        elif b + 1 <= H - 1:
            board[a][b + 1] = 0
    print(board)

ans = 0
for i in board:
    ans += i.count(1)
print(ans)
