import io
import sys

_INPUT = """\
10 20
5 9
1 4
3 8
1 6
4 10
5 7
5 6
3 7
3 6
5 10
1 3
3 4
6 7
1 2
4 7
1 5
1 9
9 10
4 5
8 9

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())
list_uv = []
for i in range(M):
    list_uv.append(list(map(int, input().split())))

# 処理
min_count = float("inf")
for i in range(2**N):
    bit_i = str(bin(i)[2:]).zfill(N + 1)

    count = 0
    for u, v in list_uv:
        if bit_i[u] == bit_i[v]:
            count += 1

    min_count = min(count, min_count)

# 出力
print(min_count)
