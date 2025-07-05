import io
import sys

_INPUT = """\
6 1
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
A,B = map(int, input().split())

#処理
if A == B:
    out = 1
elif (A - B) % 2 == 1:
    out = 2
else:
    out = 3

#出力
print(out)