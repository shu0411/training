import io
import sys

_INPUT = """\
5
5 10 2 3
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_D = list(map(int, input().split()))

#処理
for i in range(N-1):
    out = []
    dist = list_D[i]
    out.append(dist)
    for j in range(i + 1, N-1):
        dist += list_D[j]
        out.append(dist)

    #出力
    print(*out)