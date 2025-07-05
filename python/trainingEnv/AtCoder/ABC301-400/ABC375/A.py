import io
import sys

_INPUT = """\
9
##.#.#.##
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
S = input()

#処理
out = 0
for i in range(N-2):
    if S[i] == "#" and S[i+2] == "#" and S[i+1] != "#":
        out += 1 

#出力
print(out)