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
list_list_taple_line = [[] for _ in range(2001)]
for i in range(1, N + 1):
    U, D, L, R = map(int, input().split())
    for j in range(U, D + 1):
        list_list_taple_line[j].append((i, L, 1))
        list_list_taple_line[j].append((i, R + 1, -1))

count_any = 0
list_count_only = [0 for _ in range(N + 1)]
for list_taple_line in list_list_taple_line:
    list_taple_line.sort(key=lambda x: x[1])
    now_count = 0
    now_pos = 0
    now_idx = set()
    for idx, pos, diff in list_taple_line:
        if now_count != 0:
            count_any += pos - now_pos
            if now_count == 1:
                list_idx = list(now_idx)
                list_count_only[list_idx[0]] += pos - now_pos

        if diff == 1:
            now_idx.add(idx)
        else:
            now_idx.remove(idx)

        now_count += diff
        now_pos = pos

# 出力
for i in range(1, N + 1):
    print(2000 * 2000 - count_any + list_count_only[i])
