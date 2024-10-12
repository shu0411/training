import io
import sys

_INPUT = """\
XYYXYYXYXXX
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
len_S = len(S)
out = 0
for i in range(len_S - 2):
    si = S[i]
    for j in range(i+2, len_S):
        sj = S[j]
        if si == sj:
            out += j - i - 1

#出力
print(out)