import io
import sys

_INPUT = """\
12.340
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
X = input()

#処理
out = X
while out[-1] == "0":
    out = out[:-1]
if out[-1] == ".":
    out = out[:-1]

#出力
print(out)