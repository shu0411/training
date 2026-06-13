import io
import sys

_INPUT = """\
98


"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import math

# 入力
D = int(input())

# 処理
r = D / 2
out = r * r * math.pi

# 出力
print(out)
