import io
import sys

_INPUT = """\
8 5
5 8 10 14 15 15 20 21

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N, M = map(int, input().split())
list_X = list(map(int, input().split()))

#処理
sorted_X = sorted(list_X)
dic_diff_X = {}
for i in range(N - 1):
    diff = sorted_X[i + 1] - sorted_X[i]
    dic_diff_X[i] = diff

dic_diff_X_sorted = sorted(dic_diff_X.items(), key=lambda x: x[1], reverse=True)

list_cut_point = []
for i in range(M - 1):
    list_cut_point.append(dic_diff_X_sorted[i][0])

list_cut_point.sort()

out = 0
begin_X = sorted_X[0]
for cut_point in list_cut_point:
    out += sorted_X[cut_point] - begin_X
    begin_X = sorted_X[cut_point + 1]

out += sorted_X[-1] - begin_X

#出力
print(out)