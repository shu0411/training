import io
import sys

_INPUT = """\
43 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
H, B = map(int, input().split())

# 処理
out = H - B
if out < 0:
    out = 0

# 出力
print(out)
