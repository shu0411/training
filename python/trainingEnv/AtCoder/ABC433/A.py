import io
import sys

_INPUT = """\
50 5 10

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
X, Y, Z = map(int, input().split())

# 処理
out = "No"
add = 0
while X + add >= (Y + add) * Z:
    if X + add == (Y + add) * Z:
        out = "Yes"
    add += 1

# 出力
print(out)
