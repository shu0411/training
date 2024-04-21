import io
import sys

_INPUT = """\
ABC000
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
out = "No"
if S[0:3] == "ABC"and int(S[3:6]) >= 1 and int(S[3:6]) <= 349 and S[3:6] != "316":
    out = "Yes"

#出力
print(out)