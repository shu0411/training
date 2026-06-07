import io
import sys

_INPUT = """\
7 9 5
2 4
1 3
2 1
2 1
1 3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
H, W, Q = map(int, input().split())

# 処理
now_H = H
now_W = W
for _ in range(Q):
    list_query = list(map(int, input().split()))
    if list_query[0] == 1:
        R = list_query[1]
        out = R * now_W
        now_H -= R
    else:
        C = list_query[1]
        out = C * now_H
        now_W -= C

    # 出力
    print(out)
