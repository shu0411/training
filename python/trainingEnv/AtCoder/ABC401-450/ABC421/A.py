import io
import sys

_INPUT = """\
2
wang
li
2 wang

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_S = [input() for _ in range(N)]
X, Y = input().split()

#処理
out = "No"
if list_S[int(X)-1] == Y:
    out = "Yes"

#出力
print(out)