import io
import sys

_INPUT = """\
30
011011100101110111100010011010
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
T = input()

#処理
dp = [[0,0]] * (N + 1)
for i in range(1, N + 1):
    if T[i - 1] == '0':
        dp[i] = [dp[i - 1][1], dp[i - 1][0] + 1]
    else:
        dp[i] = [dp[i - 1][0] + 1, dp[i - 1][1]]

out = sum(dp[i][0] for i in range(1, N + 1))

#出力
print(out)