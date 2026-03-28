import io
import sys

_INPUT = """\
illegal

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()

# 処理
len_S = len(S)
out = "No"
if len_S % 5 == 0:
    out = "Yes"

# 出力
print(out)
