import io
import sys

_INPUT = """\
10 8 14
5 20
14 21
9 21
5 23
8 10
0 14
3 8
2 6
0 16
5 20
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,L,R = map(int, input().split())

#処理
out = 0
for i in range(N):
    X, Y = map(int, input().split())
    if X <= L and Y >= R:
        out += 1

#出力
print(out)