import io
import sys

_INPUT = """\
666 999

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
A, B = map(int, input().split())

# 処理
out = "No"
if A > B / 3 * 2:
    out = "Yes"

# 出力
print(out)
