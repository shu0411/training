import io
import sys

_INPUT = """\
5 10
2 5
1 5
1 2
2 4
2 2
5 5
2 4
1 2
2 2
2 3
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M = map(int, input().split())
list_LR = [list(map(int, input().split())) for _ in range(M)]

#処理
out = 0
list_wall = [N] + [0] * N

for L, R in list_LR:
    for i in range(L, R + 1):
        list_wall[i] += 1

min_wall = min(list_wall)

#出力
print(min_wall)