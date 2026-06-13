import io
import sys

_INPUT = """\
10plus2is12

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

# 処理
out = ""
for s in list(S):
    if s.isdecimal():
        out += s

# 出力
print(out)
