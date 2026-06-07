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
#imos法を用いる
#入力
N,M = map(int, input().split())
list_LR = [list(map(int, input().split())) for _ in range(M)]

#処理
out = 0
list_begin = [0] * (N + 1)
list_end = [0] * (N + 1)

for L, R in list_LR:
    list_begin[L] += 1
    list_end[R] += 1

list_wall = [0] * (N + 1)
for i in range(1, N + 1):
    list_wall[i] = list_wall[i - 1] + list_begin[i] - list_end[i - 1]

min_wall = min(list_wall[1:])  # 0番目は無視して1からNまでの壁の数を調べる

#出力
print(min_wall)