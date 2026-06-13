import io
import sys

_INPUT = """\
5
3 1 4 2 5

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
# import sys

sys.setrecursionlimit(300000)

# 入力
N = int(input())
list_P = [0] + list(map(int, input().split()))


def search_next(idx, origin, group: list[int]):
    next_num = list_P[idx]
    visited[idx] = True
    group.append(next_num)
    if next_num == origin:
        return group

    search_next(next_num, origin, group)

    return group


# 処理
visited = [False] * (N + 1)
out = 0
for i in range(1, N + 1):
    if visited[i] or list_P[i] == i:
        continue

    visited[i] = True
    new_group = [list_P[i]]
    fixed_group = search_next(list_P[i], i, new_group)
    len_group = len(fixed_group)
    out += len_group * (len_group - 1) // 2

# 出力
print(out)
