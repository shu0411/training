import io
import sys

_INPUT = """\
6 6
3 2 5 9 1 2
2
4 5
5
1 2 3 4 6
3
2 5 6
4
1 2 5 6
1
5
3
1 2 3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, Q = map(int, input().split())
list_A = list(map(int, input().split()))


# 処理
list_tuple_min_A_6 = [(10**9, -1)] * 6
for i, A in enumerate(list_A):
    if A < list_tuple_min_A_6[5][0]:
        list_tuple_min_A_6[5] = (A, i)
        list_tuple_min_A_6.sort()

for _ in range(Q):
    K = int(input())
    list_B = list(map(int, input().split()))

    list_tuple_removed = []
    for tuple_min_A in list_tuple_min_A_6:
        for B in list_B:
            if B - 1 == tuple_min_A[1]:
                break
        else:
            out = tuple_min_A[0]
            break

    # 出力
    print(out)
