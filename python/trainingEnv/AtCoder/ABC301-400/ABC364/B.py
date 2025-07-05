import io
import sys

_INPUT = """\
6 6
1 1
.#####
######
######
######
######
######
RURLDLULLRULRDL
"""
sys.stdin = io.StringIO(_INPUT)

#上からi行、左からj列目の座標は(i,j)とする。
#.=移動可能、#=移動不可能

#############ここから下をコピペ#############

#入力
H,W = map(int, input().split())
Si,Sj = map(int, input().split())
tableC = [input() for _ in range(H)]
X = input()

#処理
tmp_i,tmp_j = Si-1,Sj-1 #今いる座標

for x in X:
    if x == "U" and tmp_i > 0 and tableC[tmp_i-1][tmp_j] == ".": #上に移動
        tmp_i -= 1
    elif x == "D" and tmp_i < H-1 and tableC[tmp_i+1][tmp_j] == ".": #下に移動
        tmp_i += 1
    elif x == "L" and tmp_j > 0 and tableC[tmp_i][tmp_j-1] == ".": #左に移動
        tmp_j -= 1
    elif x == "R" and tmp_j < W-1 and tableC[tmp_i][tmp_j+1] == ".": #右に移動
        tmp_j += 1

#出力
print(tmp_i+1,tmp_j+1)  #1-indexに直して出力