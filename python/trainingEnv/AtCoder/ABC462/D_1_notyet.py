import io
import sys

_INPUT = """\
3 2
9 17
10 12
13 20

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, D = map(int, input().split())
list_ST = [tuple(map(int, input().split())) for _ in range(N)]


# 処理
out = N

# 出力
print(out)
