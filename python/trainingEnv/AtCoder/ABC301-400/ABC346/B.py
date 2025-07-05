import io
import sys

_INPUT = """\
92 66
"""
sys.stdin = io.StringIO(_INPUT)

#S1周の中でwは7個、bは5個
#W,B<=100なので、最大20周までしか行かない
#①１周内で完結する
#②１周目の途中で始まり、２周目で完結する
#③３周以上
#①のために、Sの途中から途中までのw,bの数を数える
#②のために、Sの途中から最後までのw,bの数を数え、Sの最初から途中までのw,bの数を数える
#③は②に加えて、Sの最初から最後までのw,bの数を数える
#→③はWから7*N、Bから5*Nを引いたら②と同じ。そのうえで2周分を全探索。
#############ここから下をコピペ#############
#入力
W,B = map(int, input().split())

#処理
out = "No"
S = "wbwbwwbwbwbwwbwbwwbwbwbw"

#W >=14 and B >= 10の場合、Wから7*N、Bから5*Nを引いても結果は同じ
if W >= 14 and B >= 10:
    tmp_Nw = W // 7
    tmp_Nb = B // 5
    N = min(tmp_Nw, tmp_Nb)
    W -= 7 * N
    B -= 5 * N

for i in range(len(S)):
    for j in range(i, len(S)):
        if W == S[i:j].count("w") and B == S[i:j].count("b"):
            out = "Yes"
            break

#出力
print(out)