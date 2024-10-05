import io
import sys

_INPUT = """\
3 2 1
1 3 2 1
0 2 0 0
3 0 2 0
"""
sys.stdin = io.StringIO(_INPUT)

#(A,B)→(C,D)移動中の速度S
#線分の端から次の線分の端までの速度T
#まずは(A,B)→(C,D)の時間を求める
#次に、線分の端から次の線分の端までの時間を求める
#ここでは、どちらの端から始めるか2**6通りを試す

#############ここから下をコピペ#############
import math

#入力
N,S,T = map(int, input().split())
list_ABCD = [list(map(int, input().split())) for _ in range(N)]

#処理
time = 0
#線分を描く時間
len_S = 0
for ABCD in list_ABCD:
    A,B,C,D = ABCD
    len_S += math.sqrt((C-A)**2 + (D-B)**2)

time = len_S / S

#線分の端から次の線分の端までの時間
def calc_len(n):
    if n == -1:
        return [[0,0,0]]
    else:
        before_list = calc_len(n-1)

        list_len = []
        for before in before_list:
            before_len = before[0]
            before_X = before[1]
            before_Y = before[2]
            for i in range(2):
                if i == 0:
                    X = list_ABCD[n][0]
                    Y = list_ABCD[n][1]
                else:
                    X = list_ABCD[n][2]
                    Y = list_ABCD[n][3]
                
                len_ = before_len + math.sqrt((X-before_X)**2 + (Y-before_Y)**2)
                list_len.append([len_,X,Y])
            
        return list_len


list_len_T = calc_len(N-1)
len_T = 10 ** 9
for len_ in list_len_T:
    len_T = min(len_T, len_[0])
time += len_T / T

#出力
print(time)

#順番変えた場合を考慮する。