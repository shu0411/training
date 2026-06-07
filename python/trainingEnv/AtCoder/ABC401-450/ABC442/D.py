import io
import sys

_INPUT = """\
4 4
2 7 1 8
1 2
2 1 2
1 1
2 2 4

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, Q = map(int, input().split())
list_A = [0] + list(map(int, input().split()))

# 処理
list_sum_A = [0] * (N + 1)
for i in range(N):
    list_sum_A[i + 1] = list_sum_A[i] + list_A[i + 1]

for _ in range(Q):
    list_query = list(map(int, input().split()))
    if list_query[0] == 1:
        x = list_query[1]
        Ax = list_A[x]
        Anext = list_A[x + 1]
        list_A[x + 1] = Ax
        list_A[x] = Anext
        list_sum_A[x] = list_sum_A[x] - Ax + Anext

    else:
        l = list_query[1]
        r = list_query[2]
        out = list_sum_A[r] - list_sum_A[l - 1]

        # 出力
        print(out)
