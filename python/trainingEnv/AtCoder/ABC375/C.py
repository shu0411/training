import io
import sys

_INPUT = """\
12
.......#.###
#...#...#..#
###.#..#####
..#.#.#.#...
.#.....#.###
.......#.#..
#...#..#....
#####.......
...#...#.#.#
..###..#..##
#..#.#.#.#.#
.####.......
"""
sys.stdin = io.StringIO(_INPUT)

#外から4n+1番目→９０度回転
#外から4n+2番目→１８０度回転
#外から4n+3番目→２７０度回転
#外から4n番目→３６０度回転

#上下左右から何番目か→一番小さい値で判断

#############ここから下をコピペ#############

#入力
N = int(input())
table = [input() for _ in range(N)]

#処理
for y in range(N):
    yr = N-1-y
    out = ""
    for x in range(N):
        xr = N-1-x
        min_val = min(x,y,xr,yr)
        #外から4n+1番目→９０度回転(x,y)←(y,xr)
        if min_val % 4 == 0:
            out += table[xr][y]
        #外から4n+2番目→１８０度回転(x,y)←(yr,xr)
        elif min_val % 4 == 1:
            out += table[yr][xr]
        #外から4n+3番目→２７０度回転(x,y)←(yr,x)
        elif min_val % 4 == 2:
            out += table[x][yr]
        #外から4n番目→３６０度回転
        else:
            out += table[y][x]
    #出力
    print(out)