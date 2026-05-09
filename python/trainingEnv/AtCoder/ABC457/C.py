import io
import sys

_INPUT = """\
3 3163812
5 1 2 3 4 5
4 9 8 7 6
2 10 11
87043 908415 9814

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, K = map(int, input().split())
list_LA = [list(map(int, input().split())) for _ in range(N)]
list_C = list(map(int, input().split()))

# 処理
left = K
for i, C in enumerate(list_C):
    L = list_LA[i][0]
    if left - C * L > 0:
        left -= C * L
    else:
        mod = left % L
        if mod == 0:
            mod = L
        out = list_LA[i][mod]
        break

# 出力
print(out)
