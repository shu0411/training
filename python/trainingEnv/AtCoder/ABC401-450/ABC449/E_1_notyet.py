import io
import sys

_INPUT = """\
3 3
1 1 2
8
1
2
3
4
5
6
7
8

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())
list_A = list(map(int, input().split()))
Q = int(input().split())

for _ in range(Q):
    # 入力
    X = int(input().split())
    # 処理
    out = N

    # 出力
    print(out)
