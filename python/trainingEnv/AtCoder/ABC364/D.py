import io
import sys

_INPUT = """\
10 5
-84 -60 -41 -100 8 -8 -52 -62 -61 -76
-52 5
14 4
-2 6
46 2
26 7
"""
sys.stdin = io.StringIO(_INPUT)

#点bとの距離が、k番目に近い点aとの距離を出力する。
#例）
# 1行目: -2とAの距離が、1,1,7,8なので、3番目に近いのは7
# 2行目: 2とAの距離が、5,3,3,4なので、1番目に近いのは3
# 3行目: 10とAの距離が、13,11,5,4なので、4番目に近いのは13

#bごとに計算すると、TLE
#############ここから下をコピペ#############

#入力
N,Q = map(int, input().split())
list_A = list(map(int, input().split()))

#処理
list_A.sort()

for i in range(Q):
    #入力
    b,k = map(int, input().split())

    #処理
    out = 0
    if b < list_A[0]:
        out = list_A[k] - b
    elif b > list_A[-1]:
        out = b - list_A[-k]
    else:
        list_diff = []
        for a in list_A:
            list_diff.append(abs(b-a))
        list_diff.sort()
        out = list_diff[k-1]

    #出力
    print(out)

#→TLE