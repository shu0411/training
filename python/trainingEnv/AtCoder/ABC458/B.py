import io
import sys

_INPUT = """\
3 3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
H, W = map(int, input().split())

# 処理
table_out = [[0 for _ in range(W)] for _ in range(H)]

# 下
for h in range(H - 1):
    for w in range(W):
        table_out[h][w] += 1
# 上
for h in range(1, H):
    for w in range(W):
        table_out[h][w] += 1
# 右
for h in range(H):
    for w in range(W - 1):
        table_out[h][w] += 1
# 右
for h in range(H):
    for w in range(1, W):
        table_out[h][w] += 1

# 出力
for list_out in table_out:
    print(*list_out)
