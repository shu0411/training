import io
import sys

_INPUT = """\
1 b a
b
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,c1,c2 = input().split()
S = input()

#処理
out = ""
for s in S:
    if s == c1:
        out += s
    else:
        out += c2

#出力
print(out)