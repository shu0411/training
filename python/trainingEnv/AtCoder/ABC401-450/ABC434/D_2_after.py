import io
import sys

_INPUT = """\
5
2 4 1 4
3 3 3 5
1 3 4 6
4 5 3 5
5 5 4 6

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())

table_imos_count = [[0] * 2002 for _ in range(2002)]
table_imos_number = [[0] * 2002 for _ in range(2002)]
for i in range(1, N + 1):
    U, D, L, R = map(int, input().split())
    table_imos_count[U][L] += 1
    table_imos_count[U][R + 1] -= 1
    table_imos_count[D + 1][L] -= 1
    table_imos_count[D + 1][R + 1] += 1
    table_imos_number[U][L] += i
    table_imos_number[U][R + 1] -= i
    table_imos_number[D + 1][L] -= i
    table_imos_number[D + 1][R + 1] += i

# 処理
# 横方向の加算
table_add_count = [[0] * 2001 for _ in range(2001)]
table_add_number = [[0] * 2001 for _ in range(2001)]
for y in range(1, 2001):
    for x in range(1, 2001):
        table_add_count[y][x] = table_add_count[y][x - 1] + table_imos_count[y][x]
        table_add_number[y][x] = table_add_number[y][x - 1] + table_imos_number[y][x]

# 縦方向の加算
table_count = [[0] * 2001 for _ in range(2001)]
table_number = [[0] * 2001 for _ in range(2001)]
for y in range(1, 2001):
    for x in range(1, 2001):
        table_count[y][x] = table_count[y - 1][x] + table_add_count[y][x]
        table_number[y][x] = table_number[y - 1][x] + table_add_number[y][x]

# 雲がない場所と雲が1つだけの場所のカウント
count_zero = 0
list_count_only = [0 for _ in range(N + 1)]
for y in range(1, 2001):
    for x in range(1, 2001):
        if table_count[y][x] == 0:
            count_zero += 1
        if table_count[y][x] == 1:
            list_count_only[table_number[y][x]] += 1

# 出力
for i in range(1, N + 1):
    print(count_zero + list_count_only[i])
