#!/usr/bin/env python3
# 入力を読み込む
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append((v, w))
    G[v].append((u, -w))

visited = [False] * N  # 値が確定しているかどうか
ans = [0] * N  # 書き込む値
for i in range(N):
    # すでに値が確定しているならばスキップ
    if visited[i]:
        continue
    # 頂点 i の値を 0 に確定し，探索を始める
    st = [i]
    visited[i] = True
    while st:
        # いま頂点 u にいる
        u = st.pop()
        # 頂点 u に隣接する頂点 v を調べる
        for v, w in G[u]:
            if not visited[v]:
                # まだ頂点 v の値が確定していないならば，頂点 u の値と整合的になるように，頂点 v の値を確定させる
                visited[v] = True
                ans[v] = ans[u] + w
                st.append(v)
print(*ans)
