import io
import sys

_INPUT = """\
2025 1111
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
A,B = map(int, input().split())

#処理
out = (A + B) ** 2

#出力
print(out)