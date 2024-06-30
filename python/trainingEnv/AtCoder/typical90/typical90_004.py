#004 - Cross Sum（★2）
#問題URL:https://atcoder.jp/contests/typical90/tasks/typical90_d
import io
import sys

_INPUT = """\
10 10
83 86 77 65 93 85 86 92 99 71
62 77 90 59 63 76 90 76 72 86
61 68 67 79 82 80 62 73 67 85
79 52 72 58 69 67 93 56 61 92
79 73 71 69 84 87 98 74 65 70
63 76 91 80 56 73 62 70 96 81
55 75 84 77 86 55 96 79 63 57
74 95 82 95 64 67 84 64 93 50
87 58 76 78 88 84 53 51 54 99
82 60 76 68 89 62 76 86 94 89
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
H,W = map(int,input().split())

#処理
#テーブルの作成
table = []
#行ごとの合計のリスト
sum_row = []
#列ごとの合計のリスト
sum_col = [0] * W

for i in range(H):
    #入力
    list_A = list(map(int,input().split()))
    #テーブルに追加
    table.append(list_A)
    #行の合計を求める
    sum_row.append(sum(list_A))
    #列の合計を求める
    for j in range(W):
        sum_col[j] += list_A[j]

#出力
for i in range(H):
    for j in range(W):
        print(sum_row[i] + sum_col[j] - table[i][j], end=" ")
    print()