import io
import sys

_INPUT = """\
6
91 999999986
53 999999997
32 999999932
14 999999909
49 999999985
28 999999926

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_RC = []
min_R = 10 ** 9
max_R = 1
min_C = 10 ** 9
max_C = 1
for i in range(N):
    R, C = map(int, input().split())
    list_RC.append((R, C))
    min_R = min(min_R, R)
    max_R = max(max_R, R)
    min_C = min(min_C, C)
    max_C = max(max_C, C)

#処理
R_times = (max_R - min_R + 1) // 2
C_times = (max_C - min_C + 1) // 2
out = max(R_times, C_times)

#出力
print(out)