import io
import sys

_INPUT = """\
jjjjjj

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

# 処理
out = 0
for s in S:
    if s in ("i", "j"):
        out += 1

# 出力
print(out)
