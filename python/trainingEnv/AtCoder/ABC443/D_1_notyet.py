import io
import sys

_INPUT = """\
5
5
5 2 1 3 4
2
1 1
3
1 3 1
9
9 9 8 2 4 4 3 5 3
20
7 4 6 2 15 5 17 15 1 8 18 1 5 1 12 11 2 7 8 14

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
T = int(input())

# 処理
for _ in range(T):
    N = int(input())
    list_R = list(map(int, input().split()))

    out = 0

    # 出力
    print(out)
