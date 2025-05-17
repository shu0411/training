import io
import sys

_INPUT = """\
20003 4 5
1 2
1 3
3 4
3 1
2 2
5
1 1
1 2
2 2
2 4
1 2

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
H, W, N = map(int, input().split())
list_XY = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())

#処理
dict_X = {}
dict_Y = {}
for i,XY in enumerate(list_XY):
    if XY[0] not in dict_X:
        dict_X[XY[0]] = [i]
    else:
        dict_X[XY[0]].append(i)
    if XY[1] not in dict_Y:
        dict_Y[XY[1]] = [i]
    else:
        dict_Y[XY[1]].append(i)

for i in range(Q):
    #入力
    a,b = map(int, input().split())
    
    #出力
    out = 0 #出力用変数
    if a == 1 and b in dict_X:  #X座標を見て、b行目の件数を数える
        for j in dict_X[b]:
            if list_XY[j][0] == b:
                out += 1
                list_XY[j] = [0, 0] #カウントしたマスは0にしておく
        dict_X[b] = [] #一度カウントした行は空にしておく
    elif a == 2 and b in dict_Y: #Y座標を見て、b列目の件数を数える
        for j in dict_Y[b]:
            if list_XY[j][1] == b:
                out += 1
                list_XY[j] = [0, 0] #カウントしたマスは0にしておく
        dict_Y[b] = [] #一度カウントした行は空にしておく

    #出力
    print(out)