import io
import sys

_INPUT = """\
5
0 1 0 1 1
1 0 0 1 0
0 0 0 0 1
1 1 0 0 1
1 0 1 1 0
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
for i in range(N):
    list_A = list(map(int,input().split()))

    #処理
    out = ""
    for j in range(N):
        if list_A[j] == 1:
            out += str(j+1) + " "
    out = out[:-1]

    #出力
    print(out)