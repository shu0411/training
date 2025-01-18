import io
import sys

_INPUT = """\
7
1 5
1 7
3 2
1 3
1 4
2
3 3
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############
import queue
#入力
Q = int(input())

#処理
line_queue = queue.Queue()
sum_line = 0
list_sum_line = [0]
sum_outline = 0
count_out = 0
for i in range(Q):
    #入力
    list_query = list(map(int, input().split()))
    type = list_query[0]
    if type == 1:
        l = list_query[1]
        line_queue.put(l)
        sum_line += l
        list_sum_line.append(sum_line)
    elif type == 2:
        outline = line_queue.get()
        sum_outline += outline
        count_out += 1
    elif type == 3:
        k = list_query[1]
        print(list_sum_line[k + count_out - 1] - sum_outline)
