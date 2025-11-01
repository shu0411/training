import io
import sys

_INPUT = """\
5 3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M = map(int, input().split())

# 処理
for i in range(N):
    if i < M:
        out = "OK"
    else:
        out = "Too Many Requests"

    # 出力
    print(out)
