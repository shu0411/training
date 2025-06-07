import io
import sys

_INPUT = """\
5
xxxxx
ooooo

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
T = input()
A = input()

#処理
out = 'No'
for i in range(N):
    if T[i] == 'o' and A[i] == 'o':
        out = 'Yes'
        break

#出力
print(out)