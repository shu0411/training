import io
import sys

_INPUT = """\
6 7 17
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
A,B,C = map(int, input().split())

#処理
out = "No"
if B < C and (A < B or C < A):
    out = "Yes"
if C < B and (C < A < B):
    out = "Yes"

#出力
print(out)