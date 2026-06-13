import io
import sys

_INPUT = """\
1000000
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())

# 処理
set_out_a = set()
set_double_a = set()

max_y = int(N ** (1 / 2))
for y in range(1, max_y):
    for x in range(y + 1, N):
        tmp_a = x**2 + y**2

        if tmp_a > N:
            break

        if tmp_a in set_out_a:
            set_out_a.remove(tmp_a)
            set_double_a.add(tmp_a)
        elif tmp_a not in set_double_a:
            set_out_a.add(tmp_a)

list_out_a = sorted(list(set_out_a))

# 出力
print(len(list_out_a))
print(*list_out_a)
