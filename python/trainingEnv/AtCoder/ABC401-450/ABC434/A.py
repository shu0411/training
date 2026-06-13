import io

import sys

_INPUT = """\
100 100

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
W, B = map(int, input().split())

# 処理
out = W * 1000 // B + 1

# 出力
print(out)
