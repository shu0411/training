import io
import sys

_INPUT = """\
8 20
9 19 14 17 17 4 18 4

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, X = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
for A in list_A:
    if A < X:
        X = A
        # 出力
        print(1)
    else:
        # 出力
        print(0)
