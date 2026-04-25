import io
import sys

_INPUT = """\
6 6 6

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
A, B, C = map(int, input().split())

# 処理
out = "No"
if A != B and B == C:
    out = "Yes"

# 出力
print(out)
