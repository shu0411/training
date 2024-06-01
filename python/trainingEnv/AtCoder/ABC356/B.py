import io
import sys

_INPUT = """\
2 4
10 20 30 40
20 0 10 30
0 20 100 10
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M = map(int,input().split())
list_A = list(map(int,input().split()))
table_X = [list(map(int,input().split())) for _ in range(N)]

#処理
get_list = [0]*M
for i in range(N):
    list_X = table_X[i]
    for j in range(M):
        get_list[j] += list_X[j]

out = "Yes"
for i in range(M):
    if get_list[i] < list_A[i]:
        out = "No"
        break

#出力
print(out)