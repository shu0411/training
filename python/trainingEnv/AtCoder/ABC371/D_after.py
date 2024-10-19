import io
import sys

_INPUT = """\
7
-10 -5 -3 -1 0 1 4
2 5 6 5 2 1 7
8
-7 7
-1 5
-10 -4
-8 10
-5 0
-10 5
-8 7
-8 -3
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

import numpy as np
#入力
N = int(input())
np_X = np.array(list(map(int,input().split())))
np_P = np.array(list(map(int,input().split())))
Q = int(input())

#処理
out = N

#np_Pの累積和を取得
np_sum_P = np.cumsum(np_P)

for i in range(Q):
    L,R = map(int,input().split())

    #以下要修正。np_Xの中でL,R以下の最小の村を二分探索で取得する
    #np_Xの中でL以上の最小のxを取得
    #x_L = np_X[np_X >= L].min()
    #np_Xの中でR以下の最大のxを取得
    #x_R = np_X[np_X <= R].max()

    #x以上y以下のPの和を取得
    #if x_L == x_R:
    #    out = np_P[np_X == x_L][0]
    #else:
    #    out = np_sum_P[np_X == x_R][0] - np_sum_P[np_X == x_L][0] + np_P[np_X == x_L][0]
    #print(out)
