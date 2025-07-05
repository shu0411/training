import io
import sys

_INPUT = """\
99 12 50
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,T,A = map(int,input().split())

#処理
out = "No"
left = N - T - A
if T > A and T > A + left:
    out = "Yes"
if T < A and A > T + left: 
    out = "Yes"

#出力
print(out)