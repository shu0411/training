import io
import sys

_INPUT = """\
3 3
1 2 3

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, K = map(int, input().split())
list_A = list(map(int, input().split()))

# 処理
out = 1

# 出力
print(out)
