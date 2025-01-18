import io
import sys

_INPUT = """\
2432902008176640000
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
X = int(input())

#処理
N = 0
while True:
    N += 1
    next_X = X / N
    if next_X == 1:
        out = N
        break
    else:
        X = next_X

#出力
print(out)