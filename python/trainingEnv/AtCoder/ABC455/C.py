import io
import sys

_INPUT = """\
6 2
7 2 7 2 2 9

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, K = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
dic_A = {}
for A in list_A:
    if A not in dic_A:
        dic_A[A] = 0
    dic_A[A] += 1

list_sum = []
for key, value in dic_A.items():
    list_sum.append(key * value)

list_sum.sort()

out = sum(list_sum[:-K])

# 出力
print(out)
