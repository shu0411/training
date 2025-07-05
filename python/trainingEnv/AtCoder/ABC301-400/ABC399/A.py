import io
import sys

_INPUT = """\
8
chokudai
chokudai
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
S = input()
T = input()

#処理
out = 0
for i in range(N):
    if S[i] != T[i]:
        out += 1

#出力
print(out)