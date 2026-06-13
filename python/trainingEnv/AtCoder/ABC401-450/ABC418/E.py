import io
import sys

_INPUT = """\
8
0 1
1 3
2 3
3 1
0 2
1 0
2 0
3 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_XY = [list(map(int, input().split())) for _ in range(N)]

#処理
dic_tilt = {}
for i in range(N):
    xi, yi = list_XY[i]
    for j in range(i + 1, N):
        xj, yj = list_XY[j]
        tilt = (yj - yi) / (xj - xi) if xj != xi else float('inf')
        len2 = (xj - xi) ** 2 + (yj - yi) ** 2
        if tilt not in dic_tilt:
            dic_tilt[tilt] = []
        dic_tilt[tilt].append(len2)

count = 0
parallelogram_count = 0
for lengths in dic_tilt.values():
    if len(lengths) > 1:
        lengths.sort()
        n = len(lengths)
        count += n * (n - 1) // 2
        dic_length = {}
        for length in lengths:
            if length not in dic_length:
                dic_length[length] = 0
            dic_length[length] += 1
        for v in dic_length.values():
            if v > 1:
                parallelogram_count += v * (v - 1) // 2

out = count - (parallelogram_count // 2)

#出力
print(out)