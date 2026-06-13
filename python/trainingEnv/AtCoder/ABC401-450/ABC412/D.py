import io
import sys

_INPUT = """\
8 21
1 4
5 7
8 4
3 4
2 5
8 1
5 1
2 8
2 1
2 4
3 1
6 7
5 8
2 7
6 8
5 4
3 8
7 3
7 8
5 3
7 4

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N,M = map(int, input().split())
list_AB = [list(map(int, input().split())) for _ in range(M)]

#処理
dic_edge = {}
dic_opposite = {}
for i in range(1, N + 1):
    dic_edge[i] = 0
    dic_opposite[i] = []

for a, b in list_AB:
    dic_edge[a] += 1
    dic_opposite[a].append(b)
    dic_edge[b] += 1
    dic_opposite[b].append(a)

count_0 = 0
count_1 = 0
sum_over = 0
for i in range(1, N + 1):
    if dic_edge[i] == 0:
        count_0 += 1
    elif dic_edge[i] == 1:
        count_1 += 1
    sum_over += dic_edge[i] - 2

out = 0

if count_0 != 0:
    if count_0 == 1:
        out += 2
        sum_over += 4
        count_1 -= min(count_1, 2)
    elif count_0 == 2:
        out += 3
        sum_over += 6
        count_1 -= min(count_1, 2)
    else:
        out += count_0 * 2
        sum_over += count_0 * 2
        
if count_1 != 0:
    if count_1 == 1:
        out += 1
        sum_over += 2
    elif count_1 == 2:
        out += 3
        if count_1 == 0:
            sum_over += 4
        elif count_1 == 1:
            count_1 -= 1
            sum_over += 2
        else:
            count_1 -= 2
    else:
        out += count_1 // 2 + count_1 % 2
        sum_over += (count_1 // 2 + count_1 % 2) * 2

out += sum_over // 2

#出力
print(out)