import io
import sys

_INPUT = """\
4 10 14
5 8
5 6
7 9
99 99
"""
sys.stdin = io.StringIO(_INPUT)

#N=敵の数、H=体力、M=魔力、A=敵の体力、B=敵の魔力
#############ここから下をコピペ#############

#入力
N,H,M = map(int, input().split())

#初期化
dp = [[[(0,0)] * (M + 1) for _ in range(H + 1)] for _ in range(N + 1)]

#処理
for i in range(1, N + 1):
    a, b = map(int, input().split())
    for j in range(H + 1):
        for k in range(M + 1):
            #体力を使う場合
            if j >= a:
                tmp_j = dp[i - 1][j - a][k][0] + j
            #魔力を使う場合
            if k >= b:
                tmp_k = dp[i - 1][j][k - b][1] + k
            dp[i][j][k] = max(dp[i - 1][j][k], (tmp_j, tmp_k))
