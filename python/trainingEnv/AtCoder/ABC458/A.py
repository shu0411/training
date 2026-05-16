import io
import sys

_INPUT = """\
burger
1

"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

# 入力
S = input()
N = int(input())

# 処理
out = S[N:-N]

# 出力
print(out)
