import io
import sys

_INPUT = """\
.#......
..#..#..
....#...
........
..#....#
........
...#....
....#...

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
table = [input() for _ in range(8)]

#処理
out = 0
tmp_x = 0
tmp_y = 0
for i in range(8):
    if "#" not in table[i]:
        tmp_y += 1

for j in range(8):
    for k in range(8):
        if table[k][j] == "#":
            break
    else:
        tmp_x += 1

out = tmp_x * tmp_y

#出力
print(out)