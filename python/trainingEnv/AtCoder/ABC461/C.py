import io
import sys

_INPUT = """\
5 3 2
1 30
1 40
1 50
2 10
3 20

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
from collections import deque

# 入力
N,K,M = map(int,input().split())
max_CV = {}
list_V = []
for i in range(N):
    C,V = map(int,input().split())
    if C not in max_CV:
        max_CV[C] = V
    else:
        max_CV[C] = max(max_CV[C],V)
    list_V.append(V)

# 処理
list_max_V = list(max_CV.values())
list_max_V.sort(reverse=True)
list_V.sort(reverse=True)

list_selected_max_V = list_max_V[:M]
out = sum(list_selected_max_V)

queue_max_V = deque(list_selected_max_V)
queue_V = deque(list_V)

now_count = M
len_queue_max_V = len(queue_max_V)
while now_count < K:
    tmp_v = queue_V.popleft()
    if len_queue_max_V > 0 and tmp_v == queue_max_V[0]:
        queue_max_V.popleft()
        len_queue_max_V -= 1
    else:
        now_count += 1
        out += tmp_v

# 出力
print(out)
