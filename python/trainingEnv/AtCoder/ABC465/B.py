import io
import sys

_INPUT = """\
900 200 12 14 11 13

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
X, Y, L, R, A, B = map(int, input().split())

# 処理
x_hours = max(0, min(R, B) - max(A, L))
out = X * x_hours + Y * (B - A - x_hours)

# 出力
print(out)
