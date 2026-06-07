import io
import sys

_INPUT = """\
3 3 6
00
00
00
000
000
0 0
0 2
1 1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N, M, K = map(int, input().split())

# 処理
list_dir = ["D", "R", "U", "L"]

# 出力
print(N)
