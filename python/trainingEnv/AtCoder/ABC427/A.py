import io
import sys

_INPUT = """\
ATCODER

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
center = (len(S) + 1) // 2
out = S[:center-1] + S[center:]

#出力
print(out)