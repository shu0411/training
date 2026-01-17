import io
import sys

_INPUT = """\
5 5
10 104

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
P, Q = map(int, input().split())
X, Y = map(int, input().split())

# 処理
out = "Yes"
if X < P or X > P + 99 or Y < Q or Y > Q + 99:
    out = "No"

# 出力
print(out)
