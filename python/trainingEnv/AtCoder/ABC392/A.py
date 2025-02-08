import io
import sys

_INPUT = """\
3 3 9
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
A1, A2, A3 = map(int, input().split())

#処理
out = "No"

if A1 * A2 == A3 or A1 * A3 == A2 or A2 * A3 == A1:
    out = "Yes"

#出力
print(out)