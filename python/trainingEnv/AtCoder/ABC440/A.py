import io
import sys

_INPUT = """\
432 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
X, Y = map(int, input().split())

# 処理
out = X
for _ in range(Y):
    out *= 2

# 出力
print(out)
