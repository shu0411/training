import io
import sys

_INPUT = """\
6 16
0 8 0 2 6 8

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
out = "No"

sum_A = sum(list_A)
diff = sum_A - M
for A in list_A:
    if A == diff:
        out = "Yes"
        break

# 出力
print(out)
