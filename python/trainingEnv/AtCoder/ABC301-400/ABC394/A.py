import io
import sys

_INPUT = """\
22222000111222222

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
out = ""
for s in S:
    if s == "2":
        out += "2"


#出力
print(out)