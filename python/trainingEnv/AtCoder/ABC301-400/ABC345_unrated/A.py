import io
import sys

_INPUT = """\
<===>>
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
out = "No"
if S[0] == "<" and S[-1] == ">":
    for i in range(1,len(S)-1):
        if S[i] != "=":
            break
    else:
        out = "Yes"

#出力
print(out)