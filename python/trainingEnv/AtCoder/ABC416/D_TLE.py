import io
import sys

_INPUT = """\
3
3 6
3 1 4
2 0 1
1 1000000000
999999999
999999999
10 201
144 150 176 154 110 187 38 136 111 46
96 109 73 63 85 1 156 7 13 171
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
T = int(input())

#処理
for i in range(T):
    N,M = map(int, input().split())
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split()))

    list_A.sort()
    list_B.sort(reverse=True)

    out = 0
    for B in list_B:
        left = M - B
        for A in list_A:
            if A >= left:
                out += (B + A) % M
                list_A.remove(A)
                break
        else:
            A = list_A.pop()
            out += (B + A) % M

    #出力
    print(out)
