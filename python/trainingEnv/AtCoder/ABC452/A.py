import io
import sys

_INPUT = """\
11 7

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
M, D = map(int, input().split())

# 処理
out = "No"
if (M == 1 and D == 7) or (M in [3, 5, 7, 9] and D == M):
    out = "Yes"

# 出力
print(out)
