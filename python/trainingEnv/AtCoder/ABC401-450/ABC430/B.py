import io
import sys

_INPUT = """\
10 3
..#.......
.###......
.#.#......
#####.....
#...#.....
......####
......#..#
......#...
......#..#
......####

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())
table_S = [input() for _ in range(N)]

# 処理
set_M = set()

for i in range(N - M + 1):
    for j in range(N - M + 1):
        tmp_M = ""
        for k in range(i, i + M):
            tmp_M += table_S[k][j : j + M]
        set_M.add(tmp_M)

# 出力
print(len(set_M))
