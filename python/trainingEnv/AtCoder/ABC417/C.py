import io
import sys

_INPUT = """\
30
8 3 6 4 9 6 5 6 5 6 3 4 7 3 7 4 9 8 5 8 3 6 8 8 4 5 5 5 6 5

"""
sys.stdin = io.StringIO(_INPUT)

#right - left == list_A[left] + list_A[right]
#right - list_A[right] == left + list_A[left]

#############ここから下をコピペ#############

#入力
N = int(input())
list_A = [0] + list(map(int, input().split()))

#処理
list_right_id_value_diff = {}
for i in range(1, N + 1):
    id_value_diff = i - list_A[i]
    if id_value_diff not in list_right_id_value_diff:   
        list_right_id_value_diff[id_value_diff] = 0
    list_right_id_value_diff[id_value_diff] += 1

list_left_id_value_sum = {}
for left in range(1,N+1):
    id_value_sum = left + list_A[left]
    if id_value_sum not in list_left_id_value_sum:
        list_left_id_value_sum[id_value_sum] = 0
    list_left_id_value_sum[id_value_sum] += 1

out = 0
for id_value_sum, left_count in list_left_id_value_sum.items():
    if id_value_sum in list_right_id_value_diff:
        out += left_count * list_right_id_value_diff[id_value_sum]

#出力
print(out)