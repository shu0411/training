import io
import sys

_INPUT = """\
10 4 500 1
1 1 2 2 3 3 10 53 62 92
1 35 7 3 6 41 301 1508 81 410
602 36194 10116 40979 64284 75533 12003 1765292 267914 3899271
1839400 329448 26189909 33974926 5891756 1421171 12292679 41028554 139990581 275068707
132216460 9181343341 9984102563 13582229907 1792432832 6385549416 37389960078 267857279906 28408285981 76041334954

"""
sys.stdin = io.StringIO(_INPUT)

# 579,628,028点 585位相当
#############ここから下をコピペ#############
import copy

# 入力
N, L, T, K = map(int, input().split())
list_A = list(map(int, input().split()))
table_C = [list(map(int, input().split())) for _ in range(L)]

# 初期値
table_cost = copy.deepcopy(table_C)
table_pow = [[0] * N for _ in range(L)]
table_B = [[1] * N for _ in range(L)]
apple_count = K

# 処理

for t in range(T):
    # 次の強化の決定処理
    out_i = -1
    out_j = -1
    for i in range(3, -1, -1):
        max_cost_performance = 0
        for j in range(N):
            if table_cost[i][j] <= apple_count:
                # 残りのターン数で増やせる機械の数
                now_add_apple_per_turn = 1
                for k in range(i - 1, -1, -1):
                    now_add_apple_per_turn *= table_pow[k][j]

                # 増えるりんごの数
                now_add_apple = list_A[j] * now_add_apple_per_turn * (T - t)

                now_cost_performance = now_add_apple / table_cost[i][j]

                if now_cost_performance > max_cost_performance:
                    out_i = i
                    out_j = j
                    max_cost_performance = now_cost_performance

        # レベルの高い方が高パフォーマンスと考える
        if out_j != -1:
            break

    # 出力
    if out_j == -1:
        print(-1)
    else:
        print(str(out_i) + " " + str(out_j))
        apple_count -= table_cost[out_i][out_j]
        table_pow[out_i][out_j] += 1
        table_cost[out_i][out_j] += table_C[out_i][out_j]

    # りんごの加算
    for j in range(N):
        apple_count += list_A[j] * table_B[0][j] * table_pow[0][j]

    # powの加算
    for i in range(1, 3):
        for j in range(N - 1, -1, -1):
            if table_pow[i][j] != 0:
                table_B[i - 1][j] += table_B[i][j] * table_pow[i][j]
