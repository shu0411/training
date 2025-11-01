import io
import sys

_INPUT = """\
100 100 1 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
A, B, C, D = map(int, input().split())

# 処理
out = "No"
if A <= C and B > D:
    out = "Yes"

# 出力
print(out)
