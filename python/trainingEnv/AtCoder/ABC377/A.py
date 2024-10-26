import io
import sys

_INPUT = """\
AAC
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
if "A" in S and "B" in S and "C" in S:
    out = "Yes"
else:
    out = "No"

#出力
print(out)