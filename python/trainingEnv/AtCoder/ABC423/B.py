import io
import sys

_INPUT = """\
8
0 0 1 1 0 1 0 0

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_L = list(map(int, input().split()))

#処理
out = N - 1

if list_L.count(1) <= 1:
    out = 0
else:
    for i in range(N-1):
        if list_L[i] == 0:
            out -= 1
        else:
            break
    for i in range(N-1, 0, -1):
        if list_L[i] == 0:
            out -= 1
        else:
            break

#出力
print(out)