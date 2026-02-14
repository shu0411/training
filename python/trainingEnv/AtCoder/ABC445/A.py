import io
import sys

_INPUT = """\
rule

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

# 処理
first = S[0]
last = S[-1]

out = "No"
if first == last:
    out = "Yes"

# 出力
print(out)
