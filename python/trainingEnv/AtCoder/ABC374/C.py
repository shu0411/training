import io
import sys

_INPUT = """\
20
22 25 26 45 22 31
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_K = list(map(int, input().split()))

#処理
sum_K = sum(list_K)
half_sum_K = sum_K // 2

list_sum = [0]
for i in range(N):
    tmp_sum = []
    for sum_ in list_sum:
        if sum_ + list_K[i] <= half_sum_K:
            tmp_sum.append(sum_ + list_K[i])
    list_sum += tmp_sum

max_sum = max(list_sum)

#出力
print(sum_K - max_sum)