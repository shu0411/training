import io
import sys

_INPUT = """\
10
5 2 7 4 108728325 390529120 597713292 322456626 845148281 812604915

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_X = list(map(int, input().split()))

# 処理
out = 0
list_line = [0]
list_dist = [0]
for x in list_X:
    list_line.append(x)
    list_line.sort()
    idx_x = list_line.index(x)
    before_dist_l = list_dist[idx_x]
    before_dist_r = list_dist[idx_x + 1]


# 出力
print(out)
