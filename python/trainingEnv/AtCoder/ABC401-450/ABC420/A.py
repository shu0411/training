import io
import sys

_INPUT = """\
12 12

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
X,Y = map(int, input().split())

#処理
out = (X + Y) % 12
if out == 0:
    out = 12

#出力
print(out)