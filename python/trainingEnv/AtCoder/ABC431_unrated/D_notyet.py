import io
import sys

_INPUT = """\
3
1 41 59
2 65 35
8 97 93

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())

list_WHB = []
sum_W = 0
for i in range(N):
    WHB = list(map(int, input().split()))
    list_WHB.append(WHB)
    sum_W += WHB[0]

# 処理
dp = [[0] * sum_W] * N

for i in range(N):
    pass

# 出力
