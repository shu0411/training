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
dp = [[0] * (H + 1) for _ in range(N + 1)]  #dp[i][j]はi番目までの敵を倒したときの体力jでの最大魔力

#処理
for i in range(1, N + 1):
    a, b = map(int, input().split())
    for j in range(H + 1):
        if j >= a:
            dp[i][j] = max(dp[i-1][j - a], dp[i - 1][j] + b)
        else:
            dp[i][j] = dp[i - 1][j]
    print(dp[i])  # デバッグ用に各ステップのdpテーブルを出力
#出力
ans = max(dp[N][j] for j in range(H + 1) if j <= M)
print(ans)

#途中。もうちょっと考える。