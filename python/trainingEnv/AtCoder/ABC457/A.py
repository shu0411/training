import io
import sys

_INPUT = """\
10
4 4 4 3 4 2 1 1 2 1
10

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
list_A = list(map(int, input().split()))
X = int(input())

# 処理
out = list_A[X - 1]

# 出力
print(out)
