import io
import sys

_INPUT = """\
2 2 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import math

# 入力
X1, X2, X3 = map(int, input().split())

# 処理
out = 0
for i in range(1, X2 + 1):
    x3_area = i
    x1_area = X2 + 1 - i
    out += (
        math.factorial(X3)
        // math.factorial(x3_area)
        * (X3 - x3_area) ** (x3_area)
        * math.factorial(X1)
        // math.factorial(x1_area)
        * (X1 - x1_area) ** (x1_area)
    )


# 出力
print(out)
