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
# <反省>
# 点の番号を無視してよいことに気付くのが遅かった
#############ここから下をコピペ#############

# 入力
N = int(input())
list_XY = []
out = 0
for i in range(1, N + 1):
    X, Y = map(int, input().split())
    list_XY.append((X, Y))

# 処理
list_XY.sort()
min_Y = N + 1
out = 0
for X, Y in list_XY:
    if Y < min_Y:
        out += 1
        min_Y = Y

# 出力
print(out)
