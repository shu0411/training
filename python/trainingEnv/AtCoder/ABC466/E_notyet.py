import io
import sys

_INPUT = """\
7 2
2 1
6 9
3 5
9 2
4 8
7 4
5 6

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, K = map(int, input().split())
list_AB = [list(map(int, input().split())) for _ in range(N)]

# 処理
out = N

# 出力
print(out)
