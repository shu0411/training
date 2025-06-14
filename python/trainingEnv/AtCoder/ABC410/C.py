import io
import sys

_INPUT = """\
1000000 3
1 1000000 999999
3 1000000001
2 1000000
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,Q = map(int, input().split())

#処理
list_num = [i for i in range(1,N+1)]
shift_times = 0
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        p,x = query[1], query[2]
        input_index = (p - 1 + shift_times) % N
        list_num[input_index] = x
    elif query[0] == 2:
        p = query[1]
        out_index = (p - 1 + shift_times) % N
        print(list_num[out_index])
    else:
        k = query[1]
        shift_times = (shift_times + k) % N