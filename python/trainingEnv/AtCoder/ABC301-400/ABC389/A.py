import io
import sys

_INPUT = """\
9x9
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
S = input()

#処理
x = int(S[0])
y = int(S[2])   
out = x * y

#出力
print(out)