import io
import sys

_INPUT = """\
verticalreading agh
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S,T = input().split()

#処理
out = "No"
len_S = len(S)
len_T = len(T)

for w in range(1, len_S):
    #w以下のiについて、Sのi番目からw文字おきに取得した文字列がTと一致するか確認
    for i in range(w):
        if S[i::w] == T:
            out = "Yes"
            break

#出力
print(out)
