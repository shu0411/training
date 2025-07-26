import io
import sys

_INPUT = """\
9 6 8
xoxxoxoox

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,L,R = map(int, input().split())
list_S = input()

#処理
out = "Yes"
for i in range(L,R+1):
    if list_S[i-1] != "o":
        out = "No"
        break

#出力
print(out)