import io
import sys

_INPUT = """\
10 3
0 3 4 6 9 12 15 17 19 20
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,C = map(int, input().split())
list_T = list(map(int, input().split()))

#処理
out = 0
before_T = -10000
for T in list_T:
    if T - before_T >= C:
        out += 1
        before_T = T

#出力
print(out)