import io
import sys

_INPUT = """\
3 2
1 2
2 3
SSD


"""
sys.stdin = io.StringIO(_INPUT)

# 各Dの頂点から、1番近いSと2番目に近いSを求め、そこまでの経路を足す。
#############ここから下をコピペ#############

import queue

# 入力
N, M = map(int, input().split())
dict_vector = {i: [] for i in range(N)}
for _ in range(M):
    u, v = map(int, input().split())
    dict_vector[u - 1].append(v - 1)
    dict_vector[v - 1].append(u - 1)

S = input()

# 処理
out = N
list_safety = []
list_danger = []
for i, s in enumerate(S):
    if s == "D":
        list_danger.append(i)
    else:
        list_safety.append(i)

for i in list_danger:
    # BFS
    list_visited_count = [-1] * N
    q = queue.Queue()

    q.put(i)
    list_visited_count[i] = 0
    while not q.empty():
        u = q.get()

        for v in dict_vector[u]:
            if list_visited_count[v] != -1:
                continue
            list_visited_count[v] = list_visited_count[u] + 1
            q.put(v)

    list_visited_count_sorted = sorted(
        enumerate(list_visited_count), key=lambda x: x[1]
    )

    first_count = 0
    second_count = 0
    for id_str, visited_count in list_visited_count_sorted:
        if S[id_str] == "S":
            if first_count == 0:
                first_count = visited_count
            else:
                second_count = visited_count

        if second_count != 0:
            break

    out = first_count + second_count

    # 出力
    print(out)
