import io
import sys

_INPUT = """\
10 10 10

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
a,b,c = map(int, input().split())

#処理
out = "No"

if a == b or b == c or a == c:
    out = "Yes"

#出力
print(out)