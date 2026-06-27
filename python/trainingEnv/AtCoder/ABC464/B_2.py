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
table_C = ["." + input() + "." for _ in range(H)]

# 処理
list_has_black = [False] * (W + 2)
exists_black_h = False
max_black_h = 0
for i, C in enumerate(table_C):
    if "#" in C:
        max_black_h = i
        if not exists_black_h:
            exists_black_h = True
            min_black_h = i

        for j, c in enumerate(list(C)):
            if c == "#":
                list_has_black[j] = True

exists_black_w = False
max_black_w = 0
for i, has_black in enumerate(list_has_black):
    if has_black:
        max_black_w = i
        if not exists_black_w:
            exists_black_w = True
            min_black_w = i

table_out = []
for i, C in enumerate(table_C):
    if min_black_h <= i <= max_black_h:
        table_out.append(C[min_black_w : max_black_w + 1])

# 出力
for out in table_out:
    print(out)
