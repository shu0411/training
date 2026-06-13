import io
import sys

_INPUT = """\
abcde
XYZ

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()
T = input()

#処理
out = "Yes"
before_s = S[0]

for i in range(1,len(S)):
    if S[i] == S[i].upper() and before_s not in T:
        out = "No"
        break
    before_s = S[i]

#出力
print(out)