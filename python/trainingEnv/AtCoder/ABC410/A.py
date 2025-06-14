import io
import sys

_INPUT = """\
2
1 2 3
"""
sys.stdin = io.StringIO(_INPUT)

#############ここから下をコピペ#############

#入力
N = int(input())
list_S = input().split()

#処理
out = N

#出力
print(out)