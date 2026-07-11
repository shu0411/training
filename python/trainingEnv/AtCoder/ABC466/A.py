import io
import sys

_INPUT = """\
4
0 -2 0 -1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_X = list(map(int, input().split()))

# 処理
out = "Yes"
for x in list_X:
    if x >= 0:
        out = "No"
        break

# 出力
print(out)
