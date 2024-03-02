#004 - Cross Sum（★2）
#問題URL:https://atcoder.jp/contests/typical90/tasks/typical90_d
import io
import sys

_INPUT = """\
3 3
1 1 1
1 1 1
1 1 1
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
H,W = map(int,input().split())

#処理
#行ごとの合計のリスト
sum_row = []
#列ごとの合計のリスト
sum_col = [0] * W

for i in range(H):
    #入力
    list_A = list(map(int,input().split()))
    #行の合計を求める
    sum_row.append(sum(list_A))
    #列の合計を求める
    for j in range(W):
        sum_col[j] += list_A[j]

#出力
for i in range(H):
    for j in range(W):
        print(sum_row[i] + sum_col[j] - list_A[j], end=" ")
    print()