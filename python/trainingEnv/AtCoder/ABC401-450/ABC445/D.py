import io
import sys

_INPUT = """\
4 6 6
2 2
1 4
3 1
1 2
3 1
4 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
from collections import deque

# 入力
H, W, N = map(int, input().split())

list_hw = []

for i in range(N):
    h, w = map(int, input().split())
    list_hw.append((h, w, i))

# 処理
sorted_by_h = sorted(list_hw, key=lambda x: x[0], reverse=True)
queue_sorted_by_h = deque(sorted_by_h)
sorted_by_w = sorted(list_hw, key=lambda x: x[1], reverse=True)
queue_sorted_by_w = deque(sorted_by_w)

set_placed_idx = set()
list_place = []
max_h = H
max_w = W
next_x = 1
next_y = 1
while queue_sorted_by_h and queue_sorted_by_w:
    tmp_max_h = max_h
    tmp_max_w = max_w
    tmp_next_x = next_x
    tmp_next_y = next_y
    if queue_sorted_by_h[0][0] == max_h:
        h, w, i = queue_sorted_by_h.popleft()
        tmp_next_y += w
        tmp_max_w -= w
    else:
        h, w, i = queue_sorted_by_w.popleft()
        tmp_next_x += h
        tmp_max_h -= h

    if i in set_placed_idx:
        continue

    set_placed_idx.add(i)
    list_place.append((i, next_x, next_y))
    next_x = tmp_next_x
    next_y = tmp_next_y
    max_h = tmp_max_h
    max_w = tmp_max_w

list_place.sort()

# 出力
for i, x, y in list_place:
    print(str(x) + " " + str(y))
