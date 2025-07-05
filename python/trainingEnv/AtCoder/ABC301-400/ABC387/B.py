import io
import sys

_INPUT = """\
24
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())

#処理
out = 0
for i in range(1,10):
    for j in range(1,10):
        if i * j != N:
            out += i * j

#出力
print(out)