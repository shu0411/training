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

if len_T >= 2:
    w = len_S // len_T

    #w以下のiについて、Sのi番目からw文字おきにしゅとくした文字列がTと一致するか確認
    for i in range(w):
        if S[i::w] == T:
            out = "Yes"
            break

#出力
print(out)

#WAあり
#wで考慮不足あり