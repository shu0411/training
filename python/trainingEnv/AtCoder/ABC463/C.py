import io
import sys

_INPUT = """\
10
587 138
772 155
755 404
519 408
529 432
169 586
114 632
249 656
329 972
299 984
14
443 801 824 276 399 314 300 510 311 580 498 930 359 5

"""
sys.stdin = io.StringIO(_INPUT)

# L = 3 5 7
# T 3→3の時の最大 bisect_right=1→0
# T 4→3の時の最大 bisect_right=1→0
# T 5→5の時の最大 bisect_right=2→1
#############ここから下をコピペ#############
import bisect

# 入力
N = int(input())
list_HL = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
list_T = list(map(int, input().split()))

# 処理
list_L = []
dict_L_max_H = {}
max_H = 0
for H, L in reversed(list_HL):
    max_H = max(max_H, H)
    dict_L_max_H[L] = max_H
    list_L.append(L)

list_L.reverse()

for T in list_T:
    idx = bisect.bisect_right(list_L, T)
    target_L = list_L[idx]
    out = dict_L_max_H[target_L]

    # 出力
    print(out)
