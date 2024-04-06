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

#処理
tmp = "oox" * 34
out = tmp[:N]

#出力
print(out)