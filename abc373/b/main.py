#!/usr/bin/env python3
S = input()
alp = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

ans = 0
for i in range(len(alp) - 1):  # 'Z'の次の文字は存在しないので、len(alp) - 1まで
    current_char = alp[i]
    next_char = alp[i + 1]

    index = S.find(current_char)
    if index == -1:  # 現在の文字が見つからない場合はスキップ
        continue

    next_index = S.find(next_char)
    if next_index == -1:  # 次の文字が見つからない場合はスキップ
        continue

    distance = abs(next_index - index)  # 絶対値を取ることで前後どちらの方向でも計算可能
    ans += distance

print(ans)
