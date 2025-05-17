import io
import sys

_INPUT = """\
22 44 22 45

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
A,B,C,D = map(int, input().split())

#処理
out = "Yes"

if A < C:
    out = "No"
elif A == C:
    if B < D:
        out = "No"


#出力
print(out)