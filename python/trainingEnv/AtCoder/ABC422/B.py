import io
import sys

_INPUT = """\
15 18
##.###..##.##..##.
##.#.##.##.##.####
...##.#.......####
###.###....###.##.
#.##.......#.#....
#..#.##.##.#.#....
#.########.####.##
#.##.##.#....##.##
#......##.........
##.##..#..##..####
.#.#####..#####..#
.#..#...##.#.....#
.#..#.####.#.....#
.##.#.#.#..##..###
..###.###...####..

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
H,W = map(int, input().split())
list_S = [input() for _ in range(H)]

#処理
out = "Yes"
dir_x = [1, -1, 0, 0]
dir_y = [0, 0, 1, -1]
for i in range(H):
    for j in range(W):
        if list_S[i][j] == "#":
            cnt = 0
            for d in range(4):
                ni = i + dir_x[d]
                nj = j + dir_y[d]
                if 0 <= ni < H and 0 <= nj < W and list_S[ni][nj] == "#":
                    cnt += 1
            if cnt != 2 and cnt != 4:
                out = "No"
                break
    if out == "No":
        break


#出力
print(out)