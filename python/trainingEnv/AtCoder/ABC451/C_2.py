import io
import sys

_INPUT = """\
12
2 256601193
1 85138616
1 202564041
2 276477192
1 55551662
1 170271057
2 754166580
1 854388209
1 772036624
2 651124113
1 301137866
2 290875185

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import heapq

# 入力
Q = int(input())

# 処理
total_cnt = 0
list_heap = []

for _ in range(Q):
    kind, h = map(int, input().split())

    if kind == 1:
        heapq.heappush(list_heap, h)
        total_cnt += 1
    else:
        while len(list_heap) >= 1:
            if list_heap[0] > h:
                break
            heapq.heappop(list_heap)
            total_cnt -= 1

    # 出力
    print(total_cnt)
