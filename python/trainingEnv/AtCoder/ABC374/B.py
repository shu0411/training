import io
import sys

_INPUT = """\
abcde
abcdef
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()
T = input()

#処理
min_len = min(len(S), len(T))

for i in range(1, min_len+1):
    if S[i-1] != T[i-1]:
        print(i)
        break
else:
    if len(S) != len(T):
        print(min_len+1)
    else:
        print("0")