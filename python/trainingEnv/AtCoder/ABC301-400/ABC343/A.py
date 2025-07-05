import io
import sys

_INPUT = """\
0 0
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
A,B = map(int,input().split())

#処理
if A+B != 0:
    out = 0
else:
    out = 1

#出力
print(out)