import io
import sys

_INPUT = """\
7
1 3
4 3 4 6 7
1 7
3 2 6 7
2 3 7
1 4
1 5

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())

# 処理
dic_given = {i: [] for i in range(1, N + 1)}
for i in range(1, N + 1):
    list_KA = list(map(int, input().split()))
    for A in list_KA[1:]:
        dic_given[A].append(i)

# 出力
for X, list_B in dic_given.items():
    print(len(list_B), *list_B)
