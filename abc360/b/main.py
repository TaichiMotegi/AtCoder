#!/usr/bin/env python3

S,T = input().split()

for w in range(1, len(S)):
  # 文字を見始める位置
  for c in range(0, w):
    # 一時的に文字を格納する場所
    tmp = []
    # 文字を取得する位置
    i = c
    # 文字を取得できる範囲内の時，
    while i<len(S):
      # 文字をリストに追加する．
      tmp.append(S[i])
      # 文字を参照する位置を進める．
      i += w
    
    # リストの文字列とTが合致するかどうか．
    if("".join(tmp)==T):
      # 合致したら，Yesを出力して，プログラムを終了させる．
      print("Yes")
      exit()
# 一度も合致しなければ，Noを出力して終了させる．
print("No")


