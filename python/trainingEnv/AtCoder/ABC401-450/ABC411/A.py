import io
import sys

_INPUT = """\
atcode
7
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
P = input()
L = int(input())

#処理
out = "No"
if len(P) >= L:
    out = "Yes"


#出力
print(out)