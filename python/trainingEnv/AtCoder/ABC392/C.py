import io
import sys

_INPUT = """\
10
2 6 4 3 7 8 9 10 1 5
1 4 8 2 10 5 7 3 9 6
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_P = [0] + list(map(int, input().split()))
list_Q = [0] + list(map(int, input().split()))

#処理
dict_Q = {}
for i,q in enumerate(list_Q):
    dict_Q[q] = i

out_list = []
for i in range(1, N+1):
    wear_id = dict_Q[i]
    see_id = list_P[wear_id]
    out_list.append(list_Q[see_id])

#出力
print(*out_list)