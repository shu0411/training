import io
import sys

_INPUT = """\
1
5 100 200 300 400 500
1 5

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_LA = [list(map(int, input().split())) for _ in range(N)]
X, Y = map(int, input().split())

# 処理
out = list_LA[X - 1][Y]

# 出力
print(out)
