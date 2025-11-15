import io
import sys

_INPUT = """\
8 10
320 578 244 604 145 839 156 857
2 400 556
1 5 168
2 254 62
2 145 301
1 1 23
1 3 0
2 413 758
2 297 613
1 8 451
2 598 692

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, Q = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
# Aの個数と合計の累積和
list_count_A = [0] * (5 * 10**5 + 1)
list_sum_A = [0] * (5 * 10**5 + 1)
for A in list_A:
    list_count_A[A] = 1
    list_sum_A[A] = A

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, x, y = query
        minus_num = list_A[x - 1]
        list_count_A[minus_num] -= 1
        list_count_A[y] += 1
        list_sum_A[minus_num] -= minus_num
        list_sum_A[y] += y

    else:
        _, l, r = query
        out = 0
        if l >= r:
            out = l * N
        else:
            count_l = sum(list_count_A[: (l + 1)])
            count_r = sum(list_count_A[r:])
            out = l * count_l + r * count_r + sum(list_sum_A[(l + 1) : r])

        # 出力
        print(out)
