import io
import sys

_INPUT = """\
5
5 3
.###.
..#..
#.#.#
#...#
##..#
2 2
##
..
4 1
####
####
####
.###
3 3
...
...
...
10 3
##.##.##.#
.####..#..
...#.#..#.
.#.#.#.#..
...####...
#.#.##....
.##...#...
#.##.....#
#....###.#
.#..#.#...

"""
sys.stdin = io.StringIO(_INPUT)

# スタートから斜めに上がっていくルートより下に壁がある場合その列は×
# それ以外の場合は○
#############ここから下をコピペ#############

# 入力
T = int(input())

# 処理
for _ in range(T):
    N, C = map(int, input().split())
    table_S = [input() for _ in range(N)]

    breakable = [False] * (N + 2)
    reachable = [[False] * (N + 2) for _ in range(N)]

    # 初期位置だけ到達可能に
    breakable[C] = True
    reachable[N - 1][C] = True

    for i in range(N - 2, -1, -1):
        for j in range(1, N + 1):
            # (N,C)から斜めに到達可能でない場合スキップ
            if j < C - (N - 1 - i) or j > C + (N - 1 + i):
                continue

            # その列が壁を壊せるか判定
            if j == C - (N - 1 - i) or j == C + (N - 1 - i):
                tmp_breakable = True
                # 1つ前の列が壁を壊せた場合、かつ、その点より下に壁がなかった場合その列はそれ以降壁を壊せる
                if breakable[j + 1] or breakable[j - 1]:
                    for tmp_i in range(i + 1, N):
                        if table_S[tmp_i][j - 1] == "#":
                            tmp_breakable = False
                            break
                    breakable[j] = tmp_breakable

            # その点が到達可能か判定
            reachable[i][j] = (
                reachable[i + 1][j - 1]
                or reachable[i + 1][j]
                or reachable[i + 1][j + 1]
            ) and (table_S[i][j - 1] == "." or breakable[j])

    out = "".join(["1" if tmp else "0" for tmp in reachable[0][1 : (N + 1)]])

    # 出力
    print(out)
