import io
import sys

_INPUT = """\
2
7 3
4 2
5
1 1
1 3
1 4
1 15
2 7
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_qr = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())


#処理
for i in range(Q):
    t,d = map(int, input().split())
    q,r = list_qr[t-1]
    if d % q <= r:
        out = d // q * q + r
    else:
        out = (d // q + 1) * q + r

    #出力
    print(out)
