import io
import sys

_INPUT = """\
2 4
S.xG
#?o.

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
H,W = map(int, input().split())
table = [["#"] * (W*2)]
for i in range(H):
    row = ["#"] + list(input()) + ["#"]
    table.append(row)

table.append(["#"] * (W*2))

#処理
out = 0

#方向
dirX = [0, 1, 0, -1]
dirY = [1, 0, -1, 0]

#最短経路を保持する変数
dist = [[-1] * (W*2) for _ in range(H+2)]

#S,Gの位置を特定
start = goal = None
for i in range(H+2):
    for j in range(W*2):
        if table[i][j] == "S":
            start = (i, j)
        elif table[i][j] == "G":
            goal = (i, j)

#BFS
queue = [start]
dist[start[0]][start[1]] = 0

while queue:
    x, y = queue.pop(0)
    if (x, y) == goal:
        out = dist[x][y]
        break
    for d in range(4):
        nx, ny = x + dirX[d], y + dirY[d]
        if table[nx][ny] == "#" or table[nx][ny] == "x" or dist[nx][ny] != -1:
            continue
        dist[nx][ny] = dist[x][y] + 1
        queue.append((nx, ny))

#出力
print(out)