import io
import sys

_INPUT = """\
41
10
73 8 55 26 97 48 37 47 35 55
15
1
2
7
1
6
3
10
8
4
8
1
5
9
9
3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
X = int(input())
N = int(input())
list_W = [0] + list(map(int, input().split()))
Q = int(input())

have_parts = [False] * (N + 1)
out_weight = X

# 処理
for i in range(Q):
    P = int(input())

    out_weight += list_W[P] * ((-1) if have_parts[P] else 1)
    have_parts[P] = not have_parts[P]

    # 出力
    print(out_weight)
