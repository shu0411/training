import io
import sys

_INPUT = """\
SMR
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
out = "No"
if S[0] == "R" or S[2] == "M":
    out = "Yes"

#出力
print(out)
