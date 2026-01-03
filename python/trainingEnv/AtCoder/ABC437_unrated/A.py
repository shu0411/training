import io
import sys

_INPUT = """\
8 0
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
A, B = map(int, input().split())

# 処理
out = A * 12 + B

# 出力
print(out)
