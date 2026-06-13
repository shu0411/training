import io
import sys

_INPUT = """\
3
2 1
1 3
3 2

"""
sys.stdin = io.StringIO(_INPUT)

# X,Yの両方が自分より小さい点がなければ＋１

#############ここから下をコピペ#############

# 入力
N = int(input())
dict_i_XY = {}
dict_X_Y = {i:-1 for i in range(1,N+1)}
out = 0
for i in range(1,N+1):
    X,Y = map(int,input().split())
    dict_i_XY[i] = (X,Y)
    dict_X_Y[X] = Y

# 処理
for i,XY in dict_i_XY.items():
    X,Y = XY
    list_Y = list(dict_X_Y.values())[:X-1]
    if X == 1 or min(list_Y) > Y:
        out += 1

# 出力
print(out)
