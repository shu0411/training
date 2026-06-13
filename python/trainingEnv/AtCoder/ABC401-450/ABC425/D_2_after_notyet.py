import io
import sys

_INPUT = """\
9 9
.........
.........
.........
.........
....#....
.........
.........
.........
.........

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
H,W = map(int, input().split())
list_S = [input() for _ in range(H)]

#処理
target = []
for i in range(H):
    for j in range(W):
        if list_S[i][j] == '#':
            target.append((i, j))

while target:
    next_target = []
    for i, j in target:
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < H and 0 <= nj < W and list_S[ni][nj] == '.':
                # todo: 上下左右の#のカウント
                list_S[ni] = list_S[ni][:nj] + '#' + list_S[ni][nj+1:]
                next_target.append((ni, nj))
    target = next_target

out = 0
for i in range(H):
    out += list_S[i].count('#')

#出力
print(out)