import io
import sys

_INPUT = """\
3
4 6 2
AABB
1 2
2 3
3 1
3 3
3 4
4 2
4 6 2
ABAB
1 2
2 3
3 1
3 3
3 4
4 2
5 8 3
ABABB
1 2
2 2
2 3
3 1
3 4
4 4
4 5
5 3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
T = int(input())

# 処理
for _ in range(T):
    # 入力
    N, M, K = map(int, input().split())
    S = input()
    dic_edge = {i: [] for i in range(1, N + 1)}
    count_from = [0] * (N + 1)
    for i in range(M):
        U, V = list(map(int, input().split()))
        dic_edge[U].append(V)

    # iターン目に駒がvにある状態から、手番プレイヤーが勝てるか
    dp = [[False] * (N + 1)] * (K * 2 + 1)

    dp[K * 2] = [False] + [(s == "A") for s in S]

    for i in range(K * 2 - 1, -1, -1):
        tmp_dp = [False] * (N + 1)
        for u in range(1, N + 1):
            for v in dic_edge[u]:
                if not dp[i + 1][v]:
                    tmp_dp[u] = True
                    break
        dp[i] = tmp_dp

    out = ""
    if dp[0][1]:
        out = "Alice"
    else:
        out = "Bob"

    # 出力
    print(out)
