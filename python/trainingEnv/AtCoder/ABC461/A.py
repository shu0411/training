import io
import sys

_INPUT = """\
6 5

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
A,D = map(int,input().split())

# 処理
out = "No"
if A <= D:
    out = "Yes"

# 出力
print(out)
