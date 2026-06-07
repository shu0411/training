import io
import sys

_INPUT = """\
5 4
2 1 3 3 1
2 4
1 4
1 5
3 3

"""
sys.stdin = io.StringIO(_INPUT)

#1～Nまでを1回ずつ足したものを保持。
#1-Nのときの結果を保持。

#############ここから下をコピペ#############

#入力
N,Q = map(int, input().split())
list_A = list(map(int, input().split()))

#処理
for _ in range(Q):
    out = 0
    L,R = map(int, input().split())
    range_length = R - L + 1
    a = 1
    b = range_length
    for A in list_A[L-1:R]:
        out += A * a * b
        a += 1
        b -= 1

    #出力
    print(out)