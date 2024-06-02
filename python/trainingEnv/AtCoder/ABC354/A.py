import io
import sys

_INPUT = """\
262144
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
H = int(input())

#処理
i = 0
height = 0
while True:
    height += 2 ** i
    i += 1
    if height > H:
        break

#出力
print(i)