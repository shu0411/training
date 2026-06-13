import io
import sys

_INPUT = """\
10 24
279290 9485601 1
1094410 8022270 4
1314176 7214745 5
1897674 5924694 10
1921802 5769841 4
2506394 2765234 2
2558629 2727489 9
2681289 4061363 5
3022540 2291905 3
4407692 1313036 8

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

from collections import deque
import heapq

#入力
N,K = map(int, input().split())
wait_queue = deque()
for _ in range(N):
    A,B,C = map(int, input().split())
    wait_queue.append((A,B,C))

#処理
instore_queue = []
instore_count = 0
now_time = 0
while wait_queue:
    #退店処理
    while instore_queue and instore_queue[0][0] <= wait_queue[0][0]:
        left_time,count = heapq.heappop(instore_queue)
        instore_count -= count
        now_time = left_time
    
    while instore_queue and instore_count + wait_queue[0][2] > K:
        left_time,count = heapq.heappop(instore_queue)
        instore_count -= count
        now_time = left_time
    
    #入店処理
    A,B,C = wait_queue.popleft()
    now_time = max(now_time, A)
    heapq.heappush(instore_queue, (now_time + B,C))
    instore_count += C

    #出力
    print(now_time)
