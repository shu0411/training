import io
import sys

_INPUT = """\
4
8 2
1 10 10 1 1 10 10 1
8 3
1 10 10 1 1 10 10 1
8 4
1 10 10 1 1 10 10 1
4 100
100000 100000 100000 100000

"""
sys.stdin = io.StringIO(_INPUT)

# 初めに2W個のグループごとにCの合計を出す
# 累積和出す
# 各xに対して和を計算
# 最小が答え
#############ここから下をコピペ#############

# 入力
T = int(input())

# 処理
for _ in range(T):
    N, W = map(int, input().split())
    list_C = list(map(int, input().split()))

    W_2 = W * 2
    list_sum_C = [0] * W_2
    for i, C in enumerate(list_C):
        list_sum_C[i % W_2] += C

    # 累積和
    list_cumurative_sum_C = [0] * W_2
    for i, sum_group_C in enumerate(list_sum_C):
        list_cumurative_sum_C[i] = list_cumurative_sum_C[i - 1] + sum_group_C

    # 0番目からW-1番目を塗る
    out = list_cumurative_sum_C[W - 1]

    # x+1番目からx+W番目を塗る（0 <= x < W）
    for x in range(W):
        out = min(out, list_cumurative_sum_C[x + W] - list_cumurative_sum_C[x])

    # x+1番目からW*2番目と0番目からx-W番目を塗る（W <= x < W-2）
    for x in range(W, W_2):
        out = min(
            out,
            list_cumurative_sum_C[W_2 - 1]
            - list_cumurative_sum_C[x]
            + list_cumurative_sum_C[x - W],
        )

    # 出力
    print(out)
