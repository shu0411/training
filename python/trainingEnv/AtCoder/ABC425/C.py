import io
import sys

_INPUT = """\
5 7
1 2 4 8 16
2 1 5
1 4
1 5
2 1 5
2 2 4
1 1
2 3 3


"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int, input().split())
list_A = list(map(int, input().split()))

#処理
list_sum_A = [0] * (N + 1)
for i in range(1, N + 1):
    list_sum_A[i] = list_sum_A[i - 1] + list_A[i - 1]

diff = 0

for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        diff += query[1]
    else:
        l, r = query[1], query[2]
        real_l = (l + diff - 1) % N + 1
        real_r = (r + diff - 1) % N + 1
        out = 0
        if real_l <= real_r:
            out = list_sum_A[real_r] - list_sum_A[real_l - 1]
        else:
            out = list_sum_A[N] - list_sum_A[real_l - 1] + list_sum_A[real_r]

        #出力
        print(out)  