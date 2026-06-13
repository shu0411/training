import io
import sys

_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())

#処理
out = 0

for i in range(1, N + 1):
    out += ((-1) ** i) * (i ** 3) 

#出力
print(out)