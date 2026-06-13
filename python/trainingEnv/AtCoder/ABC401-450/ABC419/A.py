import io
import sys

_INPUT = """\
atcoder

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
out = "Unknown"

if S == "red":
    out = "SSS"
elif S == "blue":
    out = "FFF"
elif S == "green":
    out = "MMM"

#出力
print(out)