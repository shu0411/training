import io
import sys

_INPUT = """\
12
vgxgpuam

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
N = int(input())
S = input()

# 処理
tmp = "o" * N + S
out = tmp[-N:]

# 出力
print(out)
