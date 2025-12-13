import io
import sys

_INPUT = """\
3
2 3
5 6
5 3 6
3 3
5 4 6
6 2 4
5 4
18 20 19 14 17
18 20 14 15

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
T = int(input())

# 処理
for i in range(T):
    # 入力
    N, M = map(int, input().split())
    list_X = list(map(int, input().split()))
    list_Y = list(map(int, input().split()))

    # 処理
    out = "Yes"
    table_out = [[0] * M for _ in range(N)]
    for i in range(N * M, 0, -1):
        if i in list_X and i in list_Y:
            x = list_X.index(i)
            y = list_Y.index(i)
            if table_out[x][y] != 0:
                out = "No"
                break
            else:
                table_out[x][y] = i

    # 出力
    print(out)
