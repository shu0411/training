import io
import sys

_INPUT = """\
10
10 7 3 9 1 3 8 5 7 10
3 6
8 6
6 1
9 7
7 10
5 4
4 2
10 2
1 9

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
from collections import deque

# 入力
N = int(input())
list_A = [0] + list(map(int, input().split()))

dict_tree = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    U, V = map(int, input().split())
    dict_tree[U].append(V)
    dict_tree[V].append(U)

# 処理
list_set_pair = [set() for _ in range(N + 1)]
list_out = [""] * (N + 1)

queue_visit = deque([1])
list_out[1] = "No"
list_set_pair[1] = set([list_A[1]])

while queue_visit:
    check_node = queue_visit.popleft()
    before_set_pair = list_set_pair[check_node]
    before_out = list_out[check_node]

    for next_node in dict_tree[check_node]:
        if list_out[next_node] == "":
            queue_visit.append(next_node)

            next_value = list_A[next_node]
            if before_out == "Yes":
                list_out[next_node] = "Yes"
            elif next_value in before_set_pair:
                list_out[next_node] = "Yes"
            else:
                list_out[next_node] = "No"
                next_set_pair = before_set_pair.copy()
                next_set_pair.add(list_A[next_node])
                list_set_pair[next_node] = next_set_pair

# 出力
for out in list_out[1:]:
    print(out)
