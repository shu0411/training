import io
import sys

_INPUT = """\
6 7
1 5 5
2 6 5
3 3 1
3 3 6
4 1 6
6 3 6

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())

dict_kind = {}
list_list_ADB = []
for _ in range(N):
    list_ADB = list(map(int, input().split()))
    list_list_ADB.append(list_ADB)
    A = list_ADB[0]
    if A not in dict_kind:
        dict_kind[A] = 0
    dict_kind[A] += 1

# 処理
list_list_ADB.sort(key=lambda x: x[1])

count_kind = len(dict_kind)
list_diff = [0] * (M + 1)
for A, D, B in list_list_ADB:
    if A == B:
        continue
    tmp_diff = 0
    dict_kind[A] -= 1
    if dict_kind[A] == 0:
        del dict_kind[A]
        tmp_diff -= 1
    if B not in dict_kind:
        dict_kind[B] = 0
        tmp_diff += 1
    dict_kind[B] += 1
    list_diff[D] += tmp_diff

for j in range(1, M + 1):
    count_kind += list_diff[j]
    print(count_kind)
