import io
import sys

_INPUT = """\
3 4
#...
....
...#

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
H, W = map(int, input().split())
table_C = [input() for _ in range(H)]

# 処理
count_first_black = 0
count_last_black = 0
for C in table_C:
    if C[0] == "#":
        count_first_black += 1
    if C[-1] == "#":
        count_last_black += 1

table_out = []
for i, C in enumerate(table_C):
    if (i == 0) and "#" not in table_C[0]:
        continue

    if (i == H - 1) and "#" not in table_C[H - 1]:
        continue

    tmp_C = C
    if count_first_black == 0:
        tmp_C = tmp_C[1:]
    if count_last_black == 0:
        tmp_C = tmp_C[:-1]

    table_out.append(tmp_C)

# 出力
for out in table_out:
    print(out)
