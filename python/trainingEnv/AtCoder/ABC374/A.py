import io
import sys

_INPUT = """\
aokikun
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
if S[-3:] == "san":
    out = "Yes"
else:
    out = "No"

#出力
print(out)