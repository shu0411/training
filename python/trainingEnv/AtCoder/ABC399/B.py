import io
import sys

_INPUT = """\
3
3 9 6

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_P = list(map(int, input().split()))

#処理
dicc_count_P = {}
for p in list_P:
    if p in dicc_count_P:
        dicc_count_P[p] += 1
    else:
        dicc_count_P[p] = 1 

sorted_dicc_count_P = sorted(dicc_count_P.items(), key=lambda x:x[0], reverse=True)

rank = 1
rank_P = {}
for count_P in sorted_dicc_count_P:
    rank_P[count_P[0]] = rank
    rank += count_P[1]

for p in list_P:
    print(rank_P[p])
