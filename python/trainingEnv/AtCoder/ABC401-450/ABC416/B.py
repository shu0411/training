import io
import sys

_INPUT = """\
#..#.

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
list_sharp = [0]
for i in range(len(S)):
    if S[i] == "#":
        list_sharp.append(i+1)

list_sharp.append(len(S) + 1)

list_o = []
for i in range(len(list_sharp) - 1):
    if list_sharp[i+1] - list_sharp[i] > 1:
        list_o.append(list_sharp[i] + 1)

out = ""
for i in range(len(S)):
    if i + 1 in list_o:
        out += "o"
    else:
        out += S[i]

#出力
print(out)