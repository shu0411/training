import io
import sys

_INPUT = """\
5
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())

# 処理
table_out = [[0] * N for _ in range(N)]

next_i = 0
next_j = (N - 1) // 2
for i in range(1, N**2 + 1):
    table_out[next_i][next_j] = i

    if table_out[(next_i - 1 + N) % N][(next_j + 1 + N) % N] == 0:
        next_i = (next_i - 1 + N) % N
        next_j = (next_j + 1 + N) % N
    else:
        next_i = (next_i + 1 + N) % N

# 出力
for i in range(N):
    print(*table_out[i])
